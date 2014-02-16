"""
Config File for Robot

#TODO: Setup for Constants File
"""

__author__ = "Sidd Karamcheti"

from wpilib import Talon, Solenoid, Compressor, DriverStation

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.gyro import Gyro
from grt.core import SensorPoller, Constants
from grt.mechanism.mechcontroller import AttackMechController
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset
from grt.mechanism import Intake, Shooter, Defense
from grt.sensors.ticker import Ticker
from grt.autonomous.basicer_auto import BasicerAuto
from grt.sensors.encoder import Encoder
from grt.sensors.switch import Switch
import grt.networktables as networktables
from grt.sensors.potentiometer import Potentiometer

constants = Constants()

#Pin/Port map
#Talons
dt_left = Talon(1)
dt_right = Motorset((Talon(2), ), scalefactors=(-1, ))
ep_left = Talon(10)
ep_right = Talon(8)
achange_left = Talon(9)
achange_right = Talon(7)
shooter_winch = Talon(6)

#Solenoids + Relays
compressor_pin = 1
dt_shifter = Solenoid(1)
shooter_shifter = Solenoid(2)
defense_actuator = Solenoid(3)

#Digital Sensors
left_encoder = Encoder(3, 4, constants['dt_dpp'])
right_encoder = Encoder(1, 2, constants['dt_dpp'])
pressure_sensor_pin = 14
achange_limit_lf = Switch(13)
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
compressor = Compressor(pressure_sensor_pin, compressor_pin)
compressor.Start()

#Mechs
#Pickup
ep_motors = Motorset((ep_left, ep_right), scalefactors=(1, -1))
intake = Intake(ep_motors, achange_left, achange_right,
                achange_limit_lf, achange_limit_lr,
                achange_limit_rf, achange_limit_rr)

#Shooter (winch + release)
shooter = Shooter(shooter_winch, shooter_shifter, potentiometer)

#Defense
defense = Defense(defense_actuator)

#Teleop Controllers
ac = ArcadeDriveController(dt, lstick)
mc = AttackMechController(lstick, rstick, intake, defense, shooter)

#Network Tables
vision_table = networktables.get_table('vision')
status_table = networktables.get_table('status')


#Diagnostic ticker
def status_tick():
    status_table['l_speed'] = dt.left_motor.Get()
    status_table['r_speed'] = dt.right_motor.Get()
    status_table['shooter_wound'] = potentiometer.p.Get()
    status_table['shooter_shooting'] = shooter_shifter.Get()
    status_table['battery_voltage'] = DriverStation.GetInstance().GetBatteryVoltage()

status_ticker = Ticker(.05)
status_ticker.tick = status_tick

#Autonomous
#dt and shooter are declared above for mechs
#vision_table is declared above for network tables
auto = BasicerAuto(shooter, 3)

#Sensor Pollers
sp = SensorPoller((gyro, potentiometer, dt.right_encoder,
                   dt.left_encoder, status_ticker))  # robot sensors, poll always
hid_sp = SensorPoller((lstick, rstick))  # human interface devices
