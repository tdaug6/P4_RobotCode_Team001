#!/usr/bin/env python3
from ev3dev2.sensor import *
from ev3dev2.console import Console
from ev3dev2.sensor.lego import *
import ev3dev2.auto as ev3
from ev3dev2.sound import Sound
from ev3dev2.wheel import *
from ev3dev2.display import *
import math
import Movement
import time
from os import *
from PIDControl import *
from BarcodeScanner import *

#prepare console for display
console = Console()
console.set_font(font='Lat15-TerminusBold24x12')

#--------------INPUT EXPECTED BAR CODE---------------#

expected = ""

#----------------------------------------------------#

#activation condition (once location reached)
#might have to place movement in here

#move to such that the barcode is very close to the furthest edge of the box.
#Too far is better than too short

#activate scanner - might have to back up slightly
scanny = Scanner
actual = scanny.Scan()

#compare scanner results to input and output
if (actual == expected):
    while True:
        console.text_at("%0s"%("Match!"), column=1, row=1, reset_console=False, alignment="L")
else:
    while True:
        console.text_at("%0s"%("Does Not Match!"), column=1, row=1, reset_console=False, alignment="L")