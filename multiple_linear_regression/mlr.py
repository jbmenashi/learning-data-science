# MLR is the same formula, just longer: y = b0 + b1*x1 + b2*x2...
# where y is the dependent variable, b0 is the constant, the rest is indep

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('OPS.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 5].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)