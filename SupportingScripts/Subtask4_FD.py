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

# Objects to access
MotorL = CustomMotorA
MotorR = CustomMotorD

myRobot = APR_Location()
myRobot.calibrateGyro()

container = Containers()
specificContainer = container.A1[0]


#Move Back and Turn in for container
myRobot.m_motorL.on(-20)
myRobot.m_motorR.on(-20)
time.sleep(1.3)
myRobot.m_motorL.stop()
myRobot.m_motorR.stop()
myRobot.HallTurn(True, specificContainer)
myRobot.m_motorL.on(15)
myRobot.m_motorR.on(15)
time.sleep(.25)
myRobot.m_motorL.stop()
myRobot.m_motorR.stop()


#Register lift & lift container
myLift = Lift()
myLift.RaiseLift()

#Turn out
time.sleep(.1)
myRobot.HallTurn(False, specificContainer)

#Move out
myRobot.moveDistance(27*2.54, 50)
time.sleep(.5)

#Lower Container
myLift.LowerLift()

#back out
myRobot.m_motorL.on(-30)
myRobot.m_motorR.on(-30)
time.sleep(1)
myRobot.m_motorL.stop()
myRobot.m_motorR.stop()
