"""
Config File for Robot
"""

__author__ = "Sidd Karamcheti"

from wpilib import Talon, Solenoid, Compressor, DriverStation

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
from grt.sensors.gyro import Gyro
from grt.core import SensorPoller, Constants
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset
from grt.sensors.ticker import Ticker
from grt.sensors.encoder import Encoder
import grt.networktables as networktables
from grt.mechanism import Pickup
from grt.mechanism.mechcontroller import MechController

constants = Constants()

#Pin/Port map
#Talons
dt_right = Talon(2)
dt_left = Motorset((Talon(1), ), scalefactors=(-1, ))
roller = Talon(4)
elev = Talon(5)

#Solenoids + Relays
compressor_pin = 1
dt_shifter = Solenoid(1)
actuator = Solenoid(2)

#Digital Sensors
left_encoder = Encoder(3, 4, constants['dt_dpp'], reverse=True)
right_encoder = Encoder(1, 2, constants['dt_dpp'])
pressure_sensor_pin = 14

#Analog Sensors
gyro = Gyro(2)

# Controllers
driver_stick = Attack3Joystick(1)
xbox_controller = XboxJoystick(2)
driver_stick = MechController(pickup, Attack3Joystick(1))

#mechanisms
pickup = Pickup(roller, elev, actuator)

#DT
dt = DriveTrain(dt_left, dt_right, dt_shifter,
                left_encoder=left_encoder, right_encoder=right_encoder)

#Compressor
compressor = Compressor(pressure_sensor_pin, compressor_pin)
compressor.Start()

#Teleop Controllers
ac = ArcadeDriveController(dt, driver_stick)
mc = MechController(pickup, driver_stick)

#Network Tables
vision_table = networktables.get_table('vision')
status_table = networktables.get_table('status')

ds = DriverStation.GetInstance()


#Diagnostic ticker
def status_tick():
    status_table['l_speed'] = dt.left_motor.Get()
    status_table['r_speed'] = dt.right_motor.Get()
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

#Sensor Pollers
sp = SensorPoller((gyro, dt.right_encoder,
                   dt.left_encoder, status_ticker, reset_ticker))
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices
