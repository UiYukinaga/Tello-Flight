# Telloが暴走した時の緊急着陸用

from time import sleep
import tellopy
import sys

def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)


def emg_land():
    drone = tellopy.Tello()
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
        drone.connect()
        drone.wait_for_connection(60.0)
        drone.land()
        sleep(5)

    except Exception as ex:
        drone.land() #エラーが起きたらその場で緊急着陸
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    emg_land()
