#!/usr/bin/env python3
from APR_Location import *
from globals import *
import time

#
# Subtask1_FD
#
# This is the code to complete subtask 1 for the final demo
#
# Inputs:   An APR to update the position of and call the movement functions for
#           A container ocation to access the x and y components of the container to drive to
#           A container class to access the distance between the robot center and container center
# Outputs:  The APR drives to the specific location
def Subtask1_FD(APR,containerLocation, targetLocation):
    # Determine target values
    container_y_pos = containerLocation[1]
    container_x_pos = containerLocation[0]-6*2.54
    fulfillmentB_x_pos = 97 * 2.54     #INCORRECT VALUES
    fulfillmentB_y_pos = 15*2.54      #INCORRECT VALUES

    # Drive to the container
    APR.moveDistance(container_y_pos-15)     # First, move up to the correct row
    APR.TurnToAngle(90,True)
    APR.moveDistance(container_x_pos)
    #APR.DriveToPoint(container_x_pos, container_y_pos)    # Then, move down the row to the correct container

    # Wait 5 seconds
    time.sleep(5)

    # Drive to the container
    APR.moveDistance(fulfillmentB_x_pos-container_x_pos-2*2.54)
    APR.TurnToAngle(180,True)
    APR.moveDistance(container_y_pos - fulfillmentB_y_pos+20+1*2.54)
    # APR.DriveToPoint(fulfillmentB_x_pos, container_y_pos)     # drive to the end of the row
    # APR.DriveToPoint(fulfillmentB_x_pos, fulfillmentB_y_pos)     # drive to the end of the row

    APR.TurnToAngle(0,False)

    
# Important variables for function call
MyRobot = APR_Location()    # Used for position tracking and movement
MyRobot.calibrateGyro()
AllContainers = Containers()    # Used for container location and measurements

#------------------------------------------------------------#
#                       SUBTASK 1                            #

CONTAINER_NUMBER = 11    #Enter the container number, the program will automatically subtract one from the inputted value

#------------------------------------------------------------#

# Set the inputted number as a container in A1
TargetContainer = AllContainers.A1[CONTAINER_NUMBER-1]
TrueTarget = TargetContainer
TargetContainer[1] += 10
TargetContainer[0] += 10

# Function call
Subtask1_FD(MyRobot, TargetContainer, TrueTarget)