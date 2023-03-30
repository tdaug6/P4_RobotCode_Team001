#!/usr/bin/env python3
import time
from ev3dev2.motor import *
from Movement import *
from ev3dev2.sensor import*
from ev3dev2.sensor.lego import*
from customClasses import *
from PIDControl import *


# Prepare gyro for program
GYRO = GyroSensor()
GYRO.reset()
GYRO.calibrate()
time.sleep(2)       # Ensure gyro is calibrated

"""
#------------------------------------------------------------------#
#           THIS IS FOR MID-PROJECT REVIEW TESTING MOVEMENT

# This one goes forward for specified inches

distanceInInches = 84   #This stores the distance in INCHES for the travel distance
movementSpeed = 50      # This stores the speed for the APR

dist = distanceInInches * 2.54  #converts inches to cm

moveDistance(dist,movementSpeed)    #Function call using inputs
time.sleep(0.1)
#------------------------------------------------------------------#
"""


#------------------------------------------------------------------#
#           THIS IS FOR MID-PROJECT REVIEW TESTING TURNING

# This one goes forward for specified inches

distanceInInches = 12   #This stores the distance in INCHES for the travel distance
movementSpeed = 50      # This stores the speed for the APR

dist = distanceInInches * 2.54  #converts inches to cm

moveDistance(12*2.54,movementSpeed)    #Move 12 inches
turnToAngle(90)     # Turn 90 degrees
moveDistance(dist,movementSpeed)    #Function call using inputs
time.sleep(0.1)
#------------------------------------------------------------------#
