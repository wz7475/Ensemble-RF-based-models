from sklearn.model_selection import cross_validate, ShuffleSplit


def evaluate(clf, X, y, scoring=None) -> dict:
    scoring = scoring or ['accuracy', 'precision', 'recall', 'roc_auc', 'f1']

    cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
    _scores = cross_validate(clf, X, y, cv=cv, scoring=scoring, n_jobs=8, return_train_score=True)
    return {name: score.mean() for name, score in _scores.items()}
