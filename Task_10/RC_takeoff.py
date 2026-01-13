from pioneer_sdk import Pioneer
drone = Pioneer()
Hup = 1

def takeoff(Hup):
    h = drone.get_dist_sensor_data(get_last_received=True)
    while h < Hup:
        ch_1 = 1500 + int((300*(Hup-h)/(Hup)))+50
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
        h = drone.get_dist_sensor_data(get_last_received=True)

def land():
    h = drone.get_dist_sensor_data(get_last_received=True)
    while h > 0.02:
        ch_1 = 1500 - int((100*(h)))-100
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)
        h = drone.get_dist_sensor_data(get_last_received=True)
    return

try:
    for i in range(0, 100):
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

    drone.arm()
    
    h = drone.get_dist_sensor_data(get_last_received=True)
    takeoff(Hup)
    while True:
        ch_1 = 1500
        ch_2 = 1500
        ch_3 = 1500
        ch_4 = 1500
        ch_5 = 2000
        drone.send_rc_channels(ch_1, ch_2, ch_3, ch_4, ch_5)

except:
    land()
    drone.disarm()

