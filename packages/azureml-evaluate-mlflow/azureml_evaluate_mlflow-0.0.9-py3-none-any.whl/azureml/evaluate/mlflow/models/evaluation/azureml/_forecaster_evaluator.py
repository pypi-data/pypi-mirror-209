# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from azureml.evaluate.mlflow.aml import AzureMLInput,\
    AMLForecastModel
from azureml.evaluate.mlflow.models.evaluation.azureml._task_evaluator import TaskEvaluator

from azureml.evaluate.mlflow.constants import ForecastColumns, ForecastFlavors
from azureml.evaluate.mlflow.exceptions import AzureMLMLFlowException
from azureml.metrics import compute_metrics, constants


class ForecasterEvaluator(TaskEvaluator):
    def evaluate(self,
                 model: AMLForecastModel,
                 X_test: AzureMLInput,
                 y_test: AzureMLInput,
                 **kwargs):
        if not isinstance(model, AMLForecastModel):
            raise AMLForecastModel("Model should be of type AMLForecastModel")

        # In the forecast data we are not guaranteed to have the same
        # dimension of output data as the input so we have to preaggregate
        # the data here.
        if 'X_train' in kwargs and 'y_train' in kwargs:
            kwargs['X_train'], kwargs['y_train'] = model._model_impl.preaggregate_data_set(
                kwargs['X_train'], kwargs['y_train'])
        # Forecasting task has several flavors: forecast, forecast_quantiles and rolling_forecast
        forecast_flavor = kwargs.get(ForecastFlavors.FLAVOUR, ForecastFlavors.RECURSIVE_FORECAST)
        if forecast_flavor not in ForecastFlavors.ALL:
            raise AzureMLMLFlowException(
                f"The {forecast_flavor} is not supported, supported forecast modes are {ForecastFlavors.ALL}")
        if forecast_flavor == ForecastFlavors.RECURSIVE_FORECAST:
            y_pred, _ = model.forecast(X_test)
            X_test, y_test = model._model_impl.preaggregate_data_set(X_test, y_test)
        else:
            step = kwargs.get('step', 1)
            X_test = model.rolling_forecast(X_test, y_test, step=step)
            y_pred = X_test.pop(model._model_impl.forecast_column_name).values
            y_test = X_test.pop(model._model_impl.actual_column_name).values

        # Take forecasting-specific parameters from the model.
        kwargs["time_series_id_column_names"] = model._model_impl.grain_column_names
        kwargs["time_column_name"] = model._model_impl.time_column_name
        metrics = compute_metrics(
            task_type=constants.Tasks.FORECASTING,
            y_test=y_test,
            y_pred=y_pred,
            X_test=X_test,
            **kwargs
        )
        X_test[ForecastColumns._ACTUAL_COLUMN_NAME] = y_test
        X_test[ForecastColumns._FORECAST_COLUMN_NAME] = y_pred

        return metrics, X_test
