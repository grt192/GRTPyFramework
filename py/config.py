"""
Config File for Robot

#TODO: Setup for Constants File
"""

__author__ = "Sidd Karamcheti"

import wpilib
from math import pi
from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.sensors.ticker import Ticker
from grt.macro.drive_macro import DriveMacro
from grt.sensors.encoder import Encoder

# Joysticks
lstick = Attack3Joystick(1)

#Solenoids (PINS TENTATIVE)
#solenoid = wpilib.Solenoid(7, 1)

#Motors (PINS TENTATIVE)
lfm = wpilib.Talon(6)
lmm = wpilib.Talon(7)
lrm = wpilib.Talon(8)
rfm = wpilib.Talon(1)
rmm = wpilib.Talon(2)
rrm = wpilib.Talon(3)

feet_per_pulse = (pi * (1.75 * 2))/(128 * 12)
left_encoder=Encoder(2,3, feet_per_pulse)
right_encoder=Encoder(4, 5, feet_per_pulse)

dt = DriveTrain(lfm, rfm, lmm, rmm, lrm, rrm, left_encoder=left_encoder, right_encoder=right_encoder)

ac = ArcadeDriveController(dt, lstick)

# Autonomous
drive_macro = DriveMacro(dt, 5, 10)

def print_encoders(sensor, state_id, datum):
	print(str(left_encoder.distance) + " " + str(right_encoder.distance) + "\n")

def print_joystick(sensor, state_id, datum):
	print("y: " + str(lstick.y_axis) + " x: " + str(lstick.x_axis) + "\n")

tick = Ticker(.2)
tick.add_listener(print_encoders)
tick.add_listener(print_joystick)

sp = SensorPoller((lstick, dt.right_encoder, dt.left_encoder, tick))
auto_sp = SensorPoller((dt.right_encoder, dt.left_encoder, tick))