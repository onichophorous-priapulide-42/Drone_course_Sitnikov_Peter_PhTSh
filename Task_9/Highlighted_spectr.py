import cv2
import numpy as np

prev = 0
def callback(event, x, y, flags, userdata):
    copy = userdata.copy()
    if event != 0 and flags == 1:
        try:
           spectr[:, x-1] = (0,0,0)
           copy[:,x-1] = (0,0,0)
        except:
            pass
        arr.append(x)
        arr.append(x)
        cv2.putText(copy, str(userdata[y,x,2])+" "+str(userdata[y,x,1])+" "+str(userdata[y,x,0]), [42,42], cv2.FONT_HERSHEY_SIMPLEX,1,[0,0,0],1)
        cv2.imshow("Spectr", copy)
    elif event == 0 and flags == 1:
        try:
           copy[:, x+1] = (0,0,0)
        except:
            pass
        arr[1] = x
        cv2.putText(copy, str(userdata[y,x,2])+" "+str(userdata[y,x,1])+" "+str(userdata[y,x,0]), [42,42], cv2.FONT_HERSHEY_SIMPLEX,1,[0,0,0],1)
        cv2.imshow("Spectr", copy)
    else:
        try:
            copy[:, x-1] = (0,0,0)
            copy[:, x+1] = (0,0,0)
        except:
            pass
        
        if arr != []:
            s = min(arr)
            f = max(arr)
            print("from", userdata[0,s,2], userdata[0,s,1], userdata[0,s,0])
            print("to", userdata[0,f,2], userdata[0,f,1], userdata[0,f,0])
            arr.clear()
            spectr[:] = orig.copy()
            
        cv2.putText(copy, str(userdata[y,x,2])+" "+str(userdata[y,x,1])+" "+str(userdata[y,x,0]), [42,42], cv2.FONT_HERSHEY_SIMPLEX,1,[0,0,0],1)
        cv2.imshow("Spectr", copy)
    #print(event, x, y, flags)

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

arr = []
spectr = cv2.resize(spectr, None, fx=0.25, fy=0.25)
orig = spectr.copy()
cv2.imshow("Spectr", spectr)
cv2.setMouseCallback("Spectr", callback, spectr)
while True:
    key = cv2.waitKey(1)
    if key == 27:
        cv2.destroyAllWindows()
        break
