"""
Config File for Robot

#TODO: Setup for Constants File
"""

__author__ = "Sidd Karamcheti"

import wpilib
from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController

# Joysticks
lstick = Attack3Joystick(1)
rstick = Attack3Joystick(2)

sp = SensorPoller((lstick, rstick, ))

#Solenoids (PINS TENTATIVE)
#solenoid = wpilib.Solenoid(7, 1)

#Motors 
lfm = wpilib.Talon(3)
lrm = wpilib.Talon(4)
rfm = wpilib.Talon(1)
rrm = wpilib.Talon(2)
shooter_pivot_motor = wpilib.Talon(8)
flywheel_1 = wpilib.Talon(9)
flywheel_2 = wpilib.Talon(10)

mechs = Mechanisms(rstick, flywheel_1, flywheel_2, shooter_pivot_motor)
dt = DriveTrain(lfm, rfm, lrm, rrm)
dt.set_scale_factors(1, -1, 1, -1)

ac = ArcadeDriveController(dt, lstick)
