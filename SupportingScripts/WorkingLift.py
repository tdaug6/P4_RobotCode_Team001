#!/usr/bin/env python3
from ev3dev2.sensor import *
from ev3dev2.console import Console
from ev3dev2.sensor.lego import *
from ev3dev2.wheel import *
import ev3dev2.auto as ev3
from ev3dev2.sound import Sound
from ev3dev2.display import *
from ev3dev2.motor import *
import math
import time
from os import *

#signify start
spkr = Sound()
spkr.play_note("D4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)

""""
LiftMotor

Create a custom motor for the lift
"""
class LiftMotor(Motor):
    def __init__(self):
        Motor.__init__(self,OUTPUT_B)

"""
Lift Class

Contains the necessary information and procedures for the Lift

VARIABLES:
    - Lift motor: contains a motor for the lift
    - Lift position: contains the position of the lift motor

FUNCTIONS:
    - Raise Lift: Raises the lift to the maximum height
    - Lower Lift: Lowers the lift to the minimum height
"""
class Lift():
    m_lift_motor = LiftMotor()
    m_lift_position = 0

    """
    RaiseLift

    Raises the lift to the maximum height

    INPUTS: None

    OUTPUTS: The lift at the maximum height
    """
    def RaiseLift(self):
        MAX_HEIGHT = 80   #Experimental value...NOT FINAL
        SPEED = 80  # Percentage out of 100

        # Set the motor position holder to the true motor position
        self.m_lift_position = self.m_lift_motor.position

        self.m_lift_motor.on(30)
        """
        # Loop until the motor's position reaches the desired height
        while self.m_lift_position < MAX_HEIGHT:
            self.m_lift_motor.on(SPEED) # Run the motor at the speed
            self.m_lift_position = self.m_lift_motor.position   # Update the motor position holder to the true motor position

        # Stop the motor so it doesn't continue to run
        self.m_lift_motor.stop()
        """
    """
    LowerLift

    Lowers the lift to the maximum height

    INPUTS: None

    OUTPUTS: The lift at the minimum height
    """
    def LowerLift(self):
        MIN_HEIGHT = 0  #Experimental value...NOT FINAL
        SPEED = 30

        self.m_lift_motor.on(-30)
        time.sleep(0.2)
        self.m_lift_motor.stop()
        """
        # Set the motor position holder to the true motor position
        self.m_lift_position = self.m_lift_motor.position

        # Loop until the motor's position reaches the desired height
        while self.m_lift_position > MIN_HEIGHT:
            self.m_lift_motor.on(-SPEED) # Run the motor at the speed
            self.m_lift_position = self.m_lift_motor.position   # Update the motor position holder to the true motor position

        # Stop the motor so it doesn't continue to run
        self.m_lift_motor.stop()
        """
"""
Example Command
"""
i=0
liftarm = Lift()
while True: 
    if i<1: #replace with location condition
        liftarm.RaiseLift()
        time.sleep(5)
        i = i+1
    else:
        break

liftarm.LowerLift()



