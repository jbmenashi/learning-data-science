# Importing the dataset
dataset = read.csv('OPS.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$OPS, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# MLR on the training set
regressor = lm(formula = OPS ~ .,
               data = training_set,
               )
#then run summary(regressor) to see the P-Values