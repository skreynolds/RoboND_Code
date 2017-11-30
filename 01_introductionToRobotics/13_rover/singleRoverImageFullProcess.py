# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:16:41 2017

@author: Shane Reynolds
"""
import cv2
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd

from extraFunctions import perspect_transform, color_thresh, \
                            rover_coords, pix_to_world

class Databucket():
    def __init__(self):
        self.images = csv_img_list  
        self.xpos = df["X_Position"].values
        self.ypos = df["Y_Position"].values
        self.yaw = df["Yaw"].values
        self.count = 0 # This will be a running index
        self.worldmap = np.zeros((200, 200, 3)).astype(np.float)
        self.ground_truth = ground_truth_3d # Ground truth worldmap


# Define a function to pass stored images to
# reading rover position and yaw angle from csv file
# This function will be used by moviepy to create an output video
def process_image(img):
    # Example of how to use the Databucket() object defined above
    # to print the current x, y and yaw values 
    # print(data.xpos[data.count], data.ypos[data.count], data.yaw[data.count])

    # TODO:
    ##############################################################
    # 1) Define source and destination points for perspective transform
    ##############################################################
    dst_size = 5 
    bottom_offset = 6
    source = np.float32([[14, 140], [301 ,140],[200, 96], [118, 96]])
    destination = np.float32([[img.shape[1]/2 - dst_size, img.shape[0] - bottom_offset],
                  [img.shape[1]/2 + dst_size, img.shape[0] - bottom_offset],
                  [img.shape[1]/2 + dst_size, img.shape[0] - 2*dst_size - bottom_offset], 
                  [img.shape[1]/2 - dst_size, img.shape[0] - 2*dst_size - bottom_offset],
                  ])
    #############################################################
    # 2) Apply perspective transform
    #############################################################
    warped = perspect_transform(img, source, destination)
    plt.imshow(warped)
    plt.show()
    #############################################################
    # 3) Apply color threshold to identify navigable terrain/obstacles/rock samples
    #############################################################
    
    # Threshold image for terrain
    nav = color_thresh(warped, (165, 165, 165))
    
    # Threshold image for gold rocks
    hsv_warped = cv2.cvtColor(warped, cv2.COLOR_RGB2HSV)
    lower_thres = np.array([0,100,110])
    upper_thres = np.array([70,255,255])
    rock = cv2.inRange(hsv_warped, lower_thres, upper_thres).astype(bool).astype(int)
    
    # Threshold image for obstacles
    obstacles_temp = color_thresh(warped, (135, 135, 135))
    obstacles_temp ^= 1
    
    # Threshold image for cone
    # Cone derivation
    nav_thresh = color_thresh(img, (165, 165, 165))
    obstacles_thresh = nav_thresh.copy()
    obstacles_thresh ^= 1
    cone = perspect_transform(obstacles_thresh, source, destination)
    cone ^= 1
    cone = np.logical_and(obstacles_temp, cone)
    
    # Thresholded image for obstacles (with cone and rocks removed)
    obstacles = obstacles_temp - cone - rock
    
    # Images showing the progression of the thresholding
    plt.imshow(nav, cmap='gray')
    plt.show()
    
    plt.imshow(rock, cmap='gray')
    plt.show()
    
    plt.imshow(obstacles_temp, cmap='gray')
    plt.show()
    
    plt.imshow(cone, cmap='gray')
    plt.show()
    
    plt.imshow(obstacles, cmap='gray')
    plt.show()
    
    #############################################################
    # 4) Convert thresholded image pixel values to rover-centric coords
    #############################################################
    
    # Terrain
    xpix_nav, ypix_nav = rover_coords(nav)
    
    # Obstacles
    xpix_obstacles, ypix_obstacles = rover_coords(obstacles)
    
    # Rocks
    xpix_rock, ypix_rock = rover_coords(rock)
    
    #############################################################
    # 5) Convert rover-centric pixel values to world coords
    #############################################################
    
    # Define parameters which will transform image
    count = data.count
    xpos = data.xpos[count]
    ypos = data.ypos[count]
    yaw = data.yaw[count]
    world_size = 200
    scale = 10
    
    # Terrain
    nav_x_world, nav_y_world = pix_to_world(xpix_nav, ypix_nav, xpos, ypos, yaw, world_size, scale)
    
    # Obstacles
    obstacle_x_world, obstacle_y_world = pix_to_world(xpix_obstacles, ypix_obstacles, xpos, ypos, yaw, world_size, scale)
    
    # Rocks
    rock_x_world, rock_y_world = pix_to_world(xpix_rock, ypix_rock, xpos, ypos, yaw, world_size, scale)
    
    #############################################################
    # 6) Update worldmap (to be displayed on right side of screen)
        # Example: data.worldmap[obstacle_y_world, obstacle_x_world, 0] += 1
        #          data.worldmap[rock_y_world, rock_x_world, 1] += 1
        #          data.worldmap[navigable_y_world, navigable_x_world, 2] += 1
    #############################################################
    
    data.worldmap[obstacle_y_world, obstacle_x_world, 0] += 10 
    data.worldmap[rock_y_world, rock_x_world, 1] += 10
    data.worldmap[nav_y_world, nav_x_world, 2] += 10
    
    #############################################################
    # 7) Make a mosaic image, below is some example code
    #############################################################
        # First create a blank image (can be whatever shape you like)
    output_image = np.zeros((img.shape[0] + data.worldmap.shape[0], img.shape[1]*2, 3))
        # Next you can populate regions of the image with various output
        # Here I'm putting the original image in the upper left hand corner
    output_image[0:img.shape[0], 0:img.shape[1]] = img

        # Let's create more images to add to the mosaic, first a warped image
        # Add the warped image in the upper right hand corner
    output_image[0:img.shape[0], img.shape[1]:] = warped
        
        # Add an image which shows the thresholded perspective transform
    output_image[image.shape[0]:(image.shape[0]+160), image.shape[1]:, 2] = nav
    output_image[image.shape[0]:(image.shape[0]+160), image.shape[1]:, 0] = obstacles
    output_image[image.shape[0]:(image.shape[0]+160), image.shape[1]:, 1] = rock
    
        # Overlay worldmap with ground truth map
    map_add = cv2.addWeighted(data.worldmap, 1, data.ground_truth, 0.5, 0)
        # Flip map overlay so y-axis points upward and add to output_image 
    output_image[img.shape[0]:, 0:data.worldmap.shape[1]] = np.flipud(map_add)

        # Then putting some text over the image
    cv2.putText(output_image,"Populate this image with your analyses to make a video!", (20, 20), 
                cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255), 1)
    if data.count < len(data.images) - 1:
        data.count += 1 # Keep track of the index in the Databucket()
    
    return nav, obstacles, rock, output_image


if __name__ == '__main__':
    
    file_path = 'test_1.jpg'
    
    image = mpimg.imread(file_path)
    plt.imshow(image)
    plt.show()
    
    # Change the path below to your data directory
    # If you are in a locale (e.g., Europe) that uses ',' as the decimal separator
    # change the '.' to ','
    df = pd.read_csv('../../../RoboND-Rover-Project/test_dataset/robot_log.csv', delimiter=',', decimal='.')
    csv_img_list = df["Path"].tolist() # Create list of image pathnames
    # Read in ground truth map and create a 3-channel image with it
    ground_truth = mpimg.imread('../../../RoboND-Rover-Project/calibration_images/map_bw.png')
    ground_truth_3d = np.dstack((ground_truth*0, ground_truth*255, ground_truth*0)).astype(np.float)
    
    data = Databucket()
    
    nav, obstacles, rock, output = process_image(image)
    
    