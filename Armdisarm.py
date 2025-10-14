from pioneer_sdk import Pioneer
import time
drone = Pioneer()
try:
    drone.arm()
    time.sleep(5)
    drone.disarm()
finally:
    drone.land()
