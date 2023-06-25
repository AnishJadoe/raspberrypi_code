import RPi.GPIO as GPIO
import time
from gpiozero import AngularServo

def rotate(servo: AngularServo, servo_speed: int, duration: float):
    servo.angle = 0
    start_time = time.time()
    run_time = 0
    
    while run_time <= duration:
        run_time = time.time() - start_time
        servo.angle = servo_speed
    
    servo.angle = 0
    time.sleep(3)
    return

servo = AngularServo(4)
rotate(servo,1,2)