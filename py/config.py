"""
Config File for Robot
"""

__author__ = "Alex Mallery"

crio_native = True

try:
	import wpilib
except ImportError:
	from pyfrc import wpilib
	crio_native = False

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
from grt.sensors.gyro import Gyro
from grt.core import SensorPoller, Constants
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset
from grt.sensors.ticker import Ticker
from grt.sensors.encoder import Encoder
from grt.sensors.twist_joystick import TwistJoystick
from grt.mechanism.centric_controller import CentricDriveController
from grt.mechanism.mecanum_dt import MecanumDT
#--------------------------------------------------

constants = Constants()
#Pin/Port map

#Use the motors in the order fl, fr, rl, rr.
fl_motor = wpilib.Talon(1)
fr_motor = wpilib.Talon(2)
rl_motor = wpilib.Talon(3)
rr_motor = wpilib.Talon(4)

#Solenoids + Relays
compressor_pin = 1
dt_shifter = wpilib.Solenoid(1)

#Digital Sensors
left_encoder = Encoder(3, 4, constants['dt_dpp'], reverse=True)
right_encoder = Encoder(1, 2, constants['dt_dpp'])
pressure_sensor_pin = 14

#Analog Sensors
gyro = Gyro(2)

# Controllers
driver_stick = TwistJoystick(1)
xbox_controller = XboxJoystick(2)

dt = MecanumDT(fl_motor, fr_motor, rl_motor, rr_motor, left_encoder=left_encoder, right_encoder=right_encoder, gyro=gyro)

#Compressor
compressor = wpilib.Compressor(pressure_sensor_pin, compressor_pin)
compressor.Start()

#Mechs

#Teleop Controllers
ac = CentricDriveController(dt, driver_stick)



ds = wpilib.DriverStation.GetInstance()




#Autonomous

#Sensor Pollers
sp = SensorPoller((gyro, dt.right_encoder,
                   dt.left_encoder))
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices

if crio_native:
	import grt.networktables as networktables
	#Network Tables
	vision_table = networktables.get_table('vision')
	status_table = networktables.get_table('status')

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

#--------------------------------------------------
"""constants = Constants()

#Pin/Port map
#Talons
dt_right = Talon(2)
dt_left = Motorset((Talon(1), ), scalefactors=(-1, ))

#Solenoids + Relays
compressor_pin = 1
dt_shifter = Solenoid(1)

#Digital Sensors
left_encoder = Encoder(3, 4, constants['dt_dpp'], reverse=True)
right_encoder = Encoder(1, 2, constants['dt_dpp'])
pressure_sensor_pin = 14

#Analog Sensors
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

#Teleop Controllers
ac = ArcadeDriveController(dt, driver_stick)



ds = DriverStation.GetInstance()




#Autonomous

#Sensor Pollers
sp = SensorPoller((gyro, dt.right_encoder,
                   dt.left_encoder))
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices"""
