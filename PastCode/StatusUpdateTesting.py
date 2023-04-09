#!/usr/bin/env python3
from customClasses import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *

# Prepare the script
APR = APR_Location()
APR.calibrateGyro()
time.sleep(2)

#------------------------------------------------------------------#
#               INPUTS FOR STATUS UPDATE TESTING

# This program will drive to the given points

x_coordinate1 = 0    # X-Coordinate for first point in cm
y_coordinate1 = 10   # Y-Coordinate for first point in cm

x_coordinate2 = -10  # X-Coordinate for second point in cm
y_coordinate2 = 10   # Y-Coordinate for second point in cm

#------------------------------------------------------------------#

# Drive to the point
APR.DriveToPoint(x_coordinate1, y_coordinate1)
APR.DriveToPoint(x_coordinate2, y_coordinate2)