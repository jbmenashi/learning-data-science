#dummy variables for categoricals (like the state)
#create new columns, put a 1 for NY, 1 for CA, 1 for FL, 0 if its not
#always include one less DV than there are available

#p-value
# the null hypothesis is what we assume is already true
# the reg hypothesis is what we are trying to prove against it
# the p-value is the probability that IF the null hyp is true, we get the result we test
# the smaller the p-value, the better chance its not a result of luck

#5 methods of building models
1. All in - DONT DO THIS UNLESS YOU KNOW ALL YOUR VARIABLES ARE PREDICTIVE
2. Backward Elimination
   1. Select a significance level (0.05 is normal)
   2. Fit the full model with all possible predictors (all variables)
   3. Consider the predictor with highest P-value, if its higher than 5%...
      1. Remove the predictor and REFIT the model
   4. If not, the model is ready to go
3. Forward Selection
   1. Select a sig level (0.05)
   2. Fit all simple regression models, select the one with the lowest P-value
   3. Save that variable and do the regressions with one extra predictor, a different variables
   4. If the two-variable model is still significant, keep going until its not.
4. Bidirectional Elimination
   1. Select a significance level to enter and one to stay (they both can be 5$)
   2. Do the next step of Forward Selection (new variables must have p-value < 0.05 to enter)
   3. Then do all of Backward Elimination with what you have (and need 0.05 to stay)
   