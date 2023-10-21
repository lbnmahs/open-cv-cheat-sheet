import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bmw_1.jpg'))
# This example is converting the image to HSV color scheme
# Play around with the cv2.COLOR_ method to see the different types of color schemes
img_converted = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# Displaying the images
cv2.imshow('Original Image', img)
cv2.imshow('Color Converted Image', img_converted)
cv2.waitKey(0)