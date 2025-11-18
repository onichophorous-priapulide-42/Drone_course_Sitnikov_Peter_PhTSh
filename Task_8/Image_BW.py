import cv2
import numpy as np
img = cv2.imread("Graph_dop_vel.PNG")
cv2.imshow("Image BW Window", cv2.cvtColor(img, 6))
try:
    while True:
        key = cv2.waitKey(1)
        if key == 27:
            break
finally:
    cv2.destroyAllWindows()
