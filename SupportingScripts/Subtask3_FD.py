#!/usr/bin/env python3
from ev3dev2.console import Console
from ev3dev2.sound import Sound
from ev3dev2.display import *
import time
from os import *
from ev3dev2.motor import *
from BarcodeScanner import *
from APR_Location import *
from WorkingLift import *
from customClasses import *

MotorL = CustomMotorA
MotorR = CustomMotorD

spkr = Sound()
spkr.play_note("D4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)

#prepare console for display
console = Console()
console.set_font(font='Lat15-TerminusBold24x12')

#--------------INPUT EXPECTED BAR CODE---------------#

expected = 1

#----------------------------------------------------#

#activation condition (once location reached)
#might have to place movement in here

#move to such that the barcode is very close to the furthest edge of the box.
#Too far is better than too short

myRobot = APR_Location()
myRobot.calibrateGyro()

container = Containers()
specificContainer = container.A1[0]

spkr.play_note("A2", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)


#activate scanner - might have to back up slightly
myRobot.moveDistance(14*2.54)
actual = Scanner()

spkr.play_note("B4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)

#compare scanner results to input and output
if (expected == actual):
    while (True):
        console.text_at("%0s"%("Match"), column=1, row=1, reset_console=False, alignment="L")
        console.text_at("%0s"%(actual), column=1, row=3, reset_console=False, alignment="L")
else:
    while (True):
        console.text_at("%0s"%("Doesn't Match"), column=1, row=1, reset_console=False, alignment="L")
        console.text_at("%0s"%(actual), column=1, row=3, reset_console=False, alignment="L")