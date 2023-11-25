#### boosting def
*adaboost paper*
Boosting is a general method for improving the accuracy of any given learning algorith

Boosting refers to a general and provably effective method of producing a very accurate prediction rule by combining rough and moderately inaccurate rules of thum

#### adaboost
https://cseweb.ucsd.edu/~yfreund/papers/IntroToBoosting.pdf
##### algorithm
1) uniformed weighted samples
2) create weak learner with
3) evaluate learner
4) reassign weights with higher weight for wrongly classified samples
5) repeat for n learners
- weighted *(accuracy)* voting

##### idea
- create prediction for horse racing
- no grand set of rules (at general)
- expert give data rules of thumb
	- most won races
	- most favorite odds
- let's combine them into one rule


