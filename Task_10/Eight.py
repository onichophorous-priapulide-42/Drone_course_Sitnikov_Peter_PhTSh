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

t = 11000

tmp = []

try:
    for i in range(0, 5000):
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    drone.arm()
    takeoff(1)
    for i in range(0, 1):
        '''
        for i in range(0, t):
                ch_1 = 1500
                ch_2 = 1300
                ch_3 = 1300
                ch_4 = 1500
                ch_5 = 2000
                drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
        '''
        
        for i in range(0, int(t*1.2267)):
                ch_1 = 1500
                ch_2 = 1500 + int(100*(i/(t*1.2267)))
                ch_3 = 1400
                ch_4 = 1500
                ch_5 = 2000
                tmp.append(ch_2)
                drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
        for i in range(0, int(t*1.2267)):
                ch_1 = 1500
                ch_2 = 1600 - int(100*(i/(t*1.2267)))
                ch_3 = 1400
                ch_4 = 1500
                ch_5 = 2000
                tmp.append(ch_2)
                drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
        
    KeyboardInterrupt

except KeyboardInterrupt:
    drone.land()
    print(tmp)
