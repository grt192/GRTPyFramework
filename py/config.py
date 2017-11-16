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
from grt.mechanism.swerve import Swerve


#DT Talons and Objects

turn_l2 = CANTalon(4) 
turn_l2.changeControlMode(CANTalon.ControlMode.Position)
turn_l2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_l2.setPID(1.0, 0.0, 0.0)

turn_r2 = CANTalon(1)
turn_r2.changeControlMode(CANTalon.ControlMode.Position)
turn_r2.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_r2.setPID(1.0, 0.0, 0.0)

turn_left = CANTalon(5)
turn_left.changeControlMode(CANTalon.ControlMode.Position)
turn_left.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_left.setPID(1.0, 0.0, 0.0)

turn_right = CANTalon(6)#5
turn_right.changeControlMode(CANTalon.ControlMode.Position)
turn_right.setFeedbackDevice(CANTalon.FeedbackDevice.QuadEncoder)
turn_right.setPID(1.0, 0.0, 0.0)


dt_right = CANTalon(9)
dt_left = CANTalon(7)

dt_l2 = CANTalon(3)
dt_r2 = CANTalon(10)


# shooter1_m1 = CANTalon(11)
# shooter1_m2 = CANTalon(9)



#Skeleton sensor poller
#gyro = Gyro(1)
# define sensor poller
# sp = SensorPoller()

swerve = Swerve(turn_right, turn_r2, turn_left, turn_l2, dt_right, dt_r2, dt_left, dt_l2)


# Drive Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices



# Mech Talons, objects, and controller

# define MechController
mc = MechController(driver_stick, xbox_controller, swerve)

# define DriverStation
ds = DriverStation.getInstance()





