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
def Subtask2_FD(APR,x_initial,y_initial):
    # Target location values
    transition_y_pos = 8.5*2.54 #PLACEHOLDER VALUE, UPDATE TO CORRECT
    FulfillmentA_x_pos = 0 #PLACEHOLDER VALUE, UPDATE TO CORRECT
    FulfillmentA_y_pos = 3*2.54 #PLACEHOLDER VALUE, UPDATE TO CORRECT

    # Drive from center B to A
    #   Get into the hall from Center B
    APR.moveDistance(transition_y_pos)
    # APR.DriveToPoint(APR.m_x_pos, transition_y_pos)
    #   Drive down the hall to line up with center A
    APR.TurnToAngle(-90,False)
    APR.moveDistance(x_initial-FulfillmentA_x_pos-3*2.54)
    # APR.DriveToPoint(FulfillmentA_x_pos, APR.m_y_pos)
    #   Drive into centerA
    APR.TurnToAngle(-180,False)
    APR.moveDistance(transition_y_pos+y_initial-FulfillmentA_y_pos-0.5*2.54)
    # APR.DriveToPoint(FulfillmentA_x_pos, FulfillmentA_y_pos)

    #Turn to face towards the course        MAY NOT BE NEEDED
    APR.TurnToAngle(0,True)


#LIKELY INCORRECT VALUES
APR_X_INITIAL = 98*2.54
APR_Y_INITIAL = 5

MyRobot = APR_Location()
MyRobot.calibrateGyro()
Subtask2_FD(MyRobot, APR_X_INITIAL, APR_Y_INITIAL)