# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 17:44:54 2017

@author: Shane Reynolds
"""

#!/usr/bin/env python
from sympy import symbols, cos, sin, pi, sqrt
from sympy.matrices import Matrix
import numpy as np

### Create symbols for joint variables
q1, q2 = symbols('q1:3')

# Create a symbolic matrix representing an intrinsic sequence of rotations 
  # about the Y and then Z axes. Let the rotation about the Y axis be described
  # by q1 and the rotation about Z by q2. 
####### TO DO ########
# Replace R_y and R_z with the appropriate (symbolic) elementary rotation matrices 
  # and then compute YZ_intrinsic. 
R_y = Matrix([[cos(q1*pi/180.), 0, sin(q1*pi/180.)],
             [0, 1, 0],
             [-sin(q1*pi/180.), 0, cos(q1*pi/180.)]])
R_z = Matrix([[cos(q2*pi/180.), -sin(q2*pi/180.), 0],
             [sin(q2*pi/180.), cos(q2*pi/180.), 0],
             [0, 0, 1]])
YZ_intrinsic_sym = R_y*R_z

####### TO DO ########
# Numerically evaluate YZ_intrinsic assuming:
   # q1 = 45 degrees and q2 = 60 degrees. 
   # NOTE: Trigonometric functions in Python assume the input is in radians!  
#dtr = np.pi/180.
YZ_intrinsic_num = YZ_intrinsic_sym.evalf(subs={q1: 45, q2: 60})
print(YZ_intrinsic_num)