#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 22:33:55 2017

@author: Shane Reynolds
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Define a function to perform a color threshold
def color_thresh(img, rgb_thresh=(0, 0, 0)):
    ###### TODO:
    # Create an empty array the same size in x and y as the image 
    # but just a single channel
    color_select = np.zeros_like(img[:,:,0])
    # Apply the thresholds for RGB and assign 1's 
    # where threshold was exceeded
    red_thresh = (img[:,:,0] > rgb_thresh[0])
    blue_thresh = (img[:,:,1] > rgb_thresh[1])
    green_thresh = (img[:,:,2] > rgb_thresh[2])
    thresh_mat = np.logical_and(red_thresh,blue_thresh,green_thresh)
    color_select[thresh_mat] = 1
    # Return the single-channel binary image
    return color_select

def perspect_transform(img, src, dst):
    
    # Get transform matrix using cv2.getPerspectiveTransform()
    M = cv2.getPerspectiveTransform(src, dst)
    
    # Warp image using cv2.warpPerspective()
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    
    # Return the result
    return warped

image = mpimg.imread('sample.jpg')

# The souce and destination are variables that are fixed
# for the transformation of an image - this is something
# that needs to be calibrated prior to being able to
# make an image warp
dst_size = 5 
# Set a bottom offset to account for the fact that the bottom of the image 
# is not the position of the rover but a bit in front of it
bottom_offset = 6
source = np.float32([[14, 140], [301 ,140],[200, 96], [118, 96]])
destination = np.float32([[image.shape[1]/2 - dst_size, image.shape[0] - bottom_offset],
                  [image.shape[1]/2 + dst_size, image.shape[0] - bottom_offset],
                  [image.shape[1]/2 + dst_size, image.shape[0] - 2*dst_size - bottom_offset], 
                  [image.shape[1]/2 - dst_size, image.shape[0] - 2*dst_size - bottom_offset],
                  ])
# We note that colorsel is the colourthresholded
# binary image
# The colourthresholding filter returns a binary image
# according to a colour which has been detected
# NOTE: the white represents naviagable terrain
warped = perspect_transform(image, source, destination)
colorsel = color_thresh(warped, rgb_thresh=(160,160,160))

# This plot shows the binary image which has undergone
# a perspective transform, and then undergone colour
# thresholding
plt.imshow(colorsel, cmap='gray')
plt.show()

# This image shows an unsuccesful mapping of the
# image to rover centric coordinates
ypos, xpos = colorsel.nonzero()
plt.plot(xpos, ypos, '.')
plt.xlim(0,320)
plt.ylim(0,160)
plt.show()
