#!/usr/bin/env python3
import time
from ev3dev2.motor import *
from Movement import *
from ev3dev2.sensor import*
from ev3dev2.sensor.lego import*
import math
from customClasses import *

# DO NOT USE #
#This file is a work in progress
#   do not edit, do not use
"""
class pid:
    kP = 0
    kI  = 0
    kD = 0

    settled = False

    sumError = 0
    prevError = 0

    def __init__(self, p, i, d):
        self.kP = p
        self.kI = i
        self.kD = d

    def checkSettled(self):
        return False
    
    def iterate(self,target,current):
        error = current - target
        self.sumError += error
        result = self.kP*error + self.kI*self.sumError
        self.settled = self.checkSettled()
        return result
    


def moveDistance(TravelDistance,TravelSpeed,HeadingCurrentAngle):
    TravelDistance = TravelDistance * ((5.6*math.pi)/360)
    motorL = CustomMotorA()
    motorR = CustomMotorD()
    gyro = GyroSensor()

    driveLPID = pid(1,0,0)
    driveRPID = pid(1,0,0)
    headingPID = pid(1,0,0)


    while not(driveLPID.settled) and not(headingPID.settled) and not(driveRPID.settled):
        driveLPos = motorL.position *1
        driveRPos = motorR.position*1
        headingAng = gyro.angle

        driveL = driveLPID.iterate(TravelDistance,driveLPos)
        driveR = driveRPID.iterate(TravelDistance,driveRPos)
        heading = headingPID.iterate(HeadingCurrentAngle,headingAng)
        time.sleep(0.001)
        #if abs(driveL+heading)>TravelSpeed:
        #    driveL = TravelSpeed-heading
        #if abs(driveR+heading)>TravelSpeed:
        #    driveR = TravelSpeed-heading
        leftSpeed = max(min(driveL+heading,TravelSpeed),-TravelSpeed)
        rightSpeed = max(min(driveR+heading,TravelSpeed),-TravelSpeed)
        print("{0:.2f} R speed".format(rightSpeed))
        #print("{0:.2f} L speed".format(driveL+heading))
        #motorL.on(driveL+heading)
        #motorR.on(driveR+heading)
        time.sleep(.1)

    
moveDistance(50,50,0)

"""

# vvvvvvvv THIS IS FUNCTIONAL CODE vvvvvvvv
"""
moveDistance moves the APR a given distance at a specified speed.
Distance is measured in cm and speed is a percentage out of 100.

This function is designed to correct the APR's x orientation based on the gyro sensor's angle.
The motor rotation count of the left motor is printed to the screen for debugging purposes.
"""
def moveDistance(DISTANCE,SPEED):
    # Declare objects
    newWheel = EV3CustomWheel()
    motorL = CustomMotorA()
    motorR = CustomMotorD()
    
    # Initialize Constants
    DISTANCE_ROTATION = DriveDistance(DISTANCE,newWheel)    #This is the number of ticks to the motor must rotate to reach the distance

    # Prepare updater variables to enter loop
    motorLOffset = motorL.position
    motorROffset = motorR.position
    motorLPosition = motorL.position - motorLOffset
    motorRPosition = motorR.position - motorROffset

    gyroAngleOffset = GYRO.angle
    gyroAngle = GYRO.angle - gyroAngleOffset


    # Loop until the distance has been reached
    while abs(motorLPosition) < DISTANCE_ROTATION and abs(motorRPosition) < DISTANCE_ROTATION:
        # Reset motor speeds to the inputted speed
        motorLSpeed = SPEED
        motorRSpeed = SPEED

        # Update accessor variables
        gyroAngle = GYRO.angle  #Negative when turning left, positive when turning right
        motorLPosition = motorL.position - motorLOffset
        motorRPosition = motorR.position - motorROffset

        # Adjust motor speed by the gyro's angle
        motorLSpeed -= gyroAngle - gyroAngleOffset
        motorRSpeed += gyroAngle - gyroAngleOffset

        # Disallow speeds larger than the given speed
        if motorLSpeed>SPEED:
            motorLSpeed = SPEED
        if motorLSpeed < -SPEED:
            motorLSpeed = -SPEED

        if motorRSpeed>SPEED:
            motorRSpeed = SPEED
        if motorRSpeed < -SPEED:
            motorRSpeed = -SPEED

        # Set motors to calculated speed
        motorL.on(motorLSpeed)
        motorR.on(motorRSpeed)

        # for debugging
        print("{0:.2f} P=".format(motorLPosition))
        time.sleep(0.001)

    #End
    motorL.stop()
    motorR.stop()



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
