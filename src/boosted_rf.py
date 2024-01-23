import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier


class BoostedRFClassifier(AdaBoostClassifier):
    def __init__(
            self,
            *,
            estimator=DecisionTreeClassifier(),
            n_estimators=50,
            learning_rate=1.0,
            random_state=None,
            algorithm='SAMME',
            _disable_weights=True,
    ):
        super().__init__(
            estimator=estimator,
            n_estimators=n_estimators,
            learning_rate=learning_rate,
            random_state=random_state,
            algorithm=algorithm,
        )

        self._disable_weights = _disable_weights
        self._estimator_weights = np.zeros(self.n_estimators, dtype=np.float64)

    @property
    def estimator_weights_(self):
        return np.ones(self.n_estimators, dtype=np.float64) if self._disable_weights else self._estimator_weights

    @estimator_weights_.setter
    def estimator_weights_(self, v):
        if not self._disable_weights:
            self._estimator_weights = v
