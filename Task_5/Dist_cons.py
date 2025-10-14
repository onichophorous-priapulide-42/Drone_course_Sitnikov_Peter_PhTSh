from pioneer_sdk import Pioneer
import time
import math
drone = Pioneer()
def wait():
    while not drone.point_reached():
        pass
    #time.sleep(1)
f = (1+(5**0.5))/2
try:
    drone.arm()
    drone.takeoff()
    drone.go_to_local_point(0,0,1.5,0)
    wait()
    
    while True:
        print(drone.get_dist_sensor_data(get_last_received=True))
        #time.sleep(1)
    
    '''
    time.sleep(6)
    while True:
        if drone.get_dist_sensor_data(get_last_received=True) < 0.5:
            break
    '''
    '''
    while True:
        if drone.get_dist_sensor_data(get_last_received=True) < 0.5:
            drone.go_to_local_point_body_fixed(-1,0,0,0)
            wait()
    '''
finally:
    drone.land()
    drone.disarm()
