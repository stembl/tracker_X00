## tracker_X00/MPU6050_poll.py

from mpu6050 import mpu6050
import datetime
import math
import sys


address = 0x68 # I2C of acc/gyro sensor
sendRate = 1

sensor = mpu6050(address)
# Set the accelerometer range:
# * ACCEL_RANGE_2G
# * ACCEL_RANGE_4G
# * ACCEL_RANGE_8G
# * ACCEL_RANGE_16G
sensor.set_accel_range(mpu6050.ACCEL_RANGE_16G)

# Set the gyro range:
# * GYRO_RANGE_250DEG
# * GYRO_RANGE_500DEG
# * GYRO_RANGE_1000DEG
# * GYRO_RANGE_2000DEG
sensor.set_gyro_range(mpu6050.GYRO_RANGE_250DEG)

## !!! Base these settings of the callibration, need to implement!!!
# Magic Numbers
# GYRO_SCALE_MODIFIER_2000DEG = 16.4
# ACCEL_SCALE_MODIFIER_16G = 2048.0

## Values that define how and when the program records values

maxTilt = 0         # [degrees], records angle when greater than this
                    # value.  0 returns the angle with every result.
maxG = 1.5          # [g], acceleration at which sensor records results.
                    # 0 turns off maxG results.
timeResponse = 300  # [s], time when the sensor records regardless of
                    # acceleration.  0 turns off the timeResponse.
motd = None

## threading
# I want to run multiple tasks simultaneously.
# 1. Polling the Accelerometer, save buffer
# 2. Checking accel data for response greater than max G.
# 3. Saving results around max G. Prevent saving data more than once.
# 4. Filter and save results.

# Thread to check motion values
class MotionPoller():
    def __init__(self):
        global motd
        self.current_value = None
        motd = True

    def run(self):
        global motd
        global maxTilt
        global maxG
        global timeResponse


        while motd:
            accel_data = sensor.get_accel_data(g=True)  # g = True returns
                                                        # values in g units
            gyro_data = sensor.get_gyro_data()
            temp = sensor.get_temp()

            GYRx = gyro_data['x']
            GYRy = gyro_data['y']
            GYRz = gyro_data['z']
            ACCx = accel_data['x']
            ACCy = accel_data['y']
            ACCz = accel_data['z']
            TEMP = temp

            # Normalize accelerometer raw values
            # ACCr = math.sqrt(ACCx * ACCx + ACCy * ACCy + ACCz * ACCz)
            # GYRr = math.sqrt(GYRx * GYRx + GYRy * GYRy + GYRz * GYRz)


if __name__ == '__main__':
    motp = MotionPoller()
    try:
        motp.run()
        a = datetime.datetime.now()
        print "Starting..."
        while True:
            b = datetime.datetime.now() - a
            if b.total_seconds() >= sendRate:

                sys.stdout.write("\n\nAccelerometer Data [g]")
                sys.stdout.write("x: " + str(ACCx))
                sys.stdout.write("y: " + str(ACCy))
                sys.stdout.write("z: " + str(ACCz))

                sys.stdout.write("\nGyroscope Data")
                sys.stdout.write("x: " + str(GYRx))
                sys.stdout.write("y: " + str(GYRy))
                sys.stdout.write("z: " + str(GYRz))

                sys.stdout.write("\nTemp [C]: " + str(TEMP) + " C")

                sys.stdout.write("\n--------------------------")
            a = datetime.datetime.now()


    except(KeyboardInterrupt, SystemExit):
        print "\nKilling Threads..."
        motd = False
