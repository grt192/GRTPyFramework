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
from grt.sensors.gyro import Gyro
from grt.core import SensorPoller
from grt.core import Constants
from grt.mechanism.mechcontroller import AttackMechController
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset
from grt.mechanism import Intake, Shooter, Defense
from grt.sensors.ticker import Ticker
from grt.core import GRTMacroController
from grt.autonomous.basic_auto import BasicAuto
from grt.sensors.encoder import Encoder
import grt.networktables as networktables
from grt.macro.drive_macro import DriveMacro
from grt.macro.turn_macro import TurnMacro
from grt.macro.wind_macro import WindMacro
from grt.sensors.potentiometer import Potentiometer

#Pin map (Move this to a .txt file)
#Pin signifies electrical. Port signifies pneumatic.
#Talons
l_dt_pin = 1
r_dt_pin = 2
ep_motor_pin1 = 10
ep_motor_pin2 = 8
angle_change_motor_pin1 = 9
angle_change_motor_pin2 = 7
shooter_pin = 6

#Solenoids + Relays
compressor_pin = 2

dt_shifter_port = 1
shooter_port = 2
defense_port = 3

#Digital Sensors
l_dt_encoder_pin1 = 2
l_dt_encoder_pin2 = 3
r_dt_encoder_pin1 = 4
r_dt_encoder_pin2 = 5
pressure_sensor_pin = 1

#Analog Sensors
potentiometer_pin = 3
gyro_pin = 2

# Joysticks
lstick = Attack3Joystick(1)
rstick = Attack3Joystick(2)

#DT
dt_dpp = (pi * 3.45 / (128 * 12))  # (pi * (1.74 * 2)) / (128 * 12)
left_encoder = Encoder(l_dt_encoder_pin1, l_dt_encoder_pin2, dt_dpp)
right_encoder = Encoder(r_dt_encoder_pin1, r_dt_encoder_pin2, dt_dpp)
l_dt = Motorset(tuple(wpilib.Talon(i) for i in (l_dt_pin,)))
r_dt = Motorset(tuple(wpilib.Talon(i) for i in (r_dt_pin,)), scalefactors=(-1, ))
dt = DriveTrain(l_dt, r_dt, left_encoder=left_encoder, right_encoder=right_encoder)

#Compressor
compressor = wpilib.Compressor(pressure_sensor_pin, compressor_pin)
compressor.Start()

#Mechs

#Pickup
ep_motor = Motorset(tuple(wpilib.Talon(ep_motor_pin1), wpilib.Talon(ep_motor_pin2))
angle_change_motor = Motorset(tuple(wpilib.Talon(angle_change_motor_pin1), wpilib.Talon(angle_change_motor_pin2))
intake = Intake(ep_motor, angle_change_motor)

#Shooter (winch + release)
shooter = Shooter(wpilib.Talon(shooter_pin), wpilib.Solenoid(shooter_port))

#Defense
defense = Defense(wpilib.Solenoid(defense_port))

#Teleop Controllers
ac = ArcadeDriveController(dt, lstick)
mc = AttackMechController(lstick, rstick, intake, defense, shooter)

#Network Tables
vision_table = networktables.get_table('vision')

#Diagnostic ticker
tick = Ticker(.2)
#Ticker test:
#tick.tick = lambda: print(str(table['fat']) + "\n")

#Autonomous
#dt and shooter are declared above for mechs
#vision_table is declared above for network tables
potentiometer = Potentiometer(3)
gyro = Gyro(2)
auto = BasicAuto(dt, shooter, vision_table, potentiometer, gyro)

#constants test
#c = Constants()
#c.add_listener(drive_macro._constant_listener)

#Sensor Pollers
sp = SensorPoller((lstick, rstick, dt.right_encoder, dt.left_encoder, tick))
auto_sp = SensorPoller((dt.right_encoder, dt.left_encoder, gyro, potentiometer, tick))
