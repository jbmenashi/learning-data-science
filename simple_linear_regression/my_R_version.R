#Simple Linear Regression

dataset = read.csv('Lebron.csv')

library(caTools)
set.seed(123)
split = sample.split(dataset$PTS, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting Simple Linear Regression to the Training set
regressor = lm(formula = PTS ~ MP, 
               data = training_set)
#PTS is proportional to MP
# do summary(regressor) to see how statistically significant things are

#Prediciting the Test Set results
y_pred = predict(regressor, newdata = test_set)

#Visualizing the Training set
library(ggplot2)

ggplot() +
  geom_point(aes(x = training_set$MP, y = training_set$PTS),
             colour = 'red') +
  geom_line(aes(x = training_set$MP, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('LeBron Minutes vs Points (Training set)') +
  xlab('Minutes') +
  ylab('Points')

ggplot() +
  geom_point(aes(x = test_set$MP, y = test_set$PTS),
             colour = 'red') +
  geom_line(aes(x = training_set$MP, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('LeBron Minutes vs Points (Test set)') +
  xlab('Minutes') +
  ylab('Points')

