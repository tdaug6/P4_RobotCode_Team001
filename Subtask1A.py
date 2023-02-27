#!/usr/bin/env python3
from ev3dev2.motor import *
from Movement import *
import time

def Subtask1A(Laps, TravelDistance):
    for k in range(Laps):
        moveStraight(TravelDistance,True)
        time.sleep(1)
        moveStraight(TravelDistance,False)
        time.sleep(1)



#------------------------------------------------------------------#
#               THIS IS FOR SUBTASK 1A

# This one goes forward, then reverse

laps = 3 #ENTER THE NUMBER OF LAPS HERE (1 lap = 1 forward and 1 back)
distance = 120 #ENTER THE DISTANCE TO TRAVEL HERE (IN CM)

Subtask1A(laps,distance)
#------------------------------------------------------------------#
