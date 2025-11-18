from pioneer_sdk import Pioneer
import time
import math
import cv2
import numpy as np

drone = Pioneer()

try:
    while True:
        h = drone.get_dist_sensor_data(get_last_received=True)
        if h != 65.53:
            img = cv2.imread("Graph_dop_vel.PNG")
            cv2.putText(img, str(h), [42,42], cv2.FONT_HERSHEY_SIMPLEX,1,[0,0,0],1)
        cv2.imshow("Image Dist Window", img)
        key = cv2.waitKey(1)
        if key == 27:
            break
finally:
    cv2.destroyAllWindows()
