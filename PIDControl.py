#!/usr/bin/env python3
import time
from ev3dev2.motor import *
import Movement
from ev3dev2.sensor import*
from ev3dev2.sensor.lego import*
import math
from customWheel import *

# DO NOT USE #
#This file is a work in progress
#   do not edit, do not use
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
        error = target - current
        self.sumError += error
        result = self.kP*error + self.kI*self.sumError
        self.settled = self.checkSettled()
        return result
    


def moveDistance(TravelDistance,TravelSpeed,HeadingCorrentAngle):
    TravelDistance = TravelDistance * ((5.6*math.pi)/360)
    motorL = CustomMotorA()
    motorR = CustomMotorD()
    gyro = GyroSensor

    driveLPID = pid(20,0,0)
    driveRPID = pid(20,0,0)
    headingPID = pid(0,0,0)


    while not(driveLPID.settled) and not(headingPID.settled) and not(driveRPID.settled):
        driveLPos = float (motorL.position)
        driveRPos = float (motorR.position)
        headingAng = gyro.angle

        driveL = driveLPID.iterate(TravelDistance,driveLPos)
        driveR = driveRPID.iterate(TravelDistance,driveRPos)
        heading = headingPID.iterate(HeadingCorrentAngle,headingAng)
        time.sleep(0.001)
        if driveL>TravelSpeed:
            driveL = TravelSpeed
        if driveR>TravelSpeed:
            driveR = TravelSpeed
        motorL.on(driveL+heading)
        motorR.on(driveR+heading)

    
moveDistance(50,50,0)

