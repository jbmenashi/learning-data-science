# MLR is the same formula, just longer: y = b0 + b1*x1 + b2*x2...
# where y is the dependent variable, b0 is the constant, the rest is indep

from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('MVP.csv')
X = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values
