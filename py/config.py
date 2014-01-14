"""
Config File for Robot

#TODO: Setup for Constants File
"""

__author__ = "Sidd Karamcheti"

try:
    import wpilib
except ImportError:
    from pyfrc import wpilib

from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset

# Joysticks
lstick = Attack3Joystick(1)

sp = SensorPoller((lstick, ))

#Solenoids (PINS TENTATIVE)
#solenoid = wpilib.Solenoid(7, 1)

#Motors (PINS TENTATIVE)
l_dt = Motorset(wpilib.Talon(6), wpilib.Talon(7), wpilib.Talon(8))
r_dt = Motorset(wpilib.Talon(3), wpilib.Talon(4), wpilib.Talon(5), scalefactors=(-1, -1, -1))

dt = DriveTrain(l_dt, r_dt)

ac = ArcadeDriveController(dt, lstick)
