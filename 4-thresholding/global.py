import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'birds.jpg'))
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Global Thresholding
ret, thresh = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY_INV)
# Bluring
new_thresh = cv2.medianBlur(thresh, 5)
ret, new_2_thresh = cv2.threshold(new_thresh, 75, 255, cv2.THRESH_BINARY)

cv2.imshow('Initial Image', img)
cv2.imshow('Threshold Image', thresh)

cv2.waitKey(0)