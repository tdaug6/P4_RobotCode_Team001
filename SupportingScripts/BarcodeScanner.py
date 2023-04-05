#!/usr/bin/env python3
from ev3dev2.sensor import *
from ev3dev2.console import Console
from ev3dev2.sensor.lego import *
import ev3dev2.auto as ev3
from ev3dev2.sound import Sound
from ev3dev2.display import *
import math
import time
from os import *

#signify start
spkr = Sound()
spkr.play_note("D4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
def Scanner():
    #prepare console for display
    console = Console()
    console.set_font(font='Lat15-TerminusBold24x12')
        
    #Create Scanner
    colorscan = ColorSensor(INPUT_1)

    #testing how color sensor works

    bar1 = 0
    bar2 = 0
    bar3 = 0
    i = 0
    done = 0
    while (done == 0):
        scanner = colorscan.reflected_light_intensity
        #print("{0:.0f}".format(scanner))
        #console.text_at("", column=1, row=1, reset_console=True, alignment="L")
        time.sleep(.1)
                    
        if (scanner > 3 and scanner < 12):
            spkr.play_note("F4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
            time.sleep(2)
            while (i < 3):
                scanner = colorscan.reflected_light_intensity
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


    if (bar1 >= 20):
        if (bar2 >= 20):
            if (bar3 >= 20):
                code = "A"
            else:
                code = "D"
        else:
            code = "B"
    else:
        code = "C"
            
#    while True:
#        console.text_at("%0s"%(code), column=1, row=1, reset_console=False, alignment="L")

    return code