#!/usr/bin/env python3
from APR_Location import *
from globals import *
import time

#
# Subtask2_FD
#
# This is the code to complete subtask 2 of the final demo
#
# Inputs:   An APR storage variable to track the robot's location and movment functions
# Outpus:   The APR moves to Fulfillment Center A from B
def Subtask2_FD(APR):
    # Target location values
    transition_y_pos = 5 #PLACEHOLDER VALUE, UPDATE TO CORRECT
    FulfillmentA_x_pos = 0 #PLACEHOLDER VALUE, UPDATE TO CORRECT
    FulfillmentA_y_pos = 0 #PLACEHOLDER VALUE, UPDATE TO CORRECT

    # Drive from center B to A
    #   Get into the hall from Center B
    APR.DriveToPoint(APR.m_x_pos, transition_y_pos)
    #   Drive down the hall to line up with center A
    APR.DriveToPoint(FulfillmentA_x_pos, APR.m_y_pos)
    #   Drive into centerA
    APR.DriveToPoint(FulfillmentA_x_pos, FulfillmentA_y_pos)

    #Turn to face towards the course        MAY NOT BE NEEDED
    APR.TurnToAngle(0)


#LIKELY INCORRECT VALUES
APR_X_INITIAL = 100
APR_Y_INITIAL = 0

MyRobot = APR_Location(APR_X_INITIAL, APR_Y_INITIAL)
Subtask2_FD(MyRobot)