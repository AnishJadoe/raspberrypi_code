from adafruit_servokit import ServoKit
import time
import board
import busio
# Import MPR121 module.
import adafruit_mpr121

nbPCAServo=16
pca = ServoKit(channels=16)
for i in range(nbPCAServo):
    pca.continuous_servo[0].throttle = 0



# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)
# Create MPR121 object.
mpr121 = adafruit_mpr121.MPR121(i2c)



while True:
    # Loop through all 12 inputs (0-11).
    #print([mpr121.baseline_data(i) for i in range(12)])
    
    for i in range(12):
        if mpr121[1].value:
            print('touched 1, faster')
            pca.continuous_servo[0].throttle += 0.05
            time.sleep(0.25)
        if mpr121[2].value:
            print('touched 2, speed up ')
            pca.continuous_servo[0].throttle -= 0.05
            time.sleep(0.25)
        if mpr121[3].value:
            print('touched 3, stop')
            pca.continuous_servo[0].throttle = 0
            time.sleep(0.25)
            
    time.sleep(0.25)  # Small delay to keep from spamming output messages.