#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 08:38:29 2017

@author: Shane Reynolds
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read in an image
image = mpimg.imread('can_image.JPG')
# Your other options for input images are:
    # hammer.jpeg
    # beer.jpeg
    # bowl.jpeg
    # create.jpeg
    # disk_part.jpeg
    
# Define a function to compute color histogram features  
def color_hist(img, nbins=32, bins_range=(0, 256)):
    # Convert from RGB to HSV using cv2.cvtColor()
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    
    # Compute the histogram of the HSV channels separately
    h_hist = np.histogram(hsv_image[:,:,0], nbins, bins_range)
    s_hist = np.histogram(hsv_image[:,:,1], nbins, bins_range)
    v_hist = np.histogram(hsv_image[:,:,2], nbins, bins_range)
    
    # Concatenate the histograms into a single feature vector
    features = np.concatenate((h_hist[0], s_hist[0], v_hist[0])).astype(np.float64)
    
    # Normalize the result
    norm_features = features/np.sum(features)
    
    return norm_features
    
feature_vec = color_hist(image, nbins=32, bins_range=(0, 256))

# Plot a figure with all three bar charts
if feature_vec is not None:
    fig = plt.figure(figsize=(12,6))
    plt.plot(feature_vec)
    plt.title('HSV Feature Vector', fontsize=30)
    plt.tick_params(axis='both', which='major', labelsize=20)
    fig.tight_layout()
    plt.show()
else:
    print('Your function is returning None...')