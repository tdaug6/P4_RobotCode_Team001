#!usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.wheel import *
from customWheel import *

Wheel_height = 56
Wheel_width = 28

driveTire = EV3CustomWheel

distance_from_center_to_tire = 36.115625

mdiff = MoveDifferential(OUTPUT_A, OUTPUT_D, driveTire, distance_from_center_to_tire)

def moveStraight(TravelDistance,direction):
    TravelDistance = TravelDistance * 25.4 + 3.175
    mdiff.odometry_start
    travel_speed = 30
    if(direction):
        mdiff.on_for_distance(travel_speed,TravelDistance)
    else:
        mdiff.on_for_distance(-travel_speed,TravelDistance)
    mdiff.odometry_stop