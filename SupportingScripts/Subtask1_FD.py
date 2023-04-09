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
def Subtask1_FD(APR,containerLocation, Container):
    # Determine target values
    container_y_pos = Container.DISTANCE_BETWEEN_CENTERS + containerLocation[1]
    container_x_pos = containerLocation[0]
    fulfillmentB_x_pos = 60     #INCORRECT VALUES
    fulfillmentB_y_pos = 0      #INCORRECT VALUES

    # Drive to the container
    APR.DriveToPoint(APR.m_x_pos, container_y_pos)     # First, move up to the correct row
    APR.DriveToPoint(container_x_pos, container_y_pos)    # Then, move down the row to the correct container

    # Wait 5 seconds
    time.sleep(5)

    # Drive to the container
    APR.DriveToPoint(fulfillmentB_x_pos, container_y_pos)     # drive to the end of the row
    APR.DriveToPoint(fulfillmentB_x_pos, fulfillmentB_y_pos)     # drive to the end of the row

    # Turn to face course
    APR.TurnToAngle(0)


    
# Important variables for function call
MyRobot = APR_Location()    # Used for position tracking and movement
AllContainers = Containers()    # Used for container location and measurements

#------------------------------------------------------------#
#                       SUBTASK 1                            #

CONTAINER_NUMBER = 2    #Enter the container number, the program will automatically subtract one from the inputted value

#------------------------------------------------------------#

# Set the inputted number as a container in A1
TargetContainer = AllContainers.A1[CONTAINER_NUMBER-1]

# Function call
Subtask1_FD(MyRobot, TargetContainer, AllContainers)