#!usr/bin/env python3
from ev3dev2.motor import *

m1 = Motor(OUTPUT_A)

m1.on_for_seconds(SpeedPercent(100),5)