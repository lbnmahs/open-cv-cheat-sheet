import cv2

# Read Webcam
webcam = cv2.VideoCapture(1)    # 1 is my camera index
                                # yours can be 0 or more than one
                                # depending on how many cameras you have
webcam.set(3, 1000) # Width of webcam frame
webcam.set(4, 700)  # Height of webcam frame

# Visualize Webcam
while True: 
    ret, frame = webcam.read()

    cv2.imshow('Webcam Frame', frame)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()