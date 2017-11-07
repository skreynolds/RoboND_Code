# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 07:18:54 2017

@author: Shane Reynolds
"""

import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    return sum([-yi*np.log(pi)-(1-yi)*np.log(1-pi) for yi,pi in zip(Y,P)])