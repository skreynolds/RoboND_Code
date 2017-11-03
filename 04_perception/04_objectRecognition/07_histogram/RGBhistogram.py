# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 08:17:31 2017

@author: Shane Reynolds
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Read in and plot the image
image = mpimg.imread('can_image.jpg')
plt.imshow(image)

# Note that jpeg is the formate that yields the 
# best results with the RGB histogram (png doesn't
# seem to work with this)

# Take histograms in R, G, and B
r_hist = np.histogram(image[:,:,0], bins=32, range=(0, 256))
g_hist = np.histogram(image[:,:,1], bins=32, range=(0, 256))
b_hist = np.histogram(image[:,:,2], bins=32, range=(0, 256))
# We note that the image is imported as an array and that the
# default import for colour images is in RGB colour space with
# 0 = red, 1 = green, and 2 = blue

# Generating bin centers
bin_edges = r_hist[1]
bin_centers = (bin_edges[1:]  + bin_edges[0:len(bin_edges)-1])/2

# Plot a figure with all three bar charts
fig = plt.figure(figsize=(12,3))
plt.subplot(131)
plt.bar(bin_centers, r_hist[0])
plt.xlim(0, 256)
plt.title('R Histogram')
plt.subplot(132)
plt.bar(bin_centers, g_hist[0])
plt.xlim(0, 256)
plt.title('G Histogram')
plt.subplot(133)
plt.bar(bin_centers, b_hist[0])
plt.xlim(0, 256)
plt.title('B Histogram')
plt.show()