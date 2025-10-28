import cv2
import numpy as np

prison = cv2.VideoCapture(0)
t, frame = prison.read()
cv2.imshow("Shoot", frame)
while True:
    key = cv2.waitKey(0)
    if key == 27:
        prison.release()
        cv2.destroyAllWindows()
        break
