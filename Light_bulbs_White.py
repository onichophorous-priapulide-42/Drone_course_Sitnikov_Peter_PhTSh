from pioneer_sdk import Pioneer
import time
drone = Pioneer()
try:
    #drone.arm()
    while True:
        time.sleep(1)
        drone.led_control(255,1,1,1)
        time.sleep(0.05)
        drone.led_control(255,0,0,0)
finally:
    drone.land()
    drone.disarm()
    drone.led_control(255,0,0,0)
