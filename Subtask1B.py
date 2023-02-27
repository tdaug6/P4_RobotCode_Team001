#!/usr/bin/env python3

from ev3dev2.motor import *
from Movement import *
import time
from ev3dev2.sensor import *

"""
Subtask1B is the complete code for the demo Subtask 1B.
It takes inputs for the number of laps and travel distance (cm).
This program will go forward, turn, and come back.
"""
def Subtask1B(TravelDistance,Laps):
    #Calibrate the gyro sensor
    calibrateGyro()
    time.sleep(2)
    i = 0
    #While the number of laps is not complete...
    while i<Laps*2:     #Must be *2 because this only accounts for the first half of the movement
        #Move forward for the travel distance
        moveStraight(TravelDistance,True)
        #Turn 180 degrees
        turnToAngle(180 + i*180)
        i+=1    #increment counter variable
        time.sleep(1)


#------------------------------------------------------------------#
#               THIS IS FOR SUBTASK 1B

# This one goes forward, turns, and goes forward to starting position

laps = 4 #ENTER THE NUMBER OF LAPS HERE (1 lap = 1 forward, 1 turn, and 1 forward)
distance = 90 #ENTER THE DISTANCE TO TRAVEL HERE (IN CM)

Subtask1B(distance,laps)
#------------------------------------------------------------------#


