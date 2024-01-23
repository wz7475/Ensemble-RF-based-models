
#### legened
**#num experiment**

**model num**

*ModelLibraryName*

#### content

- [ ]  Classic RF **model A** -> *RandomForrrestClassifier*

- [ ] Boosted RF -> 
- *AdaBoostClassifer* **model B**
	- estimator - *DecisionTreeClassifier* 
	- max_depth  - *max_depth*
	- reset weight - *estimator_weights*
- **#1 check impact of depth of accuracy**
	- check assumption about **week classifier** to boosting methods - referring to publication Introduction to boositng
	- motivation - **lower bias** - base aim of boositng
- **#0 compare to classic RF**

- [ ] Stacked RF
- *StackingClassifier* **model C**
	- with estimators as
		- multiplies instances of *RandomForrestClassifier*
		- *RadomForrestClassifer* + a few diffrent classifiers
	- final estimator as *RadomForrestClassifer*
- **#2 check if variety of stacked estimators is important** (what with boring layer consisting only with RFs) -  referring to publication Stacked Generalization
- **#0 compare to classic RF**

*optional*
- [ ] Iterative (initially stacked) RF
- *own implementation of framework for iterations* **model D**
	- *RadomForrestClassifer* as base model (one per layer)
- **#3 compare depth**
- motivation - improve accuracy by learning errors of predecesor
- **#0 compare to classic RF**

#### conclusions
**Boosted RF**
- high risk of overfitting
- RF has advantage over Boosted RF by using bagging

**Iterative RF**
- underrepresentation of correct predictions

**Stacked RF**
- need for diversity of estimatorty in layer 1 (not only RFs)
- again overfitting
