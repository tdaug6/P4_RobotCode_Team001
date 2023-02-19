#!/usr/bin/env python3

from ev3dev2.motor import *
from Movement import *
import time
from ev3dev2.sensor import *



def Subtask1B(TravelDistance,Laps):
    calibrateGyro()
    time.sleep(2)
    i = 0
    while i<Laps*2:
        moveStraight(TravelDistance,True)
        turnToAngle(180 + i*180)
        i+=1
        time.sleep(1)

Subtask1B(200,2)

