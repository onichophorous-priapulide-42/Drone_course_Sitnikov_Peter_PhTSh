import cv2
import numpy as np
from pioneer_sdk import Pioneer
from pioneer_sdk import Camera
import time

drone = Pioneer()
cam = Camera()
cam.connect()
img = cam.get_cv_frame()
if img is not None:
    imshow("Drone camera", img)
