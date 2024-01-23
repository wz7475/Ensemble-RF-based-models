import pandas as pd
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
        self.iter_count = iter_count
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self._fitted_estimator = None

    def _get_estimator(self):
        return RandomForestClassifier(
            n_estimators=self.n_estimators,
            max_depth=self.max_depth,
            n_jobs=8
        )

    def fit(self, X, y):
        for iteration_idx in range(self.iter_count):
            estimator = self._get_estimator()
            estimator.fit(X, y)
            y_pred = estimator.predict(X)
            misclassified_samples = np.where(y_pred != y)[0]
            X = pd.concat([X, X.iloc[misclassified_samples]])
            y = np.concatenate([y, y[misclassified_samples]])

        self._fitted_estimator = estimator

    def get_fiited_estimator(self):
        return self._fitted_estimator

    def predict(self, X):
        return self._fitted_estimator.predict(X)

    def decision_function(self, X):
        # called for roc_auc_score
        raise NotImplementedError("This IterativeRandomForrest instance is not fitted yet")

    def predict_proba(self, X):
        # called for roc_auc_score
        raise NotImplementedError("This IterativeRandomForrest instance is not fitted yet")
