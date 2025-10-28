import cv2
import numpy as np

prison = cv2.capture(0)
t, frame = prison.read()
imshow(frame)
while True:
    key = cv2.waitkey(0)
    if key == 27:
       prison.release()
        break
