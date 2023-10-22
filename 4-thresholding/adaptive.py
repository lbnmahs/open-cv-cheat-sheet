import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'handwriting.jpg'))
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Better than global threshold because it automatically finds a threshold
thresh = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

cv2.imshow('Initial Image', img)
cv2.imshow('Threshold Image', thresh)

cv2.waitKey(0)