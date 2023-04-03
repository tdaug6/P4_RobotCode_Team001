#!/usr/bin/env python3
from ev3dev2.wheel import *
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
import math
import os

os.system('setfont Lat15-TerminusBold32x16')


"""
This class adds a custom wheel size that matches the size of the wheel on our APR.
The diameter is 56mm and the width is 28mm.
"""
class EV3CustomWheel(Wheel):
    def __init__(self):
        Wheel.__init__(self,56,28)
    # This calculates the circumference of the wheel based on the diameter (56mm)
    # There are a couple of changes made to the basic circumference equation
    #       1. 56 is in mm, so /10 is used to turn convert it to cm
    #       2. The distance was slightly too short, so a percentage was used to adjust this value
    #               Through trial and error 0.985 was determined to be the ideal percentage
    Wheel_Circumference = 56/10*math.pi*.985
    
    # Ticks_per_CM is used to get the rotations in another function
    Ticks_per_CM = 360.0/Wheel_Circumference


"""
The custom classes for A and D initialize the port to either A or D.
This makes the rest of the code cleaner.
"""
class CustomMotorA(Motor):
    def __init__(self):
        Motor.__init__(self,OUTPUT_A)

class CustomMotorD(Motor):
    def __init__(self):
        Motor.__init__(self,OUTPUT_D)

""""
LiftMotor

Create a custom motor for the lift
"""
class LiftMotor(Motor):
    def __init__(self):
        Motor.__init__(self,OUTPUT_B)
