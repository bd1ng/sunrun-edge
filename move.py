import time
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

# Setup I2C interface
i2c = busio.I2C(SCL, SDA)

# Setup PCA9685 using the I2C interface
pca = PCA9685(i2c)
pca.frequency = 50  # Standard for servos

# Create servo objects on channels 1 and 4
servo1 = servo.Servo(pca.channels[0])  # Channel 1
servo4 = servo.Servo(pca.channels[3])  # Channel 4

# Move the servos
try:
    while True:
        # Sweep from 0 to 180 degrees
        for angle in range(0, 181, 10):
            servo1.angle = angle
            servo4.angle = angle  # Move in opposite direction
            time.sleep(0.1)
        # Sweep back from 180 to 0 degrees
        for angle in range(180, -1, -10):
            servo1.angle = angle
            servo4.angle = angle
            time.sleep(0.1)

except KeyboardInterrupt:
    servo1.angle = None
    servo4.angle = None
    print("Stopped by User")