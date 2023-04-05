#!/usr/bin/env python3
from ev3dev2.console import Console
from ev3dev2.sound import Sound
from ev3dev2.display import *
import time
from os import *
from BarcodeScanner import *
from APR_Location import *

spkr = Sound()
spkr.play_note("D4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)

#prepare console for display
console = Console()
console.set_font(font='Lat15-TerminusBold24x12')

#--------------INPUT EXPECTED BAR CODE---------------#

expected = "B"

#----------------------------------------------------#

#activation condition (once location reached)
#might have to place movement in here

#move to such that the barcode is very close to the furthest edge of the box.
#Too far is better than too short

#myRobot = APR_Location()
#myRobot.calibrateGyro()

#activate scanner - might have to back up slightly
actual = Scanner()

spkr.play_note("B4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)


#compare scanner results to input and output
if (actual == expected):
    spkr.play_note("F4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
    while True:
        console.text_at("%0s"%("Match!"), column=1, row=1, reset_console=False, alignment="L")
else:
    spkr.play_note("E4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
    while True:
        console.text_at("%0s"%("Does Not Match!"), column=1, row=1, reset_console=False, alignment="L")
