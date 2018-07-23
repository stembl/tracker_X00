# tracker_X00/print_gps.py

from gps import *
from time import sleep


def print_gps(n=60):
    """
    Pull data from GPS unit with gpsd.  Assumes gps
    unit is connected and running.
    Prints the UTC, Latitude, and Longitude
    every second for n seconds.

    Input
    -----
    Number of Prints

    Returns
    -------

    Examples
    --------
    >>> print_gps(3)
    UTC: 123.12, Latitude: 12.12345, Longitude: -12.12345
    UTC: 124.12, Latitude: 12.12345, Longitude: -12.12345
    UTC: 125.12, Latitude: 12.12345, Longitude: -12.12345
    """

    # try i is int, positive

    gpsd = gps(mode=WATCH_ENABLE)

    try:
        gpsd.latitude
    except:
        print('GPS not connected')
        exit()

    for i in range(n):
        gpsd.next()
        utc = gpsd.utc
        lat = gpsd.latitude
        lon = gpsd.longitude

        print('UTC: .2%f, Latitude: .5%f, Longitude: .5%f\n' %(utc, lat, lon))

        sleep(1)
