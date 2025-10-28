import cv2
import numpy as np

prison = cv2.VideoCapture(0)
while True:
    t, frame = prison.read()
    cv2.imshow("Camera_Machine", frame)
    cv2.waitKey(1)
cv2.destroyAllWindows
