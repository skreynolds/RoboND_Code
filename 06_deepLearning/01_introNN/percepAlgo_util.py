# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 11:49:49 2017

@author: Shane Reynolds
"""

import numpy as np
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def stepFunction(t):
    if t >= 0:
        return 1
    return 0

def prediction(X, W, b):
    return stepFunction((np.matmul(X,W)+b)[0])

# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate = 0.01):
###########################################################################
# Attempt at a vectorised version of the code - flawed because
# the code didn't look if the next point was still misclassified when the
# weights are changed - we hvae to do this incrementally
###########################################################################  
#    # Create a vector of predictions 
#    yhat = np.array([prediction(X[i,:], W, b) for i in range(len(X))])
#    
#    # Create a boolean vector of incorrect classification
#    logic_y = (y != yhat)
#    
#    misclas_X = X[logic_y,:]    # Return X which are misclassified
#    misclas_yhat = y[logic_y]   # Return yhat which are misclassified
#    
#    misclas_yhat0_logical = (misclas_yhat==0)   # Logical vector for yhat0 (+)
#    misclas_yhat1_logical = (misclas_yhat==1)   # Logical vector for yhat1 (-)
#    
#    # Create the amounts to be added to the bias b
#    b_change = learn_rate*(len(misclas_yhat0_logical) - len(misclas_yhat1_logical))
#    
#    # Create the amounts to be added to the W
#    w_0_change = learn_rate*(misclas_X[misclas_yhat0_logical,0].sum() - misclas_X[misclas_yhat1_logical,0].sum())
#    w_1_change = learn_rate*(misclas_X[misclas_yhat0_logical,1].sum() - misclas_X[misclas_yhat1_logical,1].sum())
#    
#    # Alter W and b
#    W[0] = W[0] + w_0_change
#    W[1] = W[1] + w_1_change
#    b = b + b_change
###########################################################################
    for idx,y_act in enumerate(y):
        y_pred = prediction(X[idx,:],W,b)
        if not y_pred == y_act:
            if y_pred == 0:
                W[0] = W[0] + learn_rate*X[idx,0]
                W[1] = W[1] + learn_rate*X[idx,1]
                b = b + learn_rate
            else:
                W[0] = W[0] - learn_rate*X[idx,0]
                W[1] = W[1] - learn_rate*X[idx,1]
                b = b - learn_rate
    return W, b
    
# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
    return boundary_lines
