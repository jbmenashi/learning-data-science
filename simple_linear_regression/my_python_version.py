# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:07:26 2019

@author: jbmen
"""

# y = b0 + b1*x1 / it's slope!
# y is the dependent variable (pts)
# x is the independent variable (mp)
# b1 is the coefficent for the iv, how a unit change in x1 changes y
# b0 is the constant

# Points = b0 + b1 * Minutes
# b0 is the point where it crosses the y-axis
# b1 is the actual slope of the line, that makes sense

# yi is where the data actually is, yi^ is where the data should be according to the model
# you take the difference between those two numbers and square them, then add all the points up

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
dataset = pd.read_csv('Lebron.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#split into training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

#fitting simple linear reg to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#predicting the test set results
y_pred = regressor.predict(X_test)
#so y_pred is the predicted salaries, matched up with the real salaries in y_test

#visualizing! #first the training
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title("LeBron's Minutes vs Points (training set)")
plt.xlabel('Minutes Played')
plt.ylabel('Points Scored')
plt.show()

#then the test
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title("LeBron's Minutes vs Points (test set)")
plt.xlabel('Minutes Played')
plt.ylabel('Points Scored')
plt.show()

