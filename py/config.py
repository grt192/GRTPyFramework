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
#from grt.sensors.ticker import ticker
from grt.macro.drive_macro import DriveMacro
from grt.sensors.encoder import Encoder
from grt.sensors.gyro import Gyro

# Joysticks
lstick = Attack3Joystick(1)

sp = SensorPoller((lstick, ))

#Solenoids (PINS TENTATIVE)
#solenoid = wpilib.Solenoid(7, 1)

#Motors (PINS TENTATIVE)
l_dt = Motorset(tuple(wpilib.Talon(i) for i in range(3, 4)))
r_dt = Motorset(tuple(wpilib.Talon(i) for i in range(1, 2)), scalefactors=(-1, ) * 3)


import math
pi = math.pi
dist_per_pulse = .01  # (pi * (1.75 * 2))/128

left_encoder=Encoder(8,9, dist_per_pulse, reverse=True)
right_encoder=Encoder(13, 14, dist_per_pulse, reverse=True)

dt = DriveTrain(l_dt, r_dt)

ac = ArcadeDriveController(dt, lstick)

# Autonomous
gyro = Gyro(1)
auto_sp = SensorPoller((dt.right_encoder, dt.left_encoder))
drive_macro = DriveMacro(dt, 20, 10)
turn_macro = TurnMacro(dt, gyro, 90, 5)
