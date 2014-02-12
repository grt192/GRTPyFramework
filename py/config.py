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
from grt.sensors.gyro import Gyro
from grt.core import SensorPoller, Constants
from grt.mechanism.mechcontroller import AttackMechController
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset
from grt.mechanism import Intake, Shooter, Defense
from grt.sensors.ticker import Ticker
from grt.autonomous.basic_auto import BasicAuto
from grt.sensors.encoder import Encoder
from grt.sensors.switch import Switch
import grt.networktables as networktables
from grt.sensors.potentiometer import Potentiometer

constants = Constants()

#Pin/Port map
#Talons
dt_left = wpilib.Talon(1)
dt_right = Motorset(tuple(wpilib.Talon(2)), scalefactors=(-1, ))
ep_left = wpilib.Talon(10)
ep_right = wpilib.Talon(8)
achange_left = wpilib.Talon(9)
achange_right = wpilib.Talon(7)
shooter_winch = wpilib.Talon(6)

#Solenoids + Relays
compressor_pin = 2
dt_shifter = wpilib.Solenoid(1)
shooter_shifter = wpilib.Solenoid(2)
defense_actuator = wpilib.Solenoid(3)

#Digital Sensors
left_encoder = Encoder(2, 3, constants['dt_dpp'])
right_encoder = Encoder(4, 5, constants['dt_dpp'])
pressure_sensor_pin = 1
achange_limit_lf = Switch(13)  # TODO: check accuracy
achange_limit_lr = Switch(12)
achange_limit_rf = Switch(11)
achange_limit_rr = Switch(10)

#Analog Sensors
potentiometer = Potentiometer(3)  # TODO: scale + offset
gyro = Gyro(2)

# Joysticks
lstick = Attack3Joystick(1)
rstick = Attack3Joystick(2)

#DT
dt = DriveTrain(dt_left, dt_right, dt_shifter,
                left_encoder=left_encoder, right_encoder=right_encoder)

#Compressor
compressor = wpilib.Compressor(pressure_sensor_pin, compressor_pin)
compressor.Start()

#Mechs
#Pickup
ep_motors = Motorset(tuple(ep_left, ep_right), scalefactors=(1, -1))
intake = Intake(ep_motors, achange_left, achange_right,
                achange_limit_lf, achange_limit_lr,
                achange_limit_rf, achange_limit_rr)

#Shooter (winch + release)
shooter = Shooter(shooter_winch, shooter_shifter)

#Defense
defense = Defense(defense_actuator)

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
auto = BasicAuto(dt, shooter, vision_table, potentiometer, gyro)

#Sensor Pollers
sp = SensorPoller((lstick, rstick, dt.right_encoder, dt.left_encoder, tick))
auto_sp = SensorPoller((dt.right_encoder, dt.left_encoder, gyro, potentiometer, tick))
