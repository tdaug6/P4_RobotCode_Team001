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

