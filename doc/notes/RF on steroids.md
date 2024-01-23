#### pure RF
except for feature randomness uses **bagging** (multiple trees and voting) 

#### boosting RF
**on tree level** 
- each new tree learns on subset with enriched with wrongly predicted samples of predecessor
- one iteration on *forest* level

**on forest level**
- treat each forest as learner - train new forest on subset with enriched with wrongly predicted samples of predecessor (RF)
- weighted voting of collection of boosted RFs 
***doubt**: RF is rather strong instead of weak learner

#### stacking RF
*rather **iterative stacking***
1. train initial RF and evaluate
2. prepare new updated dataset
3. train meta-model on updated dataset and evaluate
4. repeat steps 2-3 n times

#### combined methods
- boosting both on tree and forest level
- stacking on tree level boosted RF (one iter. - train single RF with boosting)
- stacking on forest level RFs (one iter  - train multiple boosted RFs) (one iteration in this case) 
	- those forest level boosted RF can be trained with tree level boosting xd

#### educated guess
trade off amount of work / results

**min option**
stacking RF (classic RF)

**advanced / for experiments**
compare these:
- stacking RF (classic RF)
- boosting RF (tree level)
- above combined - stacking tree level boosted RF