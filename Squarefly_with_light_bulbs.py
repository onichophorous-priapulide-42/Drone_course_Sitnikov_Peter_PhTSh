from pioneer_sdk import Pioneer
import time
import math
drone = Pioneer()
def wait():
    while not drone.point_reached():
        pass
    #time.sleep(1)
def light(n):
    drone.led_control(255, 1, 1, 1)
    drone.led_control(255, 0, 0, 0)
    drone.led_control(255, int(n==3), int(n==1 or n==2 or n==3), int(n==0 or n==2))
try:
    light(0)
    drone.arm()
    drone.takeoff()
    time.sleep(5)
    drone.go_to_local_point(0,0,1,0)
    wait()
    drone.go_to_local_point(0,1,1,-math.pi/2)
    wait()
    light(1)
    drone.go_to_local_point_body_fixed(0,0,0,-math.pi/2)
    wait()
    drone.go_to_local_point(-1,1,1,-math.pi)
    wait()
    light(2)
    drone.go_to_local_point_body_fixed(0,0,0,-math.pi/2)
    wait()
    drone.go_to_local_point(-1,0,1,-math.pi*(3/2))
    wait()
    light(3)
    drone.go_to_local_point_body_fixed(0,0,0,-math.pi/2)
    wait()
    drone.go_to_local_point(0,0,1,-math.pi*(3/2))
    wait()
    light(0)
    drone.go_to_local_point_body_fixed(0,0,0,-math.pi/2)
    wait()
    time.sleep(2)
finally:
    drone.land()
    drone.disarm()
    drone.led_control(255,0,0,0)
