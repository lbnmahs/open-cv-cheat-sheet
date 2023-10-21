import os
import cv2

# image path -> /data/porsche.jpg
img_path = os.path.join('.', 'data', 'porsche_1.jpg')

# Reading Images
img = cv2.imread(img_path)

# Writing Images / Saving images
# cv2.imwrite(os.path.join('.', 'data', 'porsche.jpg'), img)

# Visualizing Images
cv2.imshow('Image Frame', img)
cv2.waitKey(0)  # -> Important