"""
Config File for Robot

#TODO: Setup for Constants File
"""

__author__ = "Sidd Karamcheti"

from wpilib import Talon, Solenoid, Compressor, DriverStation

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
from grt.sensors.gyro import Gyro
from grt.core import SensorPoller, Constants
from grt.mechanism.mechcontroller import MechController
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset
from grt.mechanism import Intake, Shooter, Defense
from grt.sensors.ticker import Ticker
from grt.autonomous.basic_auto import BasicAuto
from grt.autonomous.twoball_auto import TwoBallAuto
from grt.sensors.encoder import Encoder
from grt.sensors.switch import Switch
import grt.networktables as networktables
from grt.sensors.potentiometer import Potentiometer

constants = Constants()

#Pin/Port map
#Talons
dt_right = Talon(2)
dt_left = Motorset((Talon(1), ), scalefactors=(-1, ))
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
left_encoder = Encoder(3, 4, constants['dt_dpp'], reverse=True)
right_encoder = Encoder(1, 2, constants['dt_dpp'])
pressure_sensor_pin = 14
achange_limit_lf = Switch(13)
achange_limit_lr = Switch(12)
achange_limit_rf = Switch(11)
achange_limit_rr = Switch(10)
winch_limit = Switch(9)

#Analog Sensors
shooter_potentiometer = Potentiometer(3, scale=constants['spot_scale'],
                                      offset=constants['spot_offset'])
gyro = Gyro(2)

# Controllers
driver_stick = Attack3Joystick(1)
xbox_controller = XboxJoystick(2)

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
shooter = Shooter(shooter_winch, shooter_shifter, winch_limit, shooter_potentiometer)

#Defense
defense = Defense(defense_actuator)

#Teleop Controllers
ac = ArcadeDriveController(dt, driver_stick)
mc = MechController(driver_stick, xbox_controller, intake, defense, shooter)

#Network Tables
vision_table = networktables.get_table('vision')
status_table = networktables.get_table('status')

ds = DriverStation.GetInstance()


#Diagnostic ticker
def status_tick():
    status_table['l_speed'] = dt.left_motor.Get()
    status_table['r_speed'] = dt.right_motor.Get()
    status_table['shooter_wound'] = shooter_potentiometer.p.Get()
    status_table['shooter_shooting'] = shooter_shifter.Get()
    status_table['voltage'] = ds.GetBatteryVoltage()
    status_table['status'] = 'disabled' if ds.IsDisabled() else 'teleop' if ds.IsOperatorControl() else 'auto'

status_ticker = Ticker(.05)
status_ticker.tick = status_tick


def reset_tick():
    if driver_stick.button10 and driver_stick.button11:
        constants.poll()

reset_ticker = Ticker(1)
reset_ticker.tick = reset_tick

#Autonomous
#dt and shooter are declared above for mechs
#vision_table is declared above for network tables
if '2ballautoenabled' in constants and constants['2ballautoenabled'] != 0:
    auto = TwoBallAuto(dt, shooter, intake)
else:
    auto = BasicAuto(dt, shooter, intake)
basicauto = BasicAuto(dt, shooter, intake)
twoballauto = TwoBallAuto(dt, shooter, intake)

#Sensor Pollers
sp = SensorPoller((gyro, shooter_potentiometer, dt.right_encoder,
                   dt.left_encoder, status_ticker, reset_ticker,
                   achange_limit_lf, achange_limit_rf,
                   achange_limit_lr, achange_limit_rr,
                   winch_limit))  # robot sensors, poll always
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices
