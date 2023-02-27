#!/usr/bin/env python3
from ev3dev2.motor import *
from Movement import *
import time

"""
Subtask1A is the complete code for the demo Subtask 1A.
It takes inputs for laps and travel distance (cm).
This program will go forward and go in reverse.
"""
def Subtask1A(Laps, TravelDistance):
    #For the number of laps...
    for k in range(Laps):
        #Move forward
        moveStraight(TravelDistance,True)
        time.sleep(1)
        #Move in reverse
        moveStraight(TravelDistance,False)
        time.sleep(1)



#------------------------------------------------------------------#
#               THIS IS FOR SUBTASK 1A

# This one goes forward, then reverse

laps = 3 #ENTER THE NUMBER OF LAPS HERE (1 lap = 1 forward and 1 back)
distance = 120 #ENTER THE DISTANCE TO TRAVEL HERE (IN CM)

Subtask1A(laps,distance)
#------------------------------------------------------------------#
