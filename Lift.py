#!usr/bin/env python3

from ev3dev2.motor import *
from customClasses import *


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
        MAX_HEIGHT = 1000   #Experimental value...NOT FINAL
        SPEED = 30  # Percentage out of 100

        # Set the motor position holder to the true motor position
        self.m_lift_position = self.m_lift_motor.position

        # Loop until the motor's position reaches the desired height
        while self.m_lift_position < MAX_HEIGHT:
            self.m_lift_motor.on(SPEED) # Run the motor at the speed
            self.m_lift_position = self.m_lift_motor.position   # Update the motor position holder to the true motor position

        # Stop the motor so it doesn't continue to run
        self.m_lift_motor.stop()


    """
    LowerLift

    Lowers the lift to the maximum height

    INPUTS: None

    OUTPUTS: The lift at the minimum height
    """
    def LowerLift(self):
        MIN_HEIGHT = 0  #Experimental value...NOT FINAL
        SPEED = 30

        # Set the motor position holder to the true motor position
        self.m_lift_position = self.m_lift_motor.position

        # Loop until the motor's position reaches the desired height
        while self.m_lift_position > MIN_HEIGHT:
            self.m_lift_motor.on(-SPEED) # Run the motor at the speed
            self.m_lift_position = self.m_lift_motor.position   # Update the motor position holder to the true motor position

        # Stop the motor so it doesn't continue to run
        self.m_lift_motor.stop()