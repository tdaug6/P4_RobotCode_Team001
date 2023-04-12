#!/usr/bin/env python3
from ev3dev2.sensor import *
from ev3dev2.console import Console
from ev3dev2.sensor.lego import *
from ev3dev2.sound import Sound
from ev3dev2.display import *
from ev3dev2.motor import *
import time
from os import *
from APR_Location import *
from customClasses import *

MotorL = CustomMotorA
MotorR = CustomMotorD

#signify start
spkr = Sound()
#spkr.play_note("D4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)

"""
USAGE:

Stop the APR slightly before the scanner can read the barcode.

Assign a variable with Scanner() EX: "myScan = Scanner()"

After this line of code, the robot should mvoe forward slowly until it reaches the barcode.

At this point, it should beep, indicating it is reading the barcode.

Once the beeps end, the code for the barcode is saved to the variable.
"""

def Scanner():
    #prepare console for display
    console = Console()
    console.set_font(font='Lat15-TerminusBold24x12')
        
    #Create Scanner
    colorscan = ColorSensor(INPUT_1)
    myRobot = APR_Location()
    #testing how color sensor works

    bar1 = 0
    bar2 = 0
    bar3 = 0
    i = 0
    done = 0
    scan = 0

    spkr.play_note("G1", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
    while (scan == 0):
        scanner = colorscan.reflected_light_intensity
        myRobot.m_motorR.on(20)
        myRobot.m_motorL.on(20)
        if (scanner > 4 and scanner < 15):
            scan = 1

        

    while (done == 0):
        #spkr.play_note("F4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
        while (i < 3):
            scanner = colorscan.reflected_light_intensity
            time.sleep(.1)
            myRobot.moveDistance(.45*2.54, 10)
            if (i==0):
                bar1 = colorscan.reflected_light_intensity
                spkr.play_note("G3", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
            if (i == 1):
                bar2 = colorscan.reflected_light_intensity
                spkr.play_note("G3", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
            if (i == 2):
                bar3 = colorscan.reflected_light_intensity
                spkr.play_note("G3", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
                done = 1
            i = i + 1
            time.sleep(1)


    if (bar1 >= 17):
        if (bar2 >= 17):
            if (bar3 >= 17):
                code = "A"
            else:
                code = "D"
        else:
            code = "B"
    else:
        code = "C"
            
    #while True:
        #console.text_at("%0s"%(code), column=1, row=1, reset_console=False, alignment="L")

    return code

