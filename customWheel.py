#!/usr/bin/env python3
from ev3dev2.wheel import *

class EV3CustomWheel(Wheel):
    def __init__(self):
        Wheel.__init__(self,56,28)