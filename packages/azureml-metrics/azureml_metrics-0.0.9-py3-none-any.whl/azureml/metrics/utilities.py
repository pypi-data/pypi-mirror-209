# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Utilities for computing model evaluation metrics."""
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
import pandas as pd
import logging

from azureml.metrics import constants
from azureml.metrics.exceptions import ClientException


logger = logging.getLogger(__name__)


def get_metric_task(metric: str) -> str:
    """
    Get the task for a given metric.

    :param metric: The metric to lookup.
    :return: The task type for the given metric.
    """
    if metric in constants.CLASSIFICATION_SET:
        return constants.CLASSIFICATION
    elif metric in constants.REGRESSION_SET:
        return constants.REGRESSION
    safe_message = "Metric {} not found".format(metric)
    raise ClientException(safe_message, target="metric_name", reference_code="utilities.get_metric_task",
                          safe_message=safe_message)


def minimize_or_maximize(metric: str,
                         task: Optional[str] = None) -> str:
    """
    Select the objective given a metric.

    Some metrics should be minimized and some should be maximized
    :param metric: the name of the metric to look up
    :return: returns one of constants.OptimizerObjectives.
    """
    if task is None:
        task = get_metric_task(metric)
    return constants.OBJECTIVES_TASK_MAP[task][metric]


def is_better(val1: float,
              val2: float,
              metric: Optional[str] = None,
              objective: Optional[str] = None) -> bool:
    """Select the best of two values given metric or objectives.

    :param val1: scalar value
    :param val2: scalar value
    :param metric: the name of the metric to look up
    :param objective: one of constants.OptimizerObjectives.
    :return: returns a boolean of if val1 is better than val2 in the situation
    """
    if objective is None:
        if metric is None:
            safe_message = "Must specific either metric or objective"
            raise ClientException(safe_message, target="metric_name", reference_code="utilities.is_better",
                                  safe_message=safe_message)
        else:
            objective = minimize_or_maximize(metric)
    if objective == constants.MAXIMIZE:
        return val1 > val2
    elif objective == constants.MINIMIZE:
        return val1 < val2
    return False


def get_all_nan(task: str) -> Dict[str, float]:
    """Create a dictionary of metrics to values for the given task.

    All metric values are set to nan initially
    :param task: one of constants.Tasks.
    :return: returns a dictionary of nans for each metric for the task.
    """
    return {m: np.nan for m in constants.METRICS_TASK_MAP[task]}


def get_metric_ranges(task: str) -> Tuple[Dict[str, float], Dict[str, float]]:
    """Get the metric range for the task.

    :param task: Machine learning task.
    :return: Tuple with dictionaries of minimum and maximum scores.
    """
    minimums = get_min_values(task)
    maximums = get_max_values(task)
    return minimums, maximums


def get_worst_values(task: str) -> Dict[str, float]:
    """
    Get the worst possible scores for metrics of the task.

    :param task: Machine learning task.
    :return: Dictionary from metric names to the worst scores.
    """
    minimums, maximums = get_metric_ranges(task)
    task_objectives = constants.OBJECTIVES_TASK_MAP[task]

    worst_scores = dict()
    for metric_name, objective in task_objectives.items():
        if metric_name == constants.TRAIN_TIME:
            worst_scores[metric_name] = constants.SCORE_UPPER_BOUND
            continue

        if objective == constants.MAXIMIZE:
            worst_scores[metric_name] = minimums[metric_name]
        else:
            worst_scores[metric_name] = maximums[metric_name]
    return worst_scores


def get_min_values(task: str) -> Dict[str, float]:
    """Get the minimum values for metrics for the task.

    :param task: string "classification" or "regression"
    :return: returns a dictionary of metrics with the min values.
    """
    task_ranges = constants.RANGES_TASK_MAP[task]  # type: Dict[str, Tuple[float, float]]
    return {metric_name: lower for metric_name, (lower, _) in task_ranges.items()}


def get_max_values(task: str) -> Dict[str, float]:
    """
    Get the maximum scores for metrics of the task.

    :param task: Machine learning task.
    :return: Dictionary of metrics with the maximum scores.
    """
    task_ranges = constants.RANGES_TASK_MAP[task]  # type: Dict[str, Tuple[float, float]]
    return {metric_name: upper for metric_name, (_, upper) in task_ranges.items()}


def assert_metrics_sane(scores: Dict[str, Any], task: str) -> None:
    """
    Assert that the given scores are within the valid range.

    This only checks the lower bound (upper for minimizing metrics).

    :param scores: Dictionary from metric name to metric score.
    :param task: Task name.
    """
    worst_scores = get_worst_values(task)
    objectives = constants.OBJECTIVES_TASK_MAP[task]
    for metric_name, score in scores.items():
        if not np.isscalar(score) or np.isnan(score):
            continue

        worst_value = worst_scores[metric_name]
        if objectives[metric_name] == constants.MAXIMIZE:
            if score < worst_value:
                message = "Score out of bounds for maximizing metric {}: {} < {}".format(
                    metric_name, score, worst_value)
                safe_message = "Score out of bounds for maximizing metric"
                raise ClientException(message, target="task", reference_code="utilities.assert_metrics_sane",
                                      safe_message=safe_message)

        elif objectives[metric_name] == constants.MINIMIZE:
            if score > worst_value:
                message = "Score out of bounds for minimizing metric {}: {} > {}".format(
                    metric_name, score, worst_value)
                safe_message = "Score out of bounds for minimizing metric"
                raise ClientException(message, target="task", reference_code="utilities.assert_metrics_sane",
                                      safe_message=safe_message)

        else:
            safe_message = "Cannot validate metric bounds for metrics that are not minimizing or maximizing"
            raise ClientException(safe_message, target="metric_name", reference_code="utilities.assert_metrics_sane",
                                  safe_message=safe_message)


def get_scalar_metrics(task: str) -> List[str]:
    """Get the scalar metrics supported for a given task.

    :param task: Task string, (e.g. "classification" or "regression")
    :return: List of the default metrics supported for the task
    """
    return {
        constants.CLASSIFICATION: list(constants.CLASSIFICATION_SCALAR_SET),
        constants.REGRESSION: list(constants.REGRESSION_SCALAR_SET),
    }[task]


def get_default_metrics(task: str) -> List[str]:
    """Get the metrics supported for a given task as a set.

    :param task: Task string, (e.g. "classification" or "regression")
    :return: List of the default metrics supported for the task
    """
    return {
        constants.CLASSIFICATION: list(constants.CLASSIFICATION_SET
                                       - constants.UNSUPPORTED_CLASSIFICATION_TABULAR_SET),
        constants.REGRESSION: list(constants.REGRESSION_SET),
    }[task]


def is_scalar(metric_name: str) -> bool:
    """
    Check whether a given metric is scalar or nonscalar.

    :param metric_name: the name of the metric found in constants.py
    :return: boolean for if the metric is scalar
    """
    if metric_name.endswith(constants.MetricExtrasConstants.MetricExtrasSuffix):
        metric_name = metric_name[:-len(constants.MetricExtrasConstants.MetricExtrasSuffix)]
    if metric_name in constants.FULL_SCALAR_SET or \
            metric_name in constants.CLASSIFICATION_MULTILABEL_SET or \
            metric_name in constants.Metric.SCALAR_SEQ2SEQ_SET:
        return True
    elif metric_name in constants.FULL_NONSCALAR_SET:
        return False
    elif metric_name in constants.FULL_CLASSWISE_SET:
        return False
    safe_message = "{} metric is not supported".format(metric_name)
    raise ClientException(safe_message, target="metric_name", reference_code="utilities.is_scalar",
                          safe_message=safe_message)


def is_classwise(metric_name: str) -> bool:
    """
    Check whether a given metric is a classwise metric.

    :param metric_name: the name of the metric found in constants.py
    :return: boolean for if the metric is scalar
    """
    if metric_name in constants.FULL_CLASSWISE_SET:
        return True
    else:
        return False
    safe_message = "{} metric is not supported".format(metric_name)
    raise ClientException(safe_message, target="metric_name", reference_code="utilities.is_classwise",
                          safe_message=safe_message)


def segregate_scalar_non_scalar(metrics: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    metrics_result: Dict[str, Dict[str, Any]] = {
        constants.Metric.Metrics: dict(),
        constants.Metric.Artifacts: dict()
    }
    for metric_name, metric_value in metrics.items():
        if is_scalar(metric_name):
            metrics_result[constants.Metric.Metrics][metric_name] = metric_value
        else:
            metrics_result[constants.Metric.Artifacts][metric_name] = metric_value
    return metrics_result


def amalgamate_scalar_non_scalar(metrics: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    if constants.Metric.Metrics in metrics and constants.Metric.Artifacts in metrics:
        return {**metrics[constants.Metric.Metrics], **metrics[constants.Metric.Artifacts]}
    return {}


def check_and_convert_to_np(arr: Optional[Union[np.ndarray, pd.DataFrame, List]]):
    if arr is not None:
        if isinstance(arr, pd.DataFrame):
            if len(arr.columns) == 1:
                return arr.iloc[:, 0].to_numpy()
            else:
                return arr.to_numpy()

        elif isinstance(arr, pd.Series):
            return arr.to_numpy()

        elif isinstance(arr, List):
            return np.array(arr)
    return arr


def check_for_different_dtype(y_test: Optional[Union[np.ndarray, pd.DataFrame, List]],
                              y_pred: Optional[Union[np.ndarray, pd.DataFrame, List]]):
    """validates y_test and y_pred datatype and returns True if they are different"""
    y_test = check_and_convert_to_np(y_test)
    y_pred = check_and_convert_to_np(y_pred)

    if ((isinstance(y_test, np.ndarray) and len(y_test) >= 1)
            and (isinstance(y_pred, np.ndarray) and len(y_pred) >= 1)):

        y_test_dtype = check_homogeneous_type(y_test)
        y_pred_dtype = check_homogeneous_type(y_pred)

        if y_test_dtype is False or y_pred_dtype is False:
            raise Exception("y_test or y_pred are having mix of labels with different datatype.")

        elif y_test_dtype != y_pred_dtype and y_pred.ndim == 1:
            return True

    return False


def convert_to_same_dtype(y_test: Optional[Union[np.ndarray, pd.DataFrame, List]],
                          y_pred: Optional[Union[np.ndarray, pd.DataFrame, List]],
                          class_labels: Optional[Union[np.ndarray, List]],
                          train_labels: Optional[Union[np.ndarray, List]]):
    """converts y_test, y_pred, class_labels, train_labels to same dtype."""
    y_test = np.array([str(label) for label in y_test])
    y_pred = np.array([str(label) for label in y_pred])

    class_labels = np.array([str(label) for label in class_labels]) \
        if class_labels is not None else None
    train_labels = np.array([str(label) for label in train_labels]) \
        if train_labels is not None else None

    logger.warning("Warning: y_test and y_pred have different datatypes,"
                   + "converting both of them to string type.")

    return y_test, y_pred, class_labels, train_labels


def check_homogeneous_type(arr):
    """checks if all the values in the array of same datatype."""
    value = iter(arr)
    first_data_type = type(next(value))
    return first_data_type if all((type(x) is first_data_type) for x in value) else False


def flatten_array_and_remove_duplicates(arr):
    """flattens the array to return individual elements without duplicates."""
    arr = np.array(arr).flatten()

    values_list = []

    for row in arr:
        if isinstance(row, np.ndarray) or isinstance(row, list):
            for value in row:
                if value is not None:
                    values_list.append(value)
        elif row is not None:
            values_list.append(row)

    values = set(values_list)
    return values
