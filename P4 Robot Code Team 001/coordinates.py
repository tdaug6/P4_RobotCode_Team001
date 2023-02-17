#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3Tire
STUD_MM = 8
# test with a robot that:
# - uses the standard wheels known as EV3Tire
# - wheels are 16 studs apart
mdiff = MoveDifferential(OUTPUT_A, OUTPUT_B, EV3Tire, 16 * STUD_MM)

# Enable odometry
mdiff.odometry_start()

# Use odometry to drive to specific coordinates
mdiff.on_to_coordinates(SpeedRPM(40), 300, 300)

# Use odometry to go back to where we started
mdiff.on_to_coordinates(SpeedRPM(40), 0, 0)

# Use odometry to rotate in place to 90 degrees
mdiff.turn_to_angle(SpeedRPM(40), 90)

# Disable odometry
mdiff.odometry_stop()