from gpiozero import AngularServo
import keyboard
import time

def count_rotations(servo: AngularServo, servo_speed: int, max_run_time:float):
    start_time = time.time()
    run_time = 0
    while run_time < max_run_time:
        run_time = time.time() - start_time
        servo.angle = servo_speed
        
    servo.angle = 0
    time.sleep(5)
    print('Done')
    
    return

def control_servo(servo: AngularServo):
    print('running')
    running = True
    while running:
        print(f'rotation speed is {servo.angle}')
        if keyboard.read_key() == "a":
            print(f'CW rotation speed of {servo.angle}')
            servo.angle = 30 
        elif keyboard.read_key() == "d":
            print(f'CCW rotation speed of {servo.angle}')
            servo.angle = -40
        elif keyboard.read_key() == "s":
            servo.angle = -10
            print(f'Stopping Servo speed, {servo.angle}')
        elif keyboard.read_key() == "q":
            print('Quiting Program')
            servo.angle = -10
            time.sleep(1)
            break
        else:
            print("Waiting for Input")

    print('done')
    return




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

servo = AngularServo(18)
control_servo(servo)






