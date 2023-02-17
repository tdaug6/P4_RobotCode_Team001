#!usr/bin/env python3
from ev3dev2.motor import *

def SubTask1A(Laps, TravelDistance):
    for k in range(Laps):
        moveStraight(TravelDistance,True)
        moveStraight(TravelDistance,False)