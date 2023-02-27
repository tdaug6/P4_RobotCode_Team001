#!/usr/bin/env python3
from ev3dev2.wheel import *
from ev3dev2.motor import *

"""
This class adds a custom wheel size that matches the size of the wheel on our APR.
The diameter is 56mm and the width is 28mm.
"""
class EV3CustomWheel(Wheel):
    def __init__(self):
        Wheel.__init__(self,56,28)

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
