import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bleach.png'))

# Resizing
resized_img = cv2.resize(img, (960, 540))
cv2.imshow('Resized Image', resized_img)

print(img.shape)
print(resized_img.shape)

cv2.waitKey(0)