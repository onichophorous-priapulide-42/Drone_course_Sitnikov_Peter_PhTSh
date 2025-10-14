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
    drone.go_to_local_point(0,0,1,0)
    wait()
    drone.go_to_local_point(0,1,1,0)
    wait()
    drone.go_to_local_point_body_fixed(0,0,0,-(0.8)*math.pi)
    wait()
    drone.go_to_local_point_body_fixed(0,1,0,0)
    wait()
    drone.go_to_local_point_body_fixed(0,0,0,-(0.8)*math.pi)
    wait()
    drone.go_to_local_point_body_fixed(0,1,0,0)
    wait()
    drone.go_to_local_point_body_fixed(0,0,0,-(0.8)*math.pi)
    wait()
    drone.go_to_local_point_body_fixed(0,1,0,0)
    wait()
    drone.go_to_local_point_body_fixed(0,0,0,-(0.8)*math.pi)
    wait()
    drone.go_to_local_point_body_fixed(0,1,0,0)
    wait()
finally:
    drone.land()
    drone.disarm()
