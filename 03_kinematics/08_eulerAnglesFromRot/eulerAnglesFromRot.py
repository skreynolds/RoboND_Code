# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 20:44:22 2017

@author: Shane Reynolds
"""

#!/usr/bin/env python
import numpy as np
from sympy.matrices import Matrix
from sympy import symbols, atan2, sqrt


# Fixed Axis X-Y-Z Rotation Matrix
R_XYZ = Matrix([[ 0.353553390593274, -0.306186217847897, 0.883883476483184],
            [ 0.353553390593274,  0.918558653543692, 0.176776695296637],
            [-0.866025403784439,               0.25, 0.433012701892219]])

######## TO DO ##########
# Calculate the Euler angles that produces a rotation equivalent to R (above)
# NOTE: Be sure your answer has units of DEGREES!

# Note that you can access elements of the matrix using R_XYZ.row().col()
# however, this had some weird behaviour in that the value was not
# evaluated (possibly still works but )
r31 = R_XYZ[2,1]
r11 = R_XYZ[0,0]
r21 = R_XYZ[1,0]
r32 = R_XYZ[2,1]
r33 = R_XYZ[2,2]

rtd = 180/np.pi

alpha = atan2(r21,r11)*rtd
beta = atan2(r32,r33)*rtd
gamma = atan2(-r31,sqrt(r11**2+r21**2))*rtd

print(alpha,beta,gamma)