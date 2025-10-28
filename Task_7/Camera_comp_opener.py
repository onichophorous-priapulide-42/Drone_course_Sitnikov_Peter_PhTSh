import cv2
import numpy as np

prison = cv2.capture(0)
while True:
    t, frame = prison.read()
    imshow(frame)
    cv2.waitkey(1)
    

