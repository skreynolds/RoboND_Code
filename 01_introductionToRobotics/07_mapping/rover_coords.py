#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 23:13:30 2017

@author: Shane Reynolds
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from extra_functions import perspect_transform, color_thresh, source, destination

# Read in the sample image
image = mpimg.imread('sample.jpg')


def rover_coords(binary_img):
    # TODO: fill in this function to 
    # Calculate pixel positions with reference to the rover 
    # position being at the center bottom of the image.
    # Basically this function flips the axes and provides
    # a translation of the image
    ypos, xpos = binary_img.nonzero()
    # These two lines simultaneously perform the axis flip
    # and then translate the image (it can be better seen
    # in the less accurate coding)
    #y_pixel = (-1)*(xpos-binary_img.shape[0]).astype(np.float)
    #x_pixel = (-1)*(ypos-binary_img.shape[1]/2).astype(np.float)
    y_pixel = (xpos-160)*(-1)
    x_pixel = (ypos-160)*(-1)
    return x_pixel, y_pixel

# Perform warping and color thresholding
warped = perspect_transform(image, source, destination)
colorsel = color_thresh(warped, rgb_thresh=(160, 160, 160))
# Extract x and y positions of navigable terrain pixels
# and convert to rover coordinates
xpix, ypix = rover_coords(colorsel)

# Plot the map in rover-centric coords
fig = plt.figure(figsize=(5, 7.5))
plt.plot(xpix, ypix, '.')
plt.ylim(-160, 160)
plt.xlim(0, 160)
plt.title('Rover-Centric Map', fontsize=20)
#plt.show() # Uncomment if running on your local machine