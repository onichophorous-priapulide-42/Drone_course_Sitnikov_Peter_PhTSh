import cv2
import numpy as np

img = cv2.imread("Graph_dop_vel.PNG")
sh = img.shape
a = min(sh[0], sh[1])

try:
    while True:
        img = cv2.imread("Graph_dop_vel.PNG")
        cv2.rectangle(img, [int(sh[1]/2-a/4), int(sh[0]/2-a/4)], [int(sh[1]/2+a/4), int(sh[0]/2+a/4)], [0,0,255])
        cv2.imshow("Image Seleted Window", img)
        inc_img = img[int(sh[0]/2-a/4):int(sh[0]/2+a/4)+1, int(sh[1]/2-a/4):int(sh[1]/2+a/4)+1]
        inc_img = cv2.resize(inc_img, None, fx = 2, fy = 2)
        cv2.imshow("Image Increased Window", inc_img)
        key = cv2.waitKey(1)
        if key == 27:
            break
finally:
    cv2.destroyAllWindows()
