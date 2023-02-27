#!/usr/bin/env python3
from ev3dev2.wheel import *
from ev3dev2.motor import *

class EV3CustomWheel(Wheel):
    def __init__(self):
        Wheel.__init__(self,56,28)

##DO NOT USE##
class CustomMotorA(Motor):
    def __init__(self):
        Motor.__init__(self,OUTPUT_A)

class CustomMotorD(Motor):
    def __init__(self):
        Motor.__init__(self,OUTPUT_D)
