from time import sleep
from mpu6050 import mpu6050

def print_accel():
    """
    Pull data from the MPU6050 and print the results.

    !!! add set gyro and g range !!!

    Input
    -----
    Number of Prints

    Returns
    -------

    Examples
    --------
    >>> print_gps(3)


    Accelerometer Data [g]
    x:
    y:
    z:

    Gyroscope Data
    x:
    y:
    z:

    Temp [C]: 20
    """


    sensor = mpu6050(0x68)

    while True:
        accel_data = sensor.get_accel_data(g=True)
        gyro_data = sensor.get_gyro_data()
        temp = sensor.get_temp()

        print("\n\nAccelerometer Data [g]")
        print("x: " + str(accel_data['x']))
        print("y: " + str(accel_data['y']))
        print("z: " + str(accel_data['z']))

        print("\nGyroscope Data")
        print("x: " + str(gyro_data['x']))
        print("y: " + str(gyro_data['y']))
        print("z: " + str(gyro_data['z']))

        print("\nTemp [C]: " + str(temp) + " C")
        sleep(0.5)
