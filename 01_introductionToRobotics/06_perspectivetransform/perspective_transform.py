#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 18:00:29 2017

@author: Shane Reynolds
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

image = mpimg.imread('example_grid1.jpg')
plt.imshow(image)
plt.show()

import cv2
import numpy as np

def perspect_transform(img, src, dst):
    
    # Get transform matrix using cv2.getPerspectiveTransform()
    M = cv2.getPerspectiveTransform(src, dst)
    
    # Warp image using cv2.warpPerspective()
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    
    # Return the result
    return warped

# Determine the four points of reference for the first person
# image
source = np.float32([[14.94,139.83],[301.57,139.91],[199.08,95.82],[119.32,95.75]])

# Determine the four points of reference for the top down
# transformation
destination = np.float32([[150,150],[160,150],[160,140],[150,140]])

# Transform the image to the top down map
warped = perspect_transform(image, source, destination)

# Add lines to the image which show the mapping
cv2.polylines(image, np.int32([source]), True, (0, 0, 255), 3)
cv2.polylines(warped, np.int32([destination]), True, (0, 0, 255), 3)

# Create the two axes that the images will be plotted
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 6), sharey=True)
f.tight_layout()

# Plot the original image to the first subplot
ax1.imshow(image)
ax1.set_title('Original Image', fontsize=40)

# Plot the second image to the subplot
ax2.imshow(warped, cmap='gray')
ax2.set_title('Result', fontsize=40)

# Adjustments to the plots and then show the plot
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
plt.show()