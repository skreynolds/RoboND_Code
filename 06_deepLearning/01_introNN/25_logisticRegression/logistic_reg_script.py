# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:01:58 2017

@author: Shane Reynolds
"""

import pandas as pd
import matplotlib.pyplot as plt
from logistic_regression import trainLR

# Import the dataset to be analysed
df = pd.read_csv('data.csv', names=(['x1', 'x2', 'y']))

# Set X and set y
X = df[['x1', 'x2']].values
y = df['y'].values

boundary, error = trainLR(X, y)

plt.plot(error)
plt.show()