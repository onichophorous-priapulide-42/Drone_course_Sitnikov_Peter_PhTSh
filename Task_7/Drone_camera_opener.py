import cv2
import numpy as np
from pioneer_sdk import Camera

cam = Camera()

while True:
    img = cam.get_cv_frame()
    if img is not None:
        cv2.imshow("Drone camera", img)
    cv2.waitKey(1)
