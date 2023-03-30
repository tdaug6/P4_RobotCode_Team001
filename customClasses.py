#!/usr/bin/env python3
from ev3dev2.wheel import *
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
import math
import os

os.system('setfont Lat15-TerminusBold32x16')


"""
This class adds a custom wheel size that matches the size of the wheel on our APR.
The diameter is 56mm and the width is 28mm.
"""
class EV3CustomWheel(Wheel):
    def __init__(self):
        Wheel.__init__(self,56,28)
    # This calculates the circumference of the wheel based on the diameter (56mm)
    # There are a couple of changes made to the basic circumference equation
    #       1. 56 is in mm, so /10 is used to turn convert it to cm
    #       2. The distance was slightly too short, so a percentage was used to adjust this value
    #               Through trial and error 0.985 was determined to be the ideal percentage
    Wheel_Circumference = 56/10*math.pi*.985
    
    # Ticks_per_CM is used to get the rotations in another function
    Ticks_per_CM = 360.0/Wheel_Circumference


"""
The custom classes for A and D initialize the port to either A or D.
This makes the rest of the code cleaner.
"""
class CustomMotorA(Motor):
    def __init__(self):
        Motor.__init__(self,OUTPUT_A)

class CustomMotorD(Motor):
    def __init__(self):
        Motor.__init__(self,OUTPUT_D)


"""
APR_Location 

A class designed to track the APR's position at all times
Contains functions that both move the APR and record its position

"""
class APR_Location():
    m_x_pos = 0
    m_y_pos = 0
    m_heading = 0
    m_motorL = CustomMotorA()
    m_motorR = CustomMotorD()
    m_GYRO = GyroSensor(INPUT_4)
    m_driveTire = EV3CustomWheel
    m_distance_from_center_to_tire = 36.115625

    """
    calibrateGyro calibrates the Gyro sensor and sets its rotation to 0
    Use only once in program
    """
    def calibrateGyro(self):
        self.m_GYRO.calibrate()
        self.m_GYRO.reset()

    """
    CalculateDistance

    This calculates the distance between two points

    Inputs: x1: The x coordinate of the first point
            y1: The y coordinate of the first point
            x2: The x coordinate of the second point
            y2: The y coordinate of the second point

    Output: The distance between the two points
    """
    def CalculateDistance(self, x1,y1,x2,y2):
        return(math.sqrt((x2-x1)**2+(y2-y1)**2))
    
    """
    Calculate Angle

    This calculates the heading the APR needs to have to face the target point

    Inputs: x1: The x coordinate of the first point
            y1: The y coordinate of the first point
            x2: The x coordinate of the second point
            y2: The y coordinate of the second point

    Output: The heading the APR needs to have to face the target point
    """
    def CalculateAngle(self,x1,y1,x2,y2):
        yDifference = y2-y1
        xDifference = x2-x1
        if xDifference == 0:
            if y2>y1:
                return 0
            return 180
        if yDifference == 0:
            if x2>x1:
                return 90
            return -90
        return math.atan(yDifference/xDifference)
    
    """
    CalculateMotorPosition returns the motor rotation value based on the distance given
    Recieves input for distance (in cm) and wheel (used to access its ticks per inches)
    """
    def CalculateMotorPosition(self, distance):
        return distance * self.m_driveTire.Ticks_per_CM

    """
    TurnToAngle turns to the inputted angle
    The initial turn is at 10 speed to the right
    The secondary turn is at 5 speed to the left
    The angle of the gyro sensor is printed to the screen
    """
    def TurnToAngle(self,angle):
        time.sleep(.1)  #Prepare to turn
        INITIAL_TURN_SPEED = 10
        CORRECTION_TURN_SPEED = 5

        #Turn left while the angle is less than the inputted angle
        while self.m_GYRO.angle<angle:
            self.m_motorL.on(INITIAL_TURN_SPEED)
            self.m_motorR.on(-INITIAL_TURN_SPEED)

        #Stop the motors to get more accurate results
        self.m_motorL.stop()
        self.m_motorR.stop()
        time.sleep(0.25)

        #Turn right while the angle is greater than the inputted angle
        while self.m_GYRO.angle>angle:
            self.m_motorL.on(-CORRECTION_TURN_SPEED)
            self.m_motorR.on(CORRECTION_TURN_SPEED)

        #Stop the motors to get more accurate results
        self.m_motorL.stop()
        self.m_motorR.stop()
        time.sleep(.1)
        """
        #Display the gyro's angle to the screen
        print("{0:.2f} degrees".format(self.m_GYRO.angle))
        """
    
    """
    moveDistance moves the APR a given distance at a specified speed.
    Distance is measured in cm and speed is a percentage out of 100.

    This function is designed to correct the APR's x orientation based on the gyro sensor's angle.
    The motor rotation count of the left motor is printed to the screen for debugging purposes.
    """
    def moveDistance(self, DISTANCE,SPEED):
        DISTANCE_ROTATION = self.CalculateMotorPosition(DISTANCE)    #This is the number of ticks to the motor must rotate to reach the distance

        # Prepare updater variables to enter loop
        motorLOffset = self.m_motorL.position
        motorROffset = self.m_motorR.position
        motorLPosition = self.m_motorL.position - motorLOffset
        motorRPosition = self.m_motorR.position - motorROffset

        gyroAngleOffset = self.m_GYRO.angle
        gyroAngle = self.m_GYRO.angle - gyroAngleOffset


        # Loop until the distance has been reached
        while abs(motorLPosition) < DISTANCE_ROTATION and abs(motorRPosition) < DISTANCE_ROTATION:
            # Reset motor speeds to the inputted speed
            motorLSpeed = SPEED
            motorRSpeed = SPEED

            # Update accessor variables
            gyroAngle = self.m_GYRO.angle  #Negative when turning left, positive when turning right
            motorLPosition = self.m_motorL.position - motorLOffset
            motorRPosition = self.m_motorR.position - motorROffset

            # Adjust motor speed by the gyro's angle
            motorLSpeed -= gyroAngle - gyroAngleOffset
            motorRSpeed += gyroAngle - gyroAngleOffset

            # Disallow speeds larger than the given speed
            if motorLSpeed>SPEED:
                motorLSpeed = SPEED
            if motorLSpeed < -SPEED:
                motorLSpeed = -SPEED

            if motorRSpeed>SPEED:
                motorRSpeed = SPEED
            if motorRSpeed < -SPEED:
                motorRSpeed = -SPEED

            # Set motors to calculated speed
            self.m_motorL.on(motorLSpeed)
            self.m_motorR.on(motorRSpeed)

            # for debugging
            #print("{0:.2f} P=".format(motorLPosition))
            #time.sleep(0.001)

        #End
        self.m_motorL.stop()
        self.m_motorR.stop()

        # Update the position variables based on the orientaiton of the APR
        if self.m_GYRO.angle <10 and self.m_GYRO.angle>-10:
            self.m_y_pos += DISTANCE

        elif self.m_GYRO.angle <100 and self.m_GYRO.angle>80:
            self.m_x_pos += DISTANCE

        elif self.m_GYRO.angle<190 and self.m_GYRO.angle>170:
            self.m_y_pos -= DISTANCE

        else:
            self.m_x_pos -= DISTANCE

    """
    DriveToPoint

    Makes the APR drive to a specific point

    Inputs: A target x coordinate
            A target y coordinate
    
    Outputs: The APR drives to the point
    """
    def DriveToPoint(self, x,y):
        SPEED = 50

        # Turn towards the point
        angle = self.CalculateAngle(self.m_x_pos, self.m_y_pos, x, y)
        print("{0:.2f} degrees".format(angle))
        self.TurnToAngle(angle)

        # Drive to the point
        distance = self.CalculateDistance(self.m_x_pos, self.m_y_pos, x, y)
        self.moveDistance(distance, SPEED)

