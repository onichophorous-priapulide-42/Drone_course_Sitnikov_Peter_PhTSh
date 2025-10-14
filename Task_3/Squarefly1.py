from pioneer_sdk import Pioneer
import time
import math
drone = Pioneer()
def wait():
    while not drone.point_reached():
        pass
try:
    drone.arm()
    drone.takeoff()
    drone.go_to_local_point(0,0,1,0)
    wait()
    drone.go_to_local_point(0,1,1,0)
    wait()
    drone.go_to_local_point(-1,1,1,0)
    wait()
    drone.go_to_local_point(-1,0,1,0)
    wait()
    drone.go_to_local_point(0,0,1,0)
    wait()
    time.sleep(2)
finally:
    drone.land()
    drone.disarm()
