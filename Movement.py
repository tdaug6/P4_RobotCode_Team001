#!usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.wheel import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
import ev3dev2.auto as ev3
from customClasses import *
import time
import os
os.system('setfont Lat15-TerminusBold32x16')

#Create motors
motorL = LargeMotor(OUTPUT_A)
motorR = LargeMotor(OUTPUT_D)

#Create custom wheel to match wheel size
driveTire = EV3CustomWheel

#This is the distance from the center of the APR to the center of the wheel
distance_from_center_to_tire = 36.115625

#Create gyro sensor
gyro = GyroSensor(INPUT_4)

#Create a drivebase for odometry
mdiff = MoveDifferential(OUTPUT_A, OUTPUT_D, driveTire, distance_from_center_to_tire)

"""
movestraight moves the robot straight in the specified direction for the specified distance
TravelDistance is measured in centimeters
True = forward
False = Reverse
"""
def moveStraight(TravelDistance,direction):
    TravelDistance = TravelDistance*10 + 3.175  #Convert cm to mm
    mdiff.odometry_start()    #Start odometry.  DO NOT REMOVE

    travel_speed = 30   #Set the robot's speed OG=30

    #If the direction is forward, move forward for the specified distance
    if(direction):
        mdiff.on_for_distance(travel_speed,TravelDistance)
    
    #Otherwise, the direction is reverse, move in reverse for the specified distance
    else:
        mdiff.on_for_distance(-travel_speed,TravelDistance)

    mdiff.odometry_stop() #End odometry       DO NOT REMOVE


"""
calibrateGyro calibrates the Gyro sensor and sets its rotation to 0
Use only once in program
"""
def calibrateGyro():
    gyro.calibrate()
    gyro.reset()


"""
TurnToAngle turns to the inputted angle
The initial turn is at 10 speed to the right
The secondary turn is at 5 speed to the left
The angle of the gyro sensor is printed to the screen
"""
def turnToAngle(angle):
    time.sleep(.1)  #Prepare to turn

    #Turn left while the angle is less than the inputted angle
    while gyro.angle<angle:
        motorL.on(10)
        motorR.on(-10)

    #Stop the motors to get more accurate results
    motorL.stop()
    motorR.stop()
    time.sleep(0.25)

    #Turn right while the angle is greater than the inputted angle
    while gyro.angle>angle:
        motorL.on(-5)
        motorR.on(5)

    #Stop the motors to get more accurate results
    motorL.stop()
    motorR.stop()
    time.sleep(.1)
    """
    #Display the gyro's angle to the screen
    print("{0:.2f} degrees".format(gyro.angle))
    """