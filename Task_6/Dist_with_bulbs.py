from pioneer_sdk import Pioneer
import time
import math
import random
drone = Pioneer()
def wait():
    while not drone.point_reached():
        pass
    #time.sleep(1)
try:
    
    #drone.arm()
    #drone.takeoff()
    #drone.go_to_local_point(0,0,1.5,0)
    #wait()
    drone.led_control(255,1,1,1)
    dist = drone.get_dist_sensor_data(get_last_received=True)
    '''
    while True:
        tmp = drone.get_dist_sensor_data(get_last_received=True)
        if abs(tmp-dist) >= 0.1:
            if tmp > 1.1:
                dist = 1.1
            elif tmp < 0.1:
                 drone.go_to_local_point(0,0,1.1,0)
                 wait()
            else:
                dist = tmp
            drone.led_control(255, 1.1-dist, dist-0.1, 0)
    
    '''
    '''
    time.sleep(6)
    while True:
        if drone.get_dist_sensor_data(get_last_received=True) < 0.5:
            drone.led_control(255, random.random(), random.random(), random.random())
            while drone.get_dist_sensor_data(get_last_received=True) < 0.5:
                continue
    '''
    tmp = drone.get_dist_sensor_data(get_last_received=True)
    if tmp <= 0.5:
        drone.led_control(255, 1, 0, 0)
    elif (tmp <= 1 and tmp >= 0.5):
        drone.led_control(255, 0, 1, 0)
    elif dist <= 1:
        drone.led_control(255, 0, 0, 1)
    while True:
        tmp = drone.get_dist_sensor_data()
        
        if tmp is None:
            continue
        if tmp <= 0.5 and dist > 0.5:
            drone.led_control(255, 1, 0, 0)
        elif (tmp <= 1 and tmp >= 0.5) and (dist > 1 or dist < 0.5):
            drone.led_control(255, 0, 1, 0)
        elif tmp >= 1 and dist < 1:
            drone.led_control(255, 0, 0, 1)
        dist = tmp
        
finally:
    drone.land()
    drone.disarm()
    drone.led_control(255,0,0,0)
