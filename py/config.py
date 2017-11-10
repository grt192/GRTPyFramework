"""
Config File for Robot
"""

#@dhruv_rajan is editing config.py
from wpilib import Solenoid, Compressor, DriverStation, DigitalInput
from ctre import CANTalon

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
#from grt.sensors.gyro import Gyro
from grt.core import SensorPoller
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset
from grt.sensors.ticker import Ticker
from grt.sensors.encoder import Encoder
from grt.sensors.talon import Talon
from grt.mechanism.mechcontroller import MechController
from grt.sensors.switch import Switch

from grt.mechanism.swervecontroller import SwerveController
from grt.mechanism.swervemodule import SwerveModule


#DT Talons and Objects

# talon1 = CANTalon(1)
# # 4, drive
# talon2 = CANTalon(2)
# # 1, rotate
# talon3 = CANTalon(3)
# # 3, drive
# talon4 = CANTalon(4)
# # 3, rptate
# talon5 = CANTalon(5)
# # 4, rotate
# talon6 = CANTalon(6)
# # NOTHING???
# talon7 = CANTalon(7)
# # 2, rotate
# talon8 = CANTalon(8)
# # 2, drive

turn_l2 = CANTalon(1)
turn_l2.changeControlMode(CANTalon.ControlMode.Position)
turn_l2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_l2.setPID(1.0, 0.0, 0.0)

turn_r2 = CANTalon(2)
turn_r2.changeControlMode(CANTalon.ControlMode.Position)
turn_r2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_r2.setPID(1.0, 0.0, 0.0)

turn_left = CANTalon(3)
turn_left.changeControlMode(CANTalon.ControlMode.Position)
turn_left.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_left.setPID(1.0, 0.0, 0.0)

turn_right = CANTalon(4)#5
turn_right.changeControlMode(CANTalon.ControlMode.Position)
turn_right.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_right.setPID(1.0, 0.0, 0.0)

dt_right = CANTalon(5)
dt_left = CANTalon(6)

dt_l2 = CANTalon(7)
dt_r2 = CANTalon(8)

limit_r1 = Switch(1, reverse=True)
limit_r2 = Switch(2, reverse=True)
limit_l1 = Switch(3, reverse=True)
limit_l2 = Switch(4, reverse=True)

l_joystick = Attack3Joystick(0)

xbox_controller = XboxJoystick(1)
xbox_controller_2 = XboxJoystick(2)

swerve = SwerveModule(turn_right, turn_r2, turn_left, turn_l2, dt_right, dt_r2, dt_left, dt_l2, 
	limit_r1 = limit_r1, limit_r2 = limit_r2, limit_l1 = limit_l1, limit_l2 = limit_l2)

# Drive Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
hid_sp = SensorPoller((l_joystick, xbox_controller, xbox_controller_2))  # human interface devices
sp = SensorPoller((limit_r1, limit_r2, limit_l1, limit_l2))

new_ac = SwerveController(l_joystick, xbox_controller, swerve)


# Mech Talons, objects, and controller

# define MechController
#mc = MechController(talon1, talon2, talon3, talon4, talon5, talon6, talon7, talon8, driver_stick, xbox_controller)

# define DriverStation
ds = DriverStation.getInstance()





