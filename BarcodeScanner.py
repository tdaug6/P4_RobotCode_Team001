#!usr/bin/env python3
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
import ev3dev2.auto as ev3
import math
import Movement
import time
import os
os.system('setfont Lat15-TerminusBold32x16')

#Create Scanner
scanner = ColorSensor(INPUT_1)

#testing how color sensor works
print("{0:.2f}".format(scanner))