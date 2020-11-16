from time import sleep
import tellopy


def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)


def test():
    drone = tellopy.Tello()
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)

        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        sleep(5)
        drone.up(10)
        sleep(2)
        drone.up(0)
        sleep(1)
        drone.forward(20)
        sleep(5)
        drone.forward(0)
        sleep(1)
        drone.backward(20)       
        sleep(5)
        drone.backward(0)
        sleep(1)
        drone.land()
        sleep(5)

    except Exception as ex:
        drone.land() #エラーが起きたらその場で緊急着陸
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    test()
