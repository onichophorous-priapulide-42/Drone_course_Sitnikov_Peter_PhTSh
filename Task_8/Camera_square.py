import cv2
import numpy as np

prison = cv2.VideoCapture(0)
try:
    while True:
        t, frame = prison.read()
        shape = frame.shape
        print([shape[0]/4, shape[1]/4])
        frame = cv2.rectangle(frame, [shape[0]/4, shape[1]/4], [shape[0]*(3/4),shape[1]*(3/4)], [0,0,0])
        cv2.imshow("Camera_Machine", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
finally:
    cv2.destroyAllWindows()
