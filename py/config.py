"""
Config File for Robot

#TODO: Setup for Constants File
"""

__author__ = "Sidd Karamcheti"

import wpilib

# Joysticks
lstick = wpilib.Joystick(1)
rstick = wpilib.Joystick(2)


#Solenoids (PINS TENTATIVE)
solenoid = wpilib.Solenoid(7, 1)

#Motors (PINS TENTATIVE)
#motor = wpilib.CANJaguar(8)