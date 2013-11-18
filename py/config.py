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

#Super Sketch Omega 1
shooter_pivot_motor = wpilib.Talon(8)

flywheel_1 = wpilib.Talon(9)
flywheel_2 = wpilib.Talon(10)

def flywheel_listener(source, id, datum):
	if id == 'button3' and rstick.button3:
		flywheel_1.Set(1)
		flywheel_2.Set(1)
	elif id == 'button3' and not rstick.button3:
		flywheel_1.Set(0)
		flywheel_2.Set(0)


def shooter_pivot_listener(source, id, datum):
    if id == 'y_axis':
        shooter_pivot_motor.Set(datum * 0.25)

for r in (flywheel_listener, shooter_pivot_listener):
    rstick.add_listener(r)

sp = SensorPoller((lstick, rstick, ))

#Solenoids (PINS TENTATIVE)
#solenoid = wpilib.Solenoid(7, 1)

#Motors 
lfm = wpilib.Talon(3)
lrm = wpilib.Talon(4)
rfm = wpilib.Talon(1)
rrm = wpilib.Talon(2)

dt = DriveTrain(lfm, rfm, lrm, rrm)
dt.set_scale_factors(1, -1, 1, -1)

ac = ArcadeDriveController(dt, lstick)
