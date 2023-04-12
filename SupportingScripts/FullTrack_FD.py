#!/usr/bin/env python3
from APR_Location import *
from globals import *
import time

def FullTrack_FD(SHELVING_AREA, CONTAINER_NUMBER, BARCODE_TYPE, FULFILLMENT_CENTER, ALL_CONTAINERS, APR):
    
    # Determine the target container based on the inputs for container number and shelving area
    if SHELVING_AREA == "A1":
        Target_Container = AllContainers.A1[CONTAINER_NUMBER-1]
    if SHELVING_AREA == "A2":
        Target_Container = AllContainers.A2[CONTAINER_NUMBER-1]
    if SHELVING_AREA == "B1":
        Target_Container = AllContainers.B1[CONTAINER_NUMBER-1]
    if SHELVING_AREA == "B2":
        Target_Container = AllContainers.B2[CONTAINER_NUMBER-1]
    if SHELVING_AREA == "C1":
        Target_Container = AllContainers.C1[CONTAINER_NUMBER-1]
    if SHELVING_AREA == "C2":
        Target_Container = AllContainers.C2[CONTAINER_NUMBER-1]
    if SHELVING_AREA == "D1":
        Target_Container = AllContainers.D1[CONTAINER_NUMBER-1]
    if SHELVING_AREA == "D2":
        Target_Container = AllContainers.D2[CONTAINER_NUMBER-1]
    
    # Set the target container location for x and y
    Target_Container_x = Target_Container[0]
    Target_Container_y = Target_Container[1]

    # Update the y position based on what side of the hall the container is on
    if CONTAINER_NUMBER >= 7:
        Target_Container_y += AllContainers.DISTANCE_BETWEEN_CENTERS
        # Drive to container
        #   Drive to hall container is located in
        APR.moveDistance(Target_Container_y)
        #   Turn towards the hall
        APR.TurnToAngle(90,True)
        #   Drive to the container location
        APR.moveDistance(Target_Container_x)

        """READ BARCODE"""

        """HALL TURN IN"""
        """RAISE LIFT"""
        """HALL TURN OUT"""

        APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_B_X - Target_Container_x)

        if FULFILLMENT_CENTER == 'B':
            #Turn to face center B
            APR.TurnToAngle(180,True)

            # Drive into Center B
            DistanceModifier = 5
            APR.moveDistance(Target_Container_y-DistanceModifier)

            """LOWER LIFT"""

            # Slightly back away from the center
            APR.MoveReverse(10)

            # Turn to drive down the hall
            APR.TurnToAngle(270,True)

            # Drive to be in line with the home
            DistanceModifier = 10
            APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_B_X - DistanceModifier)

            # Turn to drive into fulfillment center
            APR.TurnToAngle(180,False)

            # Drive into the fulfillment center
            Transition_y = 12*2.54
            APR.moveDistance(Transition_y)

            # Turn to face the facility
            APR.TurnToAngle(0,False)

        elif FULFILLMENT_CENTER == 'C':
            # Turn to face top of facility
            APR.TurnToAngle(0,False)

            # Drive to edge hall of facility
            DistanceModifier = 10
            APR.moveDistance(FULFILLMENT_CENTER_D_Y - Target_Container_y - DistanceModifier)

            # Turn to face left side of faciity
            APR.TurnToAngle(-90,False)

            # Drive to be in line with the center C
            DistanceModifier = 10
            APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_B_X - DistanceModifier)

            # Turn to face center C
            APR.TurnToAngle(0,True)

            # Move slightly into center C
            Transition_y = 10
            APR.moveDistance(Transition_y)

            """LOWER LIFT"""

            # Slightly back away from the center
            APR.MoveReverse(Transition_y)

            # Turn to face home
            APR.TurnToAngle(-180,False)

            # Drive into home A
            DistanceModifier = 10
            APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_C_Y-DistanceModifier)

            # Turn to face the facility
            APR.TurnToAngle(0,True)

        else:
            # Turn to face center D
            APR.TurnToAngle(0,False)

            # Drive into center D
            DistanceModifier = 0
            APR.moveDistance(FULFILLMENT_CENTER_D_Y - Target_Container_y - DistanceModifier)

            """LOWER LIFT"""

            # Slightly back away from the center
            APR.MoveReverse(10)

            # Drive to be in line with the center C
            DistanceModifier = 10
            APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_D_X - DistanceModifier)
            
            # Turn to face home A
            APR.TurnToAngle(-180,False)

            # Drive into home A
            DistanceModifier = 10
            APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_C_Y-DistanceModifier)

            # Turn to face the facility
            APR.TurnToAngle(0,True)


    else:
        Target_Container_y -= AllContainers.DISTANCE_BETWEEN_CENTERS

        # Drive into hall connecting home A and center B
        DistanceModifier = 10
        APR.moveDistance(ALL_CONTAINERS.A_B_HALL_Y-DistanceModifier)

        # Turn to face towards center B
        APR.TurnToAngle(90,True)

        # Drive to the end of the hall, in line with centers B and D
        DistanceModifier = 10
        APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_B_X-DistanceModifier)

        # Turn to face center D
        APR.TurnToAngle(0,False)

        # Drive to the hall with the container
        DistanceModifier = 0
        APR.moveDistance(Target_Container_y-Target_Container_y- DistanceModifier)

        # Turn to drive to container x position
        APR.moveDistance(Target_Container_x)

        """READ BARCODE"""

        """HALL TURN IN"""
        """RAISE LIFT"""
        """HALL TURN OUT"""

        APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_B_X - Target_Container_x)

        if FULFILLMENT_CENTER == 'B':
            # Turn to face home A
            APR.TurnToAngle(-180,False)

            # Drive to the end of the hall
            APR.moveDistance(Target_Container_y - ALL_CONTAINERS.A_B_HALL_Y)

            # Turn to face towards center B
            APR.TurnToAngle(-270,False)

            # Drive to the end of the hall
            DistanceModifier = 10
            APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_B_X-DistanceModifier)

            # Turn towards center B
            APR.TurnToAngle(-180,True)

            # Slighlty drive into center B
            Transition_y = 10
            APR.moveDistance(Transition_y)

            """LOWER LIFT"""

            # Slightly back away from the center
            APR.MoveReverse(Transition_y)

            # Turn towards home A
            APR.TurnToAngle(-90,True)

            # Drive to the end of the hall
            DistanceModifier = 10
            APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_B_X-DistanceModifier)

            # Turn to home A
            APR.TurnToAngle(-180,False)

            # Drive into home
            DistanceModifier = 10
            APR.moveDistance(ALL_CONTAINERS.A_B_HALL_Y-DistanceModifier)

            # Turn to face facility
            APR.TurnToAngle(0,True)

        elif FULFILLMENT_CENTER == 'C':
            # Turn to face center C
            APR.TurnToAngle(0,True)

            # Drive into center C
            DistanceModifier = 0
            APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_C_Y - Target_Container_y - DistanceModifier)

            """LOWER LIFT"""
            
            # Slightly back away from the center
            APR.MoveReverse(Transition_y)

            # Turn to face home A
            APR.TurnToAngle(-180,False)

            # Drive into home A
            DistanceModifier = 10
            APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_C_Y-DistanceModifier)

            # Turn to face faciity
            APR.TurnToAngle(0,True)


        else:
            # Turn to face home A
            APR.TurnToAngle(0,True)

            # Drive to the end of the hall
            DistanceModifier = 10
            APR.moveDistance(Target_Container_y - ALL_CONTAINERS.FULFILLMENT_CENTER_C_Y-DistanceModifier)

            # Turn to face towards center B
            APR.TurnToAngle(90,True)

            # Drive to the end of the hall
            DistanceModifier = 10
            APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_D_X-DistanceModifier)

            # Turn towards center B
            APR.TurnToAngle(0,False)

            # Slighlty drive into center B
            Transition_y = 10
            APR.moveDistance(Transition_y)

            """LOWER LIFT"""

            # Slightly back away from the center
            APR.MoveReverse(Transition_y)

            # Turn towards home A
            APR.TurnToAngle(-90,False)

            # Drive to the end of the hall
            DistanceModifier = 10
            APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_D_X-DistanceModifier)

            # Turn to home A
            APR.TurnToAngle(-180,False)

            # Drive into home
            DistanceModifier = 10
            APR.moveDistance(ALL_CONTAINERS.FULFILLMENT_CENTER_D_Y-DistanceModifier)

            # Turn to face facility
            APR.TurnToAngle(0,True)


SHELVING_AREA = "A1"    # must be capitalized
CONTAINER_NUMBER = 2
BARCODE_TYPE = 1
FULFILLMENT_CENTER = 'A'    # must be capitalized

AllContainers = Containers()
MyRobot = APR_Location()
MyRobot.calibrateGyro()

FullTrack_FD(SHELVING_AREA, CONTAINER_NUMBER, BARCODE_TYPE, FULFILLMENT_CENTER, AllContainers, MyRobot)