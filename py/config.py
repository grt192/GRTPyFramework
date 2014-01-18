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
from grt.sensors.ticker import ticker
# Joysticks
lstick = Attack3Joystick(1)

sp = SensorPoller((lstick, ))

#Solenoids (PINS TENTATIVE)
#solenoid = wpilib.Solenoid(7, 1)

#Motors (PINS TENTATIVE)
lfm = wpilib.Talon(6)
lmm = wpilib.Talon(7)
lrm = wpilib.Talon(8)
rfm = wpilib.Talon(3)
rmm = wpilib.Talon(4)
rrm = wpilib.Talon(5)

dt = DriveTrain(lfm, rfm, lmm, rmm, lrm, rrm)

ac = ArcadeDriveController(dt, lstick)

# Autonomous
auto_sp = SensorPoller(ticker)
