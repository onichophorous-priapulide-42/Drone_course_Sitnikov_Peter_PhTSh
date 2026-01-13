import cv2
import numpy as np
from pioneer_sdk import Pioneer
drone = Pioneer()

window = np.zeros((500, 800, 3))
cv2.putText(window, "It's window, where you can manipulate your drone", [0, 250], cv2.FONT_HERSHEY_SIMPLEX,1,[255,255,255],1)
cv2.imshow("Flight remote", window)

def takeoff(Hup):
    h = drone.get_dist_sensor_data(get_last_received=True)
    while h < Hup:
        ch_1 = 1500 + int((300*(Hup-h)/(Hup)))+50
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
        h = drone.get_dist_sensor_data(get_last_received=True)
    return

def land():
    h = drone.get_dist_sensor_data(get_last_received=True)
    while h > 0:
        ch_1 = 1500 - int((100*(h)))-100
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
    return
is_armed = False

for i in range(0, 100):
    ch_1 = 1500
    ch_2 = 1500
    ch_3 = 1500
    ch_4 = 1500
    ch_5 = 2000
    drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

try:
    drone.arm()
    takeoff(1)
    while True:
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            land()
            drone.disarm()
        if key == ord("1") and not is_armed:
            drone.arm()
            is_armed = True
        elif key == ord("2") and is_armed:
            drone.disarm()
            is_armed = False
        elif is_armed:
            if key == ord("3"):
                takeoff(1)
            elif key == ord("4"):
                land()
            else:
                ch_1 = 1500
                ch_2 = 1500
                ch_3 = 1500
                ch_4 = 1500
                ch_5 = 2000
                drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
        else:
            pass            
           
except KeyboardInterrupt:
    drone.land()
    drone.disarm()
