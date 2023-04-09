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
    else:
        Target_Container_y -= AllContainers.DISTANCE_BETWEEN_CENTERS



SHELVING_AREA = "A1"    # must be capitalized
CONTAINER_NUMBER = 2
BARCODE_TYPE = 1
FULFILLMENT_CENTER = 'A'    # must be capitalized

AllContainers = Containers()
MyRobot = APR_Location()

FullTrack_FD(SHELVING_AREA, CONTAINER_NUMBER, BARCODE_TYPE, FULFILLMENT_CENTER, AllContainers, MyRobot)