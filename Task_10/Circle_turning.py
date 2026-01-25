import numpy as np
from pioneer_sdk import Pioneer
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
    while True:
        ch_1 = 1500
        ch_2 = 1700
        ch_3 = 1600
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
        '''
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
        '''
except KeyboardInterrupt:
    drone.land()
    drone.disarm()
