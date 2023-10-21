import os
import cv2

vid_path = os.path.join('.', 'data', 'drift.mp4')

# Reading Videos
video = cv2.VideoCapture(vid_path)

# Visualizing videos
ret = True

while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('Video Frame', frame)
        cv2.waitKey(20)

# IMPORTANT because it clears the memory
video.release
cv2.destroyAllWindows()