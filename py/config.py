"""
Config File for Robot

#TODO: Setup for Constants File
"""

__author__ = "Sidd Karamcheti"

try:
    import wpilib
except ImportError:
    from pyfrc import wpilib

from math import pi
from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller
from grt.core import Constants
from grt.mechanism.mechcontroller import AttackMechController
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset
from grt.mechanism import Intake, Shooter, Defense
from grt.sensors.ticker import Ticker
from grt.macro.drive_macro import DriveMacro
from grt.sensors.encoder import Encoder
import grt.networktables as networktables

# Joysticks
lstick = Attack3Joystick(1)

#DT stuff
l_dt = Motorset(tuple(wpilib.Talon(i) for i in range(6, 9)))
r_dt = Motorset(tuple(wpilib.Talon(i) for i in range(1, 4)), scalefactors=(-1, ) * 3)

dt_dpp = (pi * 3.45 / (128 * 12))  # (pi * (1.74 * 2)) / (128 * 12)
left_encoder = Encoder(2, 3, dt_dpp)
right_encoder = Encoder(4, 5, dt_dpp)
dt = DriveTrain(l_dt, r_dt, left_encoder=left_encoder, right_encoder=right_encoder)

compressor = wpilib.Compressor(14, 1)
compressor.Start()

#Mechs
#Pickup stuff
pickup_motor = Motorset((wpilib.Talon(5), wpilib.Talon(10)), (1, -1))
intake = Intake(pickup_motor, wpilib.Talon(9))

shooter = Shooter(wpilib.Talon(4), wpilib.Solenoid(2))
defense = Defense(wpilib.Solenoid(1))

#Teleop Controllers
ac = ArcadeDriveController(dt, lstick)
mc = AttackMechController(lstick, intake, defense, shooter)

# Autonomous
auto_sp = SensorPoller((dt.right_encoder, dt.left_encoder))
drive_macro = DriveMacro(dt, 10, 10)

#Diagnostic ticker
tick = Ticker(.2)
#tick.tick = lambda: print(str(left_encoder.distance) + " " + str(right_encoder.distance) + "\n")

#networkTablesStuffCauseILoveIt
table = networktables.get_table('test')
table['fat'] = 'ugly'
table['one'] = 'two'

#constants
c = Constants()
c.add_listener(drive_macro._constant_listener)
c.poll

def _constant_update_listener(sensor, state_id, datum):
	if state_id is 'button11' and datum:
		c.poll

#Sensor Pollers
sp = SensorPoller((lstick, dt.right_encoder, dt.left_encoder, tick))
auto_sp = SensorPoller((dt.right_encoder, dt.left_encoder, tick))
