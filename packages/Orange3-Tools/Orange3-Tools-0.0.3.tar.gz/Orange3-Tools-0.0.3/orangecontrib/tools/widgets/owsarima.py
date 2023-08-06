from AnyQt.QtCore import QTimer, Qt
from AnyQt.QtWidgets import QFormLayout
import numpy as np
from numbers import Number
from orangewidget.utils.widgetpreview import WidgetPreview
import Orange.data
from Orange.data import Table, Domain, TimeVariable
from Orange.widgets.widget import Input, Output
from more_itertools import unique_everseen

import statsmodels.api as sm
from itertools import chain
from Orange.widgets import widget, gui, settings
from os.path import join, dirname
from orangecontrib.timeseries import Timeseries as TS

class TimeDelta:
    _SPAN_DAY = {86400}
    _SPAN_MONTH = {2678400,  # 31 days
                   2592000,  # 30 days
                   2419200,  # 28 days
                   2505600}  # 29 days
    _SPAN_YEAR = {31536000,  # normal year
                  31622400}  # leap year

    def __init__(self, time_values):
        self.time_values = time_values
        self.backwards_compatible_delta = self._get_backwards_compatible_delta()

        self.is_equispaced = False
        self.time_interval = None
        self.deltas = []
        self.min = None
        if len(time_values) <= 1:
            return

        deltas = list(np.unique(np.diff(np.sort(self.time_values))))

        # in case several rows fall on the same datetime, remove the zero
        if deltas and deltas[0] == 0:
            deltas.pop(0)
            if not deltas:
                return

        if len(deltas) == 1:
            self.is_equispaced = True
            self.time_interval = deltas[0]

        # TODO detect multiple days/months/years
        for i, d in enumerate(deltas[:]):
            if d in self._SPAN_MONTH:
                deltas[i] = (1, 'month')
            elif d in self._SPAN_YEAR:
                deltas[i] = (1, 'year')
        # in case several months or years of different length were matched,
        # run it through another unique check
        deltas = list(unique_everseen(deltas))
        self.deltas = deltas

        self.min = deltas[0]

        # in setting the greatest common divisor...
        if all(isinstance(d, Number) for d in deltas):
            # if no tuple timedeltas, simply calculate the gcd
            self.gcd = int(np.gcd.reduce([int(d) for d in deltas]))
        elif all(isinstance(d, tuple) for d in deltas):
            # if all of them are tuples, use the minimum one
            self.gcd = self.min
        else:
            # else if there's a mix, use the numbers, and a day
            nds = [int(d) for d in deltas if isinstance(d, Number)]
            self.gcd = int(np.gcd.reduce(nds + list(self._SPAN_DAY)))

    def _get_backwards_compatible_delta(self):
        """
        Old definition of time delta, for backwards compatibility

        Return time delta (float) between measurements if uniform. Return None
        if not uniform. Return tuple (N, unit) where N is int > 0 and
        unit one of 'day', 'month', 'year'.
        """
        delta = np.unique(np.diff(self.time_values))
        if delta.size <= len(self._SPAN_MONTH):
            deltas = set(delta)
            if not (deltas - self._SPAN_YEAR):
                delta = ((1, 'year'),)
            elif not (deltas - self._SPAN_MONTH):
                delta = ((1, 'month'),)
            elif not (deltas - self._SPAN_DAY):
                delta = ((1, 'day'),)
        return delta[0] if len(delta) == 1 else None
class Timeseries(Table):

    from os.path import join, dirname
    Orange.data.table.dataset_dirs.insert(0, join(dirname(__file__), 'datasets'))
    del join, dirname

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._interp_method = 'linear'
        self._interp_multivariate = False
        self.time_delta = None

    def copy(self):
        other = super().copy()
        other._interp_method = self._interp_method
        other._interp_multivariate = self._interp_multivariate
        other.time_variable = self.time_variable
        # previous line already sets time_delta, but it could, in principle
        # be set differently, so let's copy it to be on the safe side
        other.time_delta = self.time_delta
        return other

    def __getitem__(self, key):
        ts = super().__getitem__(key)
        if isinstance(ts, Timeseries) and ts.time_variable not in ts.domain:
            ts.time_variable = None
        return ts

    @classmethod
    def from_data_table(cls, table, time_attr=None):
        if isinstance(table, Timeseries) and (
                time_attr is table.time_variable
                or time_attr is None and table.time_variable is not None):
            return table

        if time_attr is not None:
            if time_attr not in table.domain:
                raise Exception(time_attr.name + ' is not in the domain.')
            if not time_attr.is_continuous:
                raise Exception(time_attr.name + ' must be continuous.')
        else:
            for time_attr in chain(table.domain.attributes, table.domain.metas):
                if time_attr.is_time:
                    break
            else:
                return super(Timeseries, cls).from_table(table.domain, table)

        return cls.make_timeseries_from_continuous_var(table, time_attr)

    @classmethod
    def convert_from_data_table(cls, table, time_attr=None):
        """
        Create TimeSeries and re-assign the original arrays to the new table

        The goal of this is to ensure the timeseries objects owns its data
        if it can. Therefore, re-assignment happens only if an array is a view
        into the table (which also means that the `table` itself is not a view)
        """
        ts = cls.from_data_table(table, time_attr)
        for attr in ("X", "Y", "metas", "W"):
            orig = getattr(table, attr)
            new =  getattr(ts, attr)
            if new.base is orig:
                with ts.unlocked_reference(new):
                    setattr(ts, attr, orig)
        return ts

    @classmethod
    def from_domain(cls, *args, time_attr=None, **kwargs):
        table = Table.from_domain(*args, **kwargs)
        return cls.convert_from_data_table(table, time_attr=time_attr)

    @classmethod
    def from_table(cls, domain, source, *args, time_attr=None, **kwargs):
        if not isinstance(source, Timeseries):
            table = Table.from_table(domain, source, *args, **kwargs)
            return cls.convert_from_data_table(table, time_attr=time_attr)
        return super().from_table(domain, source, *args, **kwargs)

    @classmethod
    def from_numpy(cls, *args, time_attr=None, **kwargs):
        table = Table.from_numpy(*args, **kwargs)
        return cls.convert_from_data_table(table, time_attr=time_attr)

    @classmethod
    def from_list(cls, *args, **kwargs):
        table = Table.from_list(*args, **kwargs)
        return cls.convert_from_data_table(table)

    @classmethod
    def from_file(cls, *args, **kwargs):
        table = Table.from_file(*args, **kwargs)
        return cls.convert_from_data_table(table)

    @classmethod
    def from_url(cls, *args, **kwargs):
        table = Table.from_url(*args, **kwargs)
        return cls.convert_from_data_table(table)

    @classmethod
    def make_timeseries_from_sequence(cls, table, delta=None, start=None,
                                      name="T", have_date=True, have_time=True):
        from orangecontrib.timeseries import fromtimestamp, timestamp

        domain = table.domain
        if delta is None:
            # timeseries default to sequential ordering
            return super(Timeseries, cls).from_table(domain, table)
        if start is None:
            start = fromtimestamp(0)
        n = len(table)
        time_col = np.empty((n, 1), dtype=float)
        for i, _ in enumerate(time_col):
            time_col[i] = timestamp(start + i * delta)
        t_attr = TimeVariable(
            get_unique_names(domain, name),
            have_date=have_date, have_time=have_time)
        x = np.hstack((time_col, table.X))
        ts = super(Timeseries, cls).from_numpy(
            Domain((t_attr, ) + domain.attributes, domain.class_vars, domain.metas),
            x, table.Y, table.metas, ids=table.ids
        )
        ts.time_variable = t_attr
        return ts

    @classmethod
    def make_timeseries_from_continuous_var(cls, table, attr):
        # Make a sequence attribute from one of the existing attributes,
        # and sort all values according to it
        time_var = table.domain[attr]
        values = table.get_column(time_var)
        # Filter out NaNs
        nans = np.isnan(values)
        if nans.all():
            return None
        if nans.any():
            values = values[~nans]
            table = table[~nans]
        # Sort!
        ordered = np.argsort(values)
        if (ordered != np.arange(len(ordered))).any():
            table = table[ordered]

        ts = super(Timeseries, cls).from_table(table.domain, table)
        ts.time_variable = time_var
        return ts

    @property
    def time_values(self):
        """Time series measurements times"""
        if self.time_variable is None:
            return np.arange(len(self))
        else:
            return self.get_column(self.time_variable)

    @property
    def time_variable(self):
        """The :class:`TimeVariable` or :class:`ContinuousVariable` that
        represents the time variable in the time series"""
        return self.attributes.get('time_variable')

    @time_variable.setter
    def time_variable(self, var):
        if var is None:
            self.attributes = self.attributes.copy()
            if 'time_variable' in self.attributes:
                self.attributes.pop('time_variable')
            self.time_delta = None
            return

        assert var in self.domain
        self.attributes = self.attributes.copy()
        self.attributes['time_variable'] = var

        self.time_delta = TimeDelta(self.time_values)

    def set_interpolation(self, method='linear', multivariate=False):
        self._interp_method = method
        self._interp_multivariate = multivariate

    def interp(self, attrs=None):
        """Return values of variables in attrs, interpolated by method set
        with set_interpolated().

        Parameters
        ----------
        attrs : str or list or None
            Variable or List of variables to interpolate. If None, the
            whole table is returned interpolated.

        Returns
        -------
        X : array (n_inst x n_attrs) or Timeseries
            Interpolated variables attrs in columns.
        """
        from orangecontrib.timeseries import interpolate_timeseries
        # FIXME: This interpolates the whole table, might be an overhead
        # if only a single attr is required
        interpolated = interpolate_timeseries(self,
                                              self._interp_method,
                                              self._interp_multivariate)
        if attrs is None:
            return interpolated
        if isinstance(attrs, str):
            attrs = [attrs]
        return Table.from_table(Domain([], [], attrs, interpolated.domain), interpolated).metas
class NotFittedError(ValueError, AttributeError):
    """Raised when model predictions made without fitting"""
class _BaseModel:
    REQUIRES_STATIONARY = True
    SUPPORTS_VECTOR = False

    _NOT_FITTED = NotFittedError('Model must be fitted first (see fit() method)')

    __wrapped__ = None

    def __init__(self):
        self.model = None
        self.results = None
        self.order = ()
        self._model_kwargs = dict(missing='raise')
        self._fit_kwargs = dict()
        self._endog = None

        self._table_var_names = None
        self._table_name = None
        self._table_timevar = None
        self._table_timevals = None

    def _before_init(self, endog, exog):
        """
        This method is called before the statsmodels model is init. It can
        last-minute transform the endog and exog variables, or it can set
        constructor parameters depending on their values.
        """
        return endog, exog

    def _before_fit(self, endog, exog):
        """
        This method is called before fit() with the same parameters. It
        can be used to set last-minute, endog or exog-dependent parameters.
        Override it if you need it.
        """

    def _fittedvalues(self):
        """
        This was needed to override for ARIMA as its fittedvalues returned
        unintegraded series instead.
        """
        return self.results.fittedvalues

    def fittedvalues(self, as_table=False):
        """
        Return predictions for in-sample observations, i.e. the model's
        approximations of the original training values.

        Parameters
        ----------
        as_table : bool
            If True, return results as an Orange.data.Table.

        Returns
        -------
        fitted_values : array_like
        """
        if self.results is None:
            raise self._NOT_FITTED
        values = self._fittedvalues()
        if as_table:
            values = self._as_table(values, 'fitted')
        return values

    def _as_table(self, values, what):
        """Used for residuals() and fittedvalues() methods."""
        from Orange.data import Domain, ContinuousVariable
        attrs = []
        n_vars = values.shape[1] if values.ndim == 2 else 1
        if n_vars == 1:
            values = np.atleast_2d(values).T
        tvar = None
        # If 1d, time var likely not already present, so lets add it if possible
        if n_vars == 1 and self._table_timevar:
            values = np.column_stack((self._table_timevals[-values.shape[0]:],
                                      values))
            tvar = self._table_timevar
            attrs.append(tvar)
        for i, name in zip(range(n_vars),
                           self._table_var_names or range(n_vars)):
            attrs.append(ContinuousVariable('{} ({})'.format(name, what)))

            # Make the fitted time variable time variable
            if self._table_timevar and self._table_timevar.name == name:
                tvar = attrs[-1]

        table = Timeseries.from_numpy(Domain(attrs), values)
        table.time_variable = tvar
        table.name = (self._table_name or '') + '({} {})'.format(self, what)
        return table

    def residuals(self, as_table=True):
        """
        Return residuals (prediction errors) for in-sample observations,

        Parameters
        ----------
        as_table : bool
            If True, return results as an Orange.data.Table.

        Returns
        -------
        residuals : array_like
        """
        if self.results is None:
            raise self._NOT_FITTED
        resid = self.results.resid
        if as_table:
            resid = self._as_table(resid, 'residuals')
        return resid

    def _predict(self, steps, exog, alpha):
        """
        Return forecast predictions (along with confidence intervals)
        for steps ahead given exog values (or None if not needed).
        """
        raise NotImplementedError

    def _orange_arrays(self, table):
        self._table_var_names = [v.name for v in chain(table.domain.class_vars,
                                                       table.domain.attributes)]
        self._table_name = table.name
        if getattr(table, 'time_variable', None):
            self._table_timevar = table.time_variable
            self._table_timevals = table.time_values
        y = table.Y.ravel()
        X = table.X
        if y.size:
            defined_range = (np.arange(1, len(y) + 1) * ~np.isnan(y)).max()
            y = y[:defined_range]
            X = X[:defined_range]
        return y, X

    def fit(self, endog, exog=None):
        """
        Fit the model to endogenous variable endog, optionally given
        exogenous column variables exog.

        Parameters
        ----------
        endog : array_like
            Dependent variable (y) of shape ``[nobs, k]``
            (``k = 1`` for a single variable; ``k > 1`` for vector models).
        exog : array_like
            If model supports it, the additional independent variables (X) of
            shape ``[nobs, k_vars]``.

        Returns
        -------
        fitted_model
        """
        if isinstance(endog, Table):
            assert exog is None
            endog, exog = self._orange_arrays(endog)

        if not endog.size:
            if not exog.size:
                raise ValueError('Input series are empty. Nothing to learn.')
            endog, exog = exog, None

        endog, exog = self._before_init(endog, exog)
        self._endog = endog
        kwargs = self._model_kwargs.copy()
        kwargs.update(endog=endog)
        if exog is not None:
            kwargs.update(exog=exog)
        model = self.model = self.__wrapped__(**kwargs)

        self._before_fit(endog, exog)
        kwargs = self._fit_kwargs.copy()
        self.results = model.fit(**kwargs)
        return self

    def errors(self):
        """Return dict of RMSE/MAE/MAPE/POCID/R² errors on in-sample, fitted values

        Returns
        -------
        errors : dict
            Mapping of error measure str -> error value.
        """
        if self.results is None:
            raise self._NOT_FITTED
        true = self._endog
        pred = self._fittedvalues()
        return dict(r2=r2(true, pred),
                    mae=mae(true, pred),
                    rmse=rmse(true, pred),
                    mape=mape(true, pred),
                    pocid=pocid(true, pred))

    def _predict_as_table(self, prediction, confidence):
        from Orange.data import Domain, ContinuousVariable
        means, lows, highs = [], [], []
        n_vars = prediction.shape[2] if len(prediction.shape) > 2 else 1
        for i, name in zip(range(n_vars),
                           self._table_var_names or range(n_vars)):
            mean = ContinuousVariable('{} (forecast)'.format(name))
            low = ContinuousVariable('{} ({:d}%CI low)'.format(name, confidence))
            high = ContinuousVariable('{} ({:d}%CI high)'.format(name, confidence))
            low.ci_percent = high.ci_percent = confidence
            mean.ci_attrs = (low, high)
            means.append(mean)
            lows.append(low)
            highs.append(high)
        domain = Domain(means + lows + highs)
        X = np.column_stack(prediction)
        table = Timeseries.from_numpy(domain, X)
        table.name = (self._table_name or '') + '({} forecast)'.format(self)
        return table

    def predict(self, steps=1, exog=None, *, alpha=.05, as_table=False):
        """Make the forecast of future values.

        Parameters
        ----------
        steps : int
            The number of steps to make forecast for.
        exog : array_like
            The exogenous variables some models require.
        alpha : float
            Calculate and return (1-alpha)100% confidence intervals.
        as_table : bool
            If True, return results as an Orange.data.Table.

        Returns
        -------
        forecast : array_like
            (forecast, low, high)
        """
        if self.results is None:
            raise self._NOT_FITTED
        prediction = self._predict(steps, exog, alpha)
        if as_table:
            prediction = self._predict_as_table(prediction, int((1 - alpha) * 100))
        return prediction

    def __str__(self):
        return str(self.__wrapped__)

    @property
    def max_order(self):
        return max(self.order, default=0)

    def clear(self):
        """Reset (unfit) the current model"""
        self.model = None
        self.results = None
        self._endog = None
        self._table_var_names = None
        self._table_name = None
        self._table_timevar = None
        self._table_timevals = None

    def copy(self):
        """Copy the current model"""
        from copy import deepcopy
        return deepcopy(self)
class OWBaseModel(widget.OWWidget):
    """Abstract widget representing a time series model"""
    LEARNER = None

    class Inputs:
        time_series = Input("Time series", Table, default=True)

    class Outputs:
        learner = Output("Time series model", _BaseModel)
        forecast = Output("Forecast",  Timeseries)
        fitted_values = Output("Fitted values", Timeseries)
        residuals = Output("Residuals", Timeseries)

    want_main_area = False
    resizing_enabled = False

    autocommit = settings.Setting(True)
    learner_name = settings.Setting('')
    forecast_steps = settings.Setting(3)
    forecast_confint = settings.Setting(95)

    class Error(widget.OWWidget.Error):
        not_continuous = widget.Msg("Time series' target variable should be continuous, " \
                                    "not discrete.")
        no_target = widget.Msg("Input time series doesn't contain a target variable. "\
                               "Edit the domain and make one variable target.")
        model_error = widget.Msg('Error {}: {}: {}')

    def __init__(self):
        super().__init__()
        self.name_lineedit = None
        self.data = None
        self.learner = None
        self.model = None
        self.preprocessors = None
        self.outdated_settings = False
        self.setup_layout()
        QTimer.singleShot(0, self.apply.now)

    def create_learner(self):
        """Creates a learner (cunfit model) with current configuration """
        raise NotImplementedError

    @Inputs.time_series
    def set_data(self, data):
        self.data = data = None if data is None else \
                           Timeseries.from_data_table(data)
        self.update_model()

    @gui.deferred
    def apply(self):
        self.update_learner()
        self.update_model()

    def update_learner(self):
        learner = self.learner = self.create_learner()
        self.name_lineedit.setPlaceholderText(str(self.learner))
        learner.name = self.learner_name or str(learner)
        self.Outputs.learner.send(learner)

    def fit_model(self, model, data):
        return model.fit(data.interp())

    def forecast(self, model):
        return model.predict(self.forecast_steps,
                             alpha=1 - self.forecast_confint / 100,
                             as_table=True)

    def update_model(self):
        forecast = None
        fittedvalues = None
        residuals = None
        self.Error.model_error.clear()
        if self.is_data_valid():
            model = self.learner = self.create_learner()
            model.name = self.learner_name or str(model)
            try:
                is_fit = False
                self.fit_model(model, self.data)
                is_fit = True
                forecast = self.forecast(model)
                forecast.name = f"Forecast ({model.name})"
                fittedvalues = model.fittedvalues(as_table=True)
                fittedvalues.name = f"Fitted values ({model.name})"
                residuals = model.residuals(as_table=True)
                residuals.name = f"Residuals ({model.name})"
            except Exception as ex:
                action = 'forecasting' if is_fit else 'fitting model'
                self.Error.model_error(action, ex.__class__.__name__,
                                       ex.args[0] if ex.args else '')
        self.Outputs.forecast.send(forecast)
        self.Outputs.fitted_values.send(fittedvalues)
        self.Outputs.residuals.send(residuals)

    def is_data_valid(self):
        data = self.data
        if data is None:
            return False
        self.Error.clear()
        if not data.domain.class_var:
            self.Error.no_target()
            return False
        if not data.domain.class_var.is_continuous:
            self.Error.not_continuous()
            return False
        return True

    def send_report(self):
        name = self.learner_name or str(self.learner if self.learner else '')
        if name:
            self.report_items((("Name", name),))
        if str(self.learner) != name:
            self.report_items((("Model type", str(self.learner)),))
        self.report_items((("Forecast steps", self.forecast_steps),
                           ("Confidence interval", self.forecast_confint),))
        if self.data is not None:
            self.report_data("Time series", self.data)

    # GUI
    def setup_layout(self):
        self.add_learner_name_widget()
        self.add_main_layout()
        self.add_bottom_buttons()

    def add_main_layout(self):
        """Creates layout with the learner configuration widgets.

        Override this method for laying out any learner-specific parameter controls.
        See setup_layout() method for execution order.
        """
        raise NotImplementedError

    def add_learner_name_widget(self):
        self.name_lineedit = gui.lineEdit(
            self.controlArea, self, 'learner_name', box='Name',
            tooltip='The name will identify this model in other widgets')

    def add_bottom_buttons(self):
        layout = QFormLayout()
        gui.widgetBox(self.controlArea, 'Forecast', orientation=layout)
        layout.addRow('Forecast steps ahead:',
                      gui.spin(None, self, 'forecast_steps', 1, 100,
                               alignment=Qt.AlignRight,
                               controlWidth=50, callback=self.apply.deferred))
        layout.addRow('Confidence intervals:',
                      gui.hSlider(None, self, 'forecast_confint', None, 1, 99,
                      callback=self.apply.deferred))
        gui.auto_commit(self.controlArea, self, 'autocommit', "&Apply",
                        commit=self.apply)


class ARIMA(_BaseModel):
    """Autoregressive integrated moving average (ARIMA) model

    An auto regression (AR) and moving average (MA) model with differencing.

    If exogenous variables are provided in fit() method, this becomes an
    ARIMAX model.

    Parameters
    ----------
    order : tuple (p, d, q)
        Tuple of three non-negative integers: (p) the AR order, (d) the
        degree of differencing, and (q) the order of MA model.
        If d = 0, this becomes an ARMA model.

    Returns
    -------
    unfitted_model
    """
    REQUIRES_STATIONARY = False
#    __wrapped__ = statsmodels.tsa.arima.model.ARIMA
    __wrapped__ = sm.tsa.arima.ARIMA

    def __init__(self, order=(1, 0, 0),seasonal_order=(0,0,0,0), use_exog=False):
        super().__init__()
        self.order = order
        self.seasonal_order = seasonal_order
        self.use_exog = use_exog
        self._model_kwargs.update(order=order,seasonal_order = seasonal_order)

    def __str__(self):
        return '{}({})'.format('{}AR{}MA{}'.format('S' if self.seasonal_order[1] else '',
                                                 'I' if self.order[1] else '',
                                                 'X' if self.use_exog else ''),
                               ','.join(map(str, self.order)))

    def _predict(self, steps, exog, alpha):
        pred_res = self.results.get_forecast(steps, exog=exog)
        forecast = pred_res.predicted_mean
        confint = pred_res.conf_int(alpha=alpha)
        return np.c_[forecast, confint].T

    def _before_init(self, endog, exog):
        exog = exog if self.use_exog else None
        if len(endog) == 0:
            raise ValueError('Need an endogenous (target) variable to fit')
        return endog, exog

    def _fittedvalues(self):
        # Statsmodels supports different args whether series is
        # differentiated (order has d) or not. -- stupid statsmodels
        kwargs = dict(typ='levels') if self.order[1] > 0 else {}
        return self.results.predict(**kwargs)

class OWSARIMAModel(OWBaseModel):
    name = 'SARIMA Model'
    description = 'Model the time series using ARMA, ARIMA, or SARIMA.'
    icon = 'icons/ARIMA.svg'
    priority = 210

    p = settings.Setting(1)
    d = settings.Setting(0)
    q = settings.Setting(0)
    s_p = settings.Setting(0)
    s_d = settings.Setting(0)
    s_q = settings.Setting(0)
    s_s = settings.Setting(0)

    class Inputs(OWBaseModel.Inputs):
        exogenous_data = Input("Exogenous data", Timeseries)

    def __init__(self):
        super().__init__()
        self.exog_data = None

    @Inputs.exogenous_data
    def set_exog_data(self, data):
        self.exog_data = data
        self.update_model()

    def add_main_layout(self):
        layout = QFormLayout()
        self.controlArea.layout().addLayout(layout)
        kwargs = dict(controlWidth=50, alignment=Qt.AlignRight,
                      callback=self.apply.deferred)
        layout.addRow('Auto-regression order (p):',
                      gui.spin(None, self, 'p', 0, 100, **kwargs))
        layout.addRow('Differencing degree (d):',
                      gui.spin(None, self, 'd', 0, 2, **kwargs))
        layout.addRow('Moving average order (q):',
                      gui.spin(None, self, 'q', 0, 100, **kwargs))
        layout.addRow('Seasonal Auto-regression order (P):',
                      gui.spin(None, self, 's_p', 0, 100, **kwargs))
        layout.addRow('Seasonal Differencing degree (D):',
                      gui.spin(None, self, 's_d', 0, 2, **kwargs))
        layout.addRow('Seasonal Moving average order (Q):',
                      gui.spin(None, self, 's_q', 0, 100, **kwargs))
        layout.addRow('Seasonality order (s):',
                      gui.spin(None, self, 's_s', 0, 100, **kwargs))


    def forecast(self, model):
        return model.predict(self.forecast_steps,
                             exog=self.exog_data,
                             alpha=1 - self.forecast_confint / 100,
                             as_table=True)

    def create_learner(self):
        return ARIMA((self.p, self.d, self.q),(self.s_p,self.s_d,self.s_q,self.s_s), self.exog_data is not None)


if __name__ == "__main__":
    data = TS.from_file('airpassengers')
    domain = Domain(data.domain.attributes[:-1], data.domain.attributes[-1])
    data = Timeseries.from_numpy(domain, data.X[:, :-1], data.X[:, -1])
    WidgetPreview(OWSARIMAModel).run(data)
