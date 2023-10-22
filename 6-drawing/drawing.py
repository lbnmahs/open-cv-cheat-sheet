import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'whiteboard.png'))

# Draw a line -> (image, (start_coordinates), (end_coordinates), (color), thickness)
line = cv2.line(img, (40, 40), (200, 200), (127, 30, 255), 2)

# Draw a rectangle -> (image, (top_left_coordinates), (bottom_right_coordinates), (color), thickness)
rect = cv2.rectangle(img, (250, 40), (400, 200), (40, 200, 50), 2)

# Draw a circle -> (image, (center_coordinates), radius, (color), thickness)
circ = cv2.circle(img, (200, 300), 50, (255, 0, 0), 1)

# Draw a text -> (image, text, (coordinates), font, font size, (color), font thickness)
text = cv2.putText(img, 'Hello World', (450, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 80), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)