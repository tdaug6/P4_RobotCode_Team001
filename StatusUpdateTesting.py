#!/usr/bin/env python3
from customClasses import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *

APR = APR_Location()
APR.calibrateGyro()
time.sleep(2)
x_coordinate = 0
y_coordinate = 5

APR.DriveToPoint(x_coordinate, y_coordinate)

x_coordinate = -5
y_coordinate = 5

APR.DriveToPoint(x_coordinate, y_coordinate)