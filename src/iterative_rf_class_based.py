import pandas as pd
from sklearn.metrics import confusion_matrix
import numpy as np
from sklearn.base import BaseEstimator
from sklearn.ensemble import RandomForestClassifier


class IterativeRFClassBased(BaseEstimator):
    def __init__(
            self,
            *,
            iter_count=2,
            n_estimators=2,
            max_depth=None,
    ):

        self.iter_count = 2
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self._fitted_estimator = None

    def _get_estimator(self, weights):
        return RandomForestClassifier(
            n_estimators=self.n_estimators,
            max_depth=self.max_depth,
            n_jobs=8,
            class_weight=weights
        )

    def _get_accuracy_per_class(self, y, y_pred):
        c_matrix = confusion_matrix(y, y_pred)
        return c_matrix.diagonal() / c_matrix.sum(axis=1)

    def _get_weights(self, class_accuracies, y):
        unique_classes = np.unique(y)
        weights = {}
        for class_idx, class_accuracy in enumerate(class_accuracies):
            weights[unique_classes[class_idx]] = 1 - class_accuracy
        return weights

    def _get_initial_weights(self, y):
        unique_classes = np.unique(y)
        weights = {}
        for class_name in unique_classes:
            weights[class_name] = 1
        return weights

    def fit(self, X, y):
        weights = self._get_initial_weights(y)

        for iteration_idx in range(self.iter_count):
            estimator = self._get_estimator(weights)
            estimator.fit(X, y)
            y_pred = estimator.predict(X)
            class_accuracies = self._get_accuracy_per_class(y, y_pred)
            weights = self._get_weights(class_accuracies, y)
        self._fitted_estimator = estimator

    def predict(self, X):
        return self._fitted_estimator.predict(X)

    def decision_function(self, X):
        # called for roc_auc_score
        raise NotImplementedError("This IterativeRandomForrest instance is not fitted yet")

    def predict_proba(self, X):
        # called for roc_auc_score
        raise NotImplementedError("This IterativeRandomForrest instance is not fitted yet")
