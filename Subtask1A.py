#!/usr/bin/env python3
from ev3dev2.motor import *
from Movement import *
import time

def Subtask1A(Laps, TravelDistance):
    for k in range(Laps):
        moveStraight(TravelDistance,True)
        time.sleep(3)
        moveStraight(TravelDistance,False)
        time.sleep(3)


Subtask1A(2,5)