import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'birds.jpg'))
# RGB to GRAY scale
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Threshold with THRESH_BINARY_INV
ret, thresh_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Looping through the list of contours
for cnt in contours:
    if cv2.contourArea(cnt) > 50:
        # Drawing contours and bounding boxes on contours > 50 on original image
        cv2.drawContours(img, cnt, -1, (0, 255, 0), 1)
        # Bounding box
        x1, y1, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 0, 255), 2)


cv2.imshow('Initial Image', img)
cv2.imshow('Thresh Image', thresh_img)
cv2.waitKey(0)