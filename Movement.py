#!usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.wheel import *
from customWheel import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
import ev3dev2.auto as ev3
import time
import os
os.system('setfont Lat15-TerminusBold32x16')

#Create motors
motorL = LargeMotor(OUTPUT_A)
motorR = LargeMotor(OUTPUT_D)

#Create custom wheel to match wheel size
Wheel_height = 56
Wheel_width = 28
driveTire = EV3CustomWheel

distance_from_center_to_tire = 36.115625

gyro = GyroSensor(INPUT_4)

#Create a drivebase for odometry
mdiff = MoveDifferential(OUTPUT_A, OUTPUT_D, driveTire, distance_from_center_to_tire)

"""
movestraight moves the robot straight in the specified direction for the specified distance
TravelDistance is measured in inches
True = forward
False = Reverse
"""

def moveStraight(TravelDistance,direction):
    TravelDistance = TravelDistance*10 + 3.175  #Convert inches to mm   CHANGE CONVERSION FROM CM TO MM
    mdiff.odometry_start()    #Start odometry. DO NOT REMOVE

    travel_speed = 30   #Set the robot's speed OG=30

    #If the direction is forward, move forward for the specified distance
    if(direction):
        mdiff.on_for_distance(travel_speed,TravelDistance)
    
    #Otherwise, the direction is reverse, move in reverse for the specified distance
    else:
        mdiff.on_for_distance(-travel_speed,TravelDistance)

    mdiff.odometry_stop() #End odometry       DO NOT REMOVE

def calibrateGyro():
    gyro.calibrate()
    gyro.reset()

def turnToAngle(angle):
    time.sleep(.1)
    while gyro.angle<angle:
        motorL.on(10)
        motorR.on(-10)
    motorL.stop()
    motorR.stop()
    time.sleep(0.25)
    while gyro.angle>angle:
        motorL.on(-5)
        motorR.on(5)
    motorL.stop()
    motorR.stop()
    time.sleep(.1)
    print("{0:.2f} degrees".format(gyro.angle))

    





