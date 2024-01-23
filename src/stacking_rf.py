from sklearn.ensemble import StackingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier


class StackingRFClassifier(StackingClassifier):
    def __init__(
            self,
            estimators=None,
            final_estimator=None,
            *,
            cv=None,
            stack_method="auto",
            n_jobs=None,
            passthrough=False,
            verbose=0,
    ):
        super().__init__(
            estimators=estimators or [
                ("nb", GaussianNB()),
                ("tree", DecisionTreeClassifier()),
                ("rf", RandomForestClassifier()),
                ("knn", KNeighborsClassifier()),
                ("svm", LinearSVC()),
                ("lr", LogisticRegression())
            ],
            final_estimator=final_estimator,
            cv=cv,
            stack_method=stack_method,
            n_jobs=n_jobs,
            passthrough=passthrough,
            verbose=verbose,
        )
