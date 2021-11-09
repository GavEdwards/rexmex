import pandas as pd
from typing import List, Dict
from abc import ABC, abstractmethod
from sklearn.metrics  import roc_auc_score, f1_score

class MetricSet(ABC):
    """
    """
    @abstractmethod
    def setup_basic_metrics(self):
        pass

    def _get_metrics(self, filter: List[str]=None) -> Dict:
        if filter is None:
            selected_metrics = self._metrics
        else:
            selected_metrics = {name: metric for name, metric in self._metrics.items()}
        return selected_metrics

    #def add_new_metrics(self, metrics: List[Tuple]):
    #    self._metrics = self._metrics + metrics
    #    return self._metrics
    def reset_metrics(self):
        self._metrics = {}
    
    def get_performance_metrics(self, y_true, y_score, filter: List[str]=None) -> pd.DataFrame:
        selected_metrics = self._get_metrics(filter)
        performance_metrics = {name: [metric(y_true, y_score)] for name, metric in selected_metrics.items()}
        performance_metrics = pd.DataFrame.from_dict(performance_metrics)
        return performance_metrics

class ClassificationMetricSet(MetricSet):
    """
    """
    def __init__(self, cutoff: float=0.5):
        self.cutoff = cutoff
        self._metrics = {}

    def setup_basic_metrics(self):
        self._metrics["roc_auc"] = roc_auc_score
        self._metrics["f1_score"] = roc_auc_score


class RankingMetricSet(MetricSet):
    

    def __init__(self):
        self._metrics = {}

    def setup_basic_metrics(self):
        pass


class RatingMetricSet(MetricSet):
    def __init__(self):
        self._metrics = {}

    def setup_basic_metrics(self):
        pass


class CoverageMetricSet(MetricSet):
    def __init__(self):
        self._metrics = {}

    def setup_basic_metrics(self):
        pass
