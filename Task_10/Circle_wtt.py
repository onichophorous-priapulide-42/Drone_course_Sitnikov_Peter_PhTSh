import numpy as np
from pioneer_sdk import Pioneer
import math
drone = Pioneer()

try:
    drone.arm()
    for i in range(0, 1000):
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    drone.takeoff()
    for i in range(0, 1000):
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
    size = 100
    l = 10
    mas = [x for x in range(int(-math.pi)*size, int(math.pi)*size+1)]
    mas += mas[::-1]
    mas += mas[::-1]
    while True:
        s = size
        for a in mas[:size*4 + 1]:
            ang = a/size
            s += 1
            ch_1 = 1500
            ch_2 = 1500
            ch_3 = 1500 - int(math.sin(ang)*200)
            ch_4 = 1500 - int(math.cos(ang)*200)
            ch_5 = 2000
            #print(ch_3, ch_4)
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
    drone.land()
    drone.disarm()
