import cv2
img = cv2.imread("Graph_dop_vel.PNG")
cv2.imshow("Image Window", img)
while True:
    key = cv2.waitKey(0)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
