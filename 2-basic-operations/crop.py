import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bleach.png'))

cropped_img = img[360:720, 640:1280]

cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)
print(cropped_img.shape)