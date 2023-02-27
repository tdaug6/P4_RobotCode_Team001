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


#------------------------------------------------------------------#
#               THIS IS FOR SUBTASK 1B

# This one goes forward, turns, and goes forward to starting position

laps = 4 #ENTER THE NUMBER OF LAPS HERE (1 lap = 1 forward, 1 turn, and 1 forward)
distance = 90 #ENTER THE DISTANCE TO TRAVEL HERE (IN CM)

Subtask1B(distance,laps)
#------------------------------------------------------------------#


