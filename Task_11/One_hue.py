import cv2
import numpy as np
from pioneer_sdk import Camera

cam = Camera()

while True:
    img = cam.get_cv_frame()
    blue_img = img.copy()
    
    if img is not None:
        cv2.imshow("Drone camera", img)
        cv2.imshow("Blue Drone camera", blue_img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
