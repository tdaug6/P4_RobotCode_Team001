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

expected = "B"

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
actual = Scanner()

spkr.play_note("B4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)


#compare scanner results to input and output
if (actual == expected):
    spkr.play_note("F4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
    console.text_at("%0s"%("Match!"), column=1, row=1, reset_console=False, alignment="L")
else:
    spkr.play_note("E4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
    console.text_at("%0s"%("Does Not Match!"), column=1, row=1, reset_console=False, alignment="L")

#Move Back and Turn in for container
myRobot.m_motorL.on(-20)
myRobot.m_motorR.on(-20)
time.sleep(1.3)
myRobot.m_motorL.stop()
myRobot.m_motorR.stop()
myRobot.HallTurn(True, specificContainer)
myRobot.m_motorL.on(10)
myRobot.m_motorR.on(10)
time.sleep(.1)
myRobot.m_motorL.stop()
myRobot.m_motorR.stop()


#Register lift & lift container
myLift = Lift()
myLift.RaiseLift()

#Turn out
time.sleep(.1)
myRobot.HallTurn(False, specificContainer)

#Move out
myRobot.moveDistance(24*2.54, 50)
time.sleep(.5)

#Lower Container
myLift.LowerLift()

#back out
myRobot.m_motorL.on(-30)
myRobot.m_motorR.on(-30)
time.sleep(.5)
myRobot.m_motorL.stop()
myRobot.m_motorR.stop()

#Keep displays running
if (actual == expected):
    while True:
        console.text_at("%0s"%("Match!"), column=1, row=1, reset_console=False, alignment="L")
else:
    while True:
        console.text_at("%0s"%("Does Not Match!"), column=1, row=1, reset_console=False, alignment="L")
