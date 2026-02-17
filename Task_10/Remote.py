import cv2
import numpy as np
from pioneer_sdk import Pioneer

drone = Pioneer()

window = np.zeros((500, 800, 3))
cv2.putText(window, "It's window, where you can manipulate your drone", [0, 250], cv2.FONT_HERSHEY_SIMPLEX,1,[255,255,255],1)
cv2.imshow("Flight remote", window)

def takeoff(Hup):
    old = 0
    h = drone.get_dist_sensor_data(get_last_received=True)
    while h < Hup:
        ch_1 = 1500 + int((300*(Hup-h)/(Hup)))+100
        print(ch_1)
        old = ch_1
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
        h = drone.get_dist_sensor_data(get_last_received=True)
        old += 1
        if old >= 1000:
            return takeoff(Hup)
    return [0, 1500]

def land():
    h = drone.get_dist_sensor_data(get_last_received=True)
    while h > 0.03:
        ch_1 = 1500 - int((100*(h))) - 150
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
        h = drone.get_dist_sensor_data(get_last_received=True)
    ch_1 = 1000
    ch_2 = 1500
    ch_3 = 1500
    ch_4 = 1500
    ch_5 = 2000
    drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    return [0, 1500]

sens = 5

def fd():
    for i in range(0, sens):
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1200
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    return [3, 2000]

def bk():
    for i in range(0, sens):
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1800
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    return [3, 1000]

def rt():
    for i in range(0, sens):
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1800
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    return [4, 1000]

def lt():
    for i in range(0, sens):
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1200
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    return [4, 2000]

def ro_rt():
    for i in range(0, sens):
        ch_1 = 1500
        ch_2 = 1200
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    return [0, 1500]

def ro_lt():
    for i in range(0, sens):
        ch_1 = 1500
        ch_2 = 1800
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    return [0, 1500]

def up():
    ch_1 = 2000
    ch_2 = 1500
    ch_3 = 1500
    ch_4 = 1500
    ch_5 = 2000
    drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    return [0, 1500]

def down():
    ch_1 = 1200
    ch_2 = 1500
    ch_3 = 1500
    ch_4 = 1500
    ch_5 = 2000
    drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    return [0, 1500]

t = 10
def circle(t):
    for i in range(0, t):
        ch_1 = 1500
        ch_2 = 1800
        ch_3 = 1700
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

is_armed = False

for i in range(0, 100):
    ch_1 = 1500
    ch_2 = 1500
    ch_3 = 1500
    ch_4 = 1500
    ch_5 = 2000
    drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

f = [0, 1500]

try:
    #drone.arm()
    #takeoff(1)
    while True:
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            land()
            drone.disarm()
            break
        if key == ord("1") and not is_armed:
            print("arm")
            drone.arm()
            is_armed = True
        elif key == ord("2") and is_armed:
            print("disarm")
            drone.disarm()
            is_armed = False
        elif is_armed:
            if key == ord("3"):
                takeoff(1)
            elif key == ord("4"):
                land()
            elif key == ord("w"):
                #print("w")
                f = fd()
            elif key == ord("s"):
                f = bk()
            elif key == ord("d"):
                f = rt()
            elif key == ord("a"):
                f = lt()
            elif key == ord("q"):
                f = ro_lt()
            elif key == ord("e"):
                f = ro_rt()
            elif key == ord("="):
                f = up()
            elif key == ord("-"):
                f = down()
            elif key == ord("`"):
                circle(t)
            else:
                ch_1 = 1500
                ch_2 = 1500
                '''
                if f[0] == 3:
                    ch_3 = f[1]
                else:
                    ch_3 = 1500
                if f[0] == 4:
                    ch_4 = f[1]
                else:
                    ch_4 = 1500
                '''
                ch_3 = 1500
                ch_4 = 1500
                ch_5 = 2000
                drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
                f = [0, 1500]
        else:
            pass            
           
except KeyboardInterrupt:
    drone.land()
    drone.disarm()
    cv2.destroyAllWindows()
