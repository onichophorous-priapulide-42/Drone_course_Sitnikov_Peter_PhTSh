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

    time.sleep(6)
    while True:
        if drone.get_dist_sensor_data(get_last_received=True) < 0.5:
            drone.led_control(255, random.random(), random.random(), random.random())
            while drone.get_dist_sensor_data(get_last_received=True) < 0.5:
                continue

finally:
    drone.land()
    drone.disarm()
    drone.led_control(255,0,0,0)
