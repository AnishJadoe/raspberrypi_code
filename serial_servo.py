import serial
import struct
from time import sleep
from dataclasses import dataclass

@dataclass
class TeensyPackage():
    motor_1_rpm : int
    motor_2_rpm : int
    motor_3_rpm : int
    motor_4_rpm : int
    motor_1_error_code : int
    motor_2_error_code : int
    motor_3_error_code : int
    motor_4_error_code : int
    motor_1_current : int
    motor_2_current : int
    motor_3_current : int
    motor_4_current : int
    motor_1_voltage : int
    motor_2_voltage : int
    motor_3_voltage : int
    motor_4_voltage : int
    servo_1_angle : int
    servo_2_angle : int
    servo_3_angle : int
    servo_4_angle : int
    servo_5_angle : int
    servo_6_angle : int
    servo_7_angle : int
    servo_8_angle : int
    servo_9_angle : int
    servo_10_angle : int
    servo_1_update_time_us : int
    servo_2_update_time_us : int
    servo_3_update_time_us : int
    servo_4_update_time_us : int
    servo_5_update_time_us : int
    servo_6_update_time_us : int
    servo_7_update_time_us : int
    servo_8_update_time_us : int
    servo_9_update_time_us : int
    servo_10_update_time_us : int
    rolling_msg_out : float
    rolling_msg_out_id : int
    checksum_out : int

def package_debugger(package : TeensyPackage):
    print(f"Rolling message ID: {test.rolling_msg_out_id}")
    print(f"Rolling message: {test.rolling_msg_out}")
    print(f"Checksum: {test.checksum_out}")

    print(test.motor_1_rpm)
    print(test.motor_2_rpm)
    print(test.motor_3_rpm)
    print(test.motor_4_rpm)
    print(test.motor_1_error_code)
    print(test.motor_2_error_code)
    print(test.motor_3_error_code)
    print(test.motor_4_error_code)
    print(test.motor_1_current)
    print(test.motor_2_current)
    print(test.motor_3_current)
    print(test.motor_4_current)
    print(test.motor_1_voltage)
    print(test.motor_2_voltage)
    print(test.motor_3_voltage)
    print(test.motor_4_voltage)
    print(test.servo_1_angle)
    print(test.servo_2_angle)
    print(test.servo_3_angle)
    print(test.servo_4_angle)
    print(test.servo_5_angle)
    print(test.servo_6_angle)
    print(test.servo_7_angle)
    print(test.servo_8_angle)
    print(test.servo_9_angle)
    print(test.servo_10_angle)
    print(test.servo_1_update_time_us)
    print(test.servo_2_update_time_us)
    print(test.servo_3_update_time_us)
    print(test.servo_4_update_time_us)
    print(test.servo_5_update_time_us)
    print(test.servo_6_update_time_us)
    print(test.servo_7_update_time_us)
    print(test.servo_8_update_time_us)
    print(test.servo_9_update_time_us)
    print(test.servo_10_update_time_us)
    print("--------------------------END-----------------------------")

    
ser = serial.Serial(port='/dev/serial0', baudrate=1000,timeout=1)
format_string = "<36h1f2B"
expected_size = struct.calcsize(format_string)
START_BYTE = b'\x9a'
while True:
    start_byte = ser.read(1)
    if start_byte != START_BYTE:
        continue
    data = ser.read(expected_size)
    unpacked_data = struct.unpack(format_string, data)
    test = TeensyPackage(*unpacked_data)
    package_debugger(test)

    recieved_checksum = unpacked_data[-1]
    calculated_checksum = sum(unpacked_data[:-1]) % 256
    #print('checksum: ', recieved_checksum)
    if recieved_checksum == calculated_checksum:
        test = TeensyPackage(*unpacked_data)
        print("Servo Angles: ", test.servo_1_angle, test.servo_2_angle,test.servo_3_angle,test.servo_4_angle)
    else:
        print("Checksum verification failed")
    


        
        
            
