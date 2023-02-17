#!usr/bin/env python3
from ev3dev2.motor import *
#,
def move(TravelDistance,direction):
    if(direction):
        on_for_distance(TravelDistance)