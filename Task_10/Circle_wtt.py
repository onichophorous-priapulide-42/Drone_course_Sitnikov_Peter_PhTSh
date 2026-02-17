import numpy as np
from pioneer_sdk import Pioneer
import math
drone = Pioneer()

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

try:
    for i in range(0, 1000):
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    drone.arm()
    takeoff(1)
    for i in range(0, 1000):
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    size = 100
    l = 10
    mas = [x for x in range(int(-math.pi*size), int(math.pi*size)+1)][::-1]
    mas += mas[::-1]
    mas += mas[::-1]

    tmp_fd = 0
    tmp_bk = 0
    
    while True:
        s = size
        for a in mas[:int(math.pi*size)*2+1]:
            ang = a/size
            s += 1
            ch_1 = 1500
            ch_2 = 1500
            if math.sin(ang) >= 0:
                ch_3 = 1500 - int(math.sin(ang)*200)
                tmp_fd += 1
            else:
                ch_3 = 1500 - int(math.sin(ang)*200)
                tmp_bk += 1
            ch_4 = 1500 - int(math.cos(ang)*200)
            ch_5 = 2000
            #print(ang*180/math.pi)
            for i in range(0, l):
                drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
        for i in range(0, 1000):
            ch_1 = 1500
            ch_2 = 1500
            ch_3 = 1500
            ch_4 = 1500
            ch_5 = 2000
            drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
        
except KeyboardInterrupt:
    print(tmp_fd, tmp_bk, tmp_fd-tmp_bk)
    drone.land()
    drone.disarm()
