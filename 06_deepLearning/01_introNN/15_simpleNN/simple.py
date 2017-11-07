# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 06:55:23 2017

@author: Shane Reynolds
"""

import numpy as np

def sigmoid(x):
    # TODO: Implement sigmoid function
    return 1/(1+np.exp(-x))

inputs = np.array([0.7, -0.3])
weights = np.array([0.1, 0.8])
bias = -0.1

# TODO: Calculate the output
output = sigmoid(sum(inputs*weights)+bias)

print('Output:')
print(output)