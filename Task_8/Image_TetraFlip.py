import cv2
import numpy as np

img_o = cv2.imread("Graph_dop_vel.PNG")
img_x = cv2.flip(img_o, 0)
img_y = cv2.flip(img_o, 1)
img_a = cv2.flip(img_o, -1)

img_u = cv2.vconcat([img_o, img_x])
img_d = cv2.vconcat([img_y, img_a])
img = cv2.hconcat([img_u, img_d])
img = cv2.resize(img, None, fx = 0.5, fy = 0.5)

try:
    while True:
        cv2.imshow("Image TetraFlip Window", img)
        key = cv2.waitKey(1)
        if key == 27:
            break
finally:
    cv2.destroyAllWindows()
