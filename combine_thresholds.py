import numpy as np
import cv2
import matplotlib
matplotlib.use('ps')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle
import sys

def abs_sobel_thresh(img, orient='x', sobel_kernel=3, thresh=(0, 255)):
    orient_to_params = {'x': (1, 0), 'y': (0, 1)}
    sobel = np.abs(cv2.Sobel(img, cv2.CV_64F, orient_to_params[orient][0], orient_to_params[orient][1], ksize=sobel_kernel))
    grad_binary = np.zeros_like(sobel)
    grad_binary[(sobel > thresh[0]) & (sobel < thresh[1])] = 1

    return grad_binary

def mag_thresh(image, sobel_kernel=3, mag_thresh=(0, 255)):
    # Calculate gradient magnitude
    # Apply threshold
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
    sobel = (sobel_x**2 + sobel_y**2)**0.5

    mag_binary = np.zeros_like(sobel)
    mag_binary[(sobel > mag_thresh[0]) & (sobel < mag_thresh[1])] = 1    

    return mag_binary

def dir_threshold(image, sobel_kernel=3, thresh=(0, np.pi/2)):
    # Calculate gradient direction
    # Apply threshold
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=sobel_kernel)

    abs_sobel_x = np.abs(sobel_x)
    abs_sobel_y = np.abs(sobel_y)
    
    direction = np.arctan2(abs_sobel_y, abs_sobel_x)

    dir_binary = np.zeros_like(direction)
    dir_binary[(direction > thresh[0]) & (direction < thresh[1])] = 1

    return dir_binary

if __name__ == '__main__':
    input_filename = sys.argv[1]
    
    plt.imread(input_filename)
    plt.show()