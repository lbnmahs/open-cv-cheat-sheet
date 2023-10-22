import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'player.jpg'))
ed_img = cv2.Canny(img, 100, 200)

cv2.imshow('Initial Image', img)
cv2.imshow('Edged Image', ed_img)

cv2.waitKey(0)