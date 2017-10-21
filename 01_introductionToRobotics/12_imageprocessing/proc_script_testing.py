#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:36:55 2017

@author: Shane Reynolds
"""

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import glob
import improcFunc as ipf
import cv2

path = 'test_dataset/IMG/*'
img_list = glob.glob(path)
# Grab a random image and display it
idx = np.random.randint(0, len(img_list)-1)
image = mpimg.imread(img_list[idx])
plt.imshow(image)
plt.show()

example_rock = 'test_dataset/calibration_images/example_rock2.jpg'
rock_img = mpimg.imread(example_rock)
plt.imshow(rock_img)
plt.show()

##############################################################################
# Define calibration box in source (actual) and destination (desired) coordinates
# These source and destination points are defined to warp the image
# to a grid where each 10x10 pixel square represents 1 square meter
# The destination box will be 2*dst_size on each side
dst_size = 5 
# Set a bottom offset to account for the fact that the bottom of the image 
# is not the position of the rover but a bit in front of it
# this is just a rough guess, feel free to change it!
bottom_offset = 6
source = np.float32([[14, 140], [301 ,140],[200, 96], [118, 96]])
destination = np.float32([[image.shape[1]/2 - dst_size, image.shape[0] - bottom_offset],
                  [image.shape[1]/2 + dst_size, image.shape[0] - bottom_offset],
                  [image.shape[1]/2 + dst_size, image.shape[0] - 2*dst_size - bottom_offset], 
                  [image.shape[1]/2 - dst_size, image.shape[0] - 2*dst_size - bottom_offset],
                  ])
##############################################################################

# Transform the perspective of the rock image
warped = ipf.perspect_transform(rock_img, source, destination)
plt.imshow(warped)
plt.show()

# Threshold the image for nav terrain
threshed = ipf.color_thresh(warped)
plt.imshow(threshed, cmap='gray')
plt.show()

# Use cv2 to threshold the image for gold rocks
hsv_warped = cv2.cvtColor(warped, cv2.COLOR_RGB2HSV)
lower_thres = np.array([0,100,110])
upper_thres = np.array([70,255,255])
rock = cv2.inRange(hsv_warped, lower_thres, upper_thres)
plt.imshow(rock,cmap='gray')
plt.show()