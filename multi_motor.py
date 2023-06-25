import board
import time
from adafruit_servokit import ServoKit
import busio
import keyboard
from typing import List
from adafruit_pca9685 import PCA9685
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--servo', nargs='?',const=1,type=int)

args = parser.parse_args()
print(args.servo)
nbPCAServo=16


pca = ServoKit(channels=16)


def init():
    
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(500,2500)

def unload():
    pca.continuous_servo[3].throttle = 1
    time.sleep(3)
    pca.continuous_servo[3].throttle = 0
    return

def multi_control(servos : List[ServoKit]):
    
    print('running')
    running = True
    for servo in servos:
        servo.throttle = 0
    while running:
        print(f'rotation speed is {servo.throttle}')
        if keyboard.read_key() == "a":
            servos[0].throttle += 0.1
            servos[1].throttle += 0.1
            servos[2].throttle += 0.1
            
        elif keyboard.read_key() == "d":
            servos[0].throttle -= 0.1
            servos[1].throttle -= 0.1
            servos[2].throttle -= 0.1
            
        elif keyboard.read_key() == "s":
            for servo in servos:
                servo.throttle = 0
            
            print(f'Stopping Servo speed, {servo.throttle}')
            
        elif keyboard.read_key() == "q":
            print('Quiting Program')
            for servo in servos:
                servos.throttle = 0
                
            time.sleep(1)
            break

    print('done')
    return
    
def control_servo(servos):
    print('running')
    running = True
    servo = servos[int(args.servo)]
    servo.throttle = 0
    while running:
        print(f'rotation speed is {servo.throttle}')
        if keyboard.read_key() == "a":
            
            servo.throttle += 0.1 
        elif keyboard.read_key() == "d":
   
            servo.throttle -= 0.1
        elif keyboard.read_key() == "s":
            servo.throttle = 0
            print(f'Stopping Servo speed, {servo.throttle}')
        elif keyboard.read_key() == "q":
            print('Quiting Program')
            servo.throttle = 0
            time.sleep(1)
            break

    print('done')
    return

def main():

     
    #print(f'starting motor 0')
    #pca.continuous_servo[3].throttle = -1 # - 1 tension , 1 slack
    servos = [pca.continuous_servo[0],pca.continuous_servo[1]]
    control_servo(servos)
    #multi_control(servos)
    #time.sleep(4)
    print(args)

    return

if __name__ == '__main__':
    main()