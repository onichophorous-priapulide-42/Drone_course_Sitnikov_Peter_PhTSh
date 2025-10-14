from pioneer_sdk import Pioneer
import time
drone = Pioneer()
try:
    #drone.arm()
    n = 0
    while True:
        if input() == "":
            if n%3 == 0:
                drone.led_control(255,0,0,1)
            elif n%3  == 1:
                drone.led_control(255,0,1,0)
            else:
                drone.led_control(255,1,0,0)
            n+=1
finally:
    drone.land()
    drone.disarm()
    drone.led_control(255,0,0,0)
