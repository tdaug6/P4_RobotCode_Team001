#!/usr/bin/env python3
from APR_Location import *
from globals import *

def Subtask1_FD(APR,containerLocation, Container):
    target_y_pos = Container
    

MyRobot = APR_Location()
AllContainers = Containers()
CONTAINER = AllContainers.A1[3]

#--------------------#
#   SUBTASK 1

Subtask1_FD(MyRobot, CONTAINER, AllContainers)