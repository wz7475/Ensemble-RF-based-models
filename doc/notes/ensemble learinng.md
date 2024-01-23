*src*
https://www.analyticsvidhya.com/blog/2023/01/ensemble-learning-methods-bagging-boosting-and-stacking/
#### ensemble learninig
*def*
**Ensemble learning** is a machine learning technique combining multiple individual models to create a stronger, more accurate predictive model

**weak model** - has high bias or high variance

techniques
- bagging
- boosting
- stacking

#### sequential vs parrarel
Ensemble Methods can also be divided into two groups:
- **Sequential Learners**, where different models are generated sequentially and the mistakes of previous models are learned by their successors. This aims at exploiting the dependency between models by giving the mislabeled examples higher weights (_e.g. AdaBoost_).
- **Parallel Learners**, where base models are generated in parallel. This exploits the independence between models by averaging out the mistakes (_e.g. [Random Forest](https://blog.paperspace.com/random-forests/)_).

#### bagging
*def*
aims to produce a model with lower **variance** than the individual weak models

*aka*
bootstrap aggreagating

**bootstrapping**
resample subsets of data with replacement for weak learners

**aggreagating**
weak learners are trained independently and their predictions are aggregated *(max voting or averging)*

![[Pasted image 20231125123302.png|500]]

#### boosting
*def*
aims to produce a model with a lower **bias** than that of the individual models

*method*
- each subsequent learner improves the errors of previous learners in the sequence
- aggregates the results at each step.
- final model uses **weighted voting** eg via their accuracy

![[Pasted image 20231125124241.png|500]]
1. We **sample m-number of subsets** from an initial training dataset.
2. Using the first subset, we train the first weak learner.
3. We test the trained weak learner using the training data. As a result of the testing, some data points will be incorrectly predicted.
4. Each **data point with the wrong prediction is sent into the second subset of data**, and this subset is updated.
5. Using this **updated subset, we train and test the second weak learner**.
6. We continue with the following subset until the total number of subsets is reached.
7. We now have the total prediction. The overall prediction has already been aggregated at each step, so there is no need to calculate it.


#### stacking
*aim*
create a single robust model from multiple heterogeneous strong learners

*method*
- combine learners which are
	- strong
	- heterogeneous
- create meta-model

![[Pasted image 20231125130003.png|500]]


#### comparison
![[Pasted image 20231125130050.png|500]]