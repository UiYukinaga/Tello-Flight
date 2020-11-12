# Telloが定常円旋回をするコード
# Argument: 何回転するか

from time import sleep
import tellopy
import sys

def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)


def rotate_cw(n_rote):
    drone = tellopy.Tello()
    secs_per_rotate = 16
    flight_time = n_rote * secs_per_rotate
    
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        sleep(5)
        
#        drone.up(20)
#        sleep(2)
#        drone.up(0)
        
        # 定常円旋回は、前進とその場旋回のベクトル和で実現
        drone.forward(20)   # 前進飛行速度=20cm/s
        drone.clockwise(36) # 旋回方向と角速度を設定(時計回り, 36deg/s)
        sleep(flight_time)
        drone.forward(0)
        drone.clockwise(0)
        sleep(1)
        drone.land()
        sleep(5)

    except Exception as ex:
        drone.land() #エラーが起きたらその場で緊急着陸
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    args = sys.argv
    deg = int(args[1])
    rotate_cw(deg)
