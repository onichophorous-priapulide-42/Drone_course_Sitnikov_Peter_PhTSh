import cv2
import numpy as np

prison = cv2.VideoCapture(0)
try:
    while True:
        t, frame = prison.read()
        cv2.imshow("Camera_Machine", cv2.cvtColor(frame, 6))
        key = cv2.waitKey(1)
        if key == 27:
            break
finally:
    cv2.destroyAllWindows()
