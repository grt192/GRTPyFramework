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
from grt.mechanism.pickup import Pickup

# Joysticks
lstick = Attack3Joystick(1)

sp = SensorPoller((lstick, ))

#Solenoids (PINS TENTATIVE)
#solenoid = wpilib.Solenoid(7, 1)

#Motors (PINS TENTATIVE)
l_dt = Motorset(tuple(wpilib.Talon(i) for i in range(3, 6)))
r_dt = Motorset(tuple(wpilib.Talon(i) for i in range(8, 11)), scalefactors=(-1, ) * 3)
pickup_motor = wpilib.Talon(2)

pckp = Pickup(pickup_motor, lstick)

dt = DriveTrain(l_dt, r_dt)

ac = ArcadeDriveController(dt, lstick)
