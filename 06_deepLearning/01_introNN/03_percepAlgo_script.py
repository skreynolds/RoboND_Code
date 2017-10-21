# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:02:03 2017

@author: Shane Reynolds
"""

import pandas as pd
from percepAlgo_util import trainPerceptronAlgorithm 

df = pd.read_csv('03_data.csv', names=['x1','x2','y'])

X = df[['x1','x2']].values
y = df['y'].values

output = trainPerceptronAlgorithm(X, y)