#!usr/bin/env python
"""
Created on Sun Oct  8 12:17:48 2017

@author: Shane Reynolds
"""

from sympy import symbols, cos, sin, pi, simplify, sqrt, atan2
from sympy.matrices import Matrix

###############################################################
# Problem Statement:
  # Let P be a vector expressed in frame {B} with (x,y,z)
  # coordinates = (15.0, 0.0, 42.0)
  # Rotate P about the Y-axis by angle = 110 degrees. 
  # Then translate the vector 1 unit
  # in the X-axis and 30 units in the Z-axis. 
  # Print the new (x, y, z) coordinates of P after the transformation.  
###############################################################
#### Create symbols for joint variables
q1 = symbols('q1')
gamma  = symbols('gamma')

#### TO DO ####
# Replace P and T with appropriate expressions and calculate new coordinates of P in {A}. 
P = Matrix([[15.0],
            [0.0],
            [42.0],
            [1]])     # P should be a 4x1 Matrix
T = Matrix([[cos(q1),   0,     sin(q1),     1],
            [0,         1,     0,           0],
            [-sin(q1),  0,     cos(q1),     30],
            [0,         0,     0,           1]])     # T Should be a 4x4 homogeneous Transform
P_new = T*P
P_new = P_new.evalf(subs={q1: 110*pi/180})
print(P_new)