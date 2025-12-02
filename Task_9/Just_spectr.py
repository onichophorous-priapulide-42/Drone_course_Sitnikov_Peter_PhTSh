import cv2
import numpy as np

line = 3
spectr = np.zeros((400, 255*2*3*line, 3), np.uint8)

for i in range(0, 255):
    spectr[:, i*line:i*line+line] = (255, i, 0)
for i in range(255, 255*2):
    c = i-255
    spectr[:, i*line:i*line+line] = (255-c, 255, 0)

for i in range(255*2, 255*3):
    c = i-255*2
    spectr[:, i*line:i*line+line] = (0, 255, c)
for i in range(255*3, 255*4):
    c = i-255*3
    spectr[:, i*line:i*line+line] = (0, 255-c, 255)

for i in range(255*4, 255*5):
    c = i-255*4
    spectr[:, i*line:i*line+line] = (c, 0, 255)
for i in range(255*5, 255*6):
    c = i-255*5
    spectr[:, i*line:i*line+line] = (255, 0, 255-c)

spectr = cv2.resize(spectr, None, fx=0.25, fy=0.25)
cv2.imshow("Spectr", spectr)
while True:
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()
        break
