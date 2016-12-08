"""
Config File for Robot
"""

#@dhruv_rajan is editing config.py
from wpilib import Solenoid, Compressor, DriverStation, CANTalon, DigitalInput

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
from grt.mechanism.fmechs import *


#DT Talons and Objects

dt_right = CANTalon(11)
dt_r2 = CANTalon(12)


dt_left = CANTalon(3)
dt_l2 = CANTalon(4)


m1 = CANTalon(1)
m2 = CANTalon(2)
opener_p1 = Solenoid(0)
opener_p2 = Solenoid(2)
ramp_p1 = Solenoid(1)
ramp_p2 = Solenoid(3)
ramp_p3 = Solenoid(4)

opener = Opener(opener_p1, opener_p2, m1, m2)
ramp = Ramp(ramp_p1, ramp_p2, ramp_p3)

dt_r2.changeControlMode(CANTalon.ControlMode.Follower)
# dt_r3.changeControlMode(CANTalon.ControlMode.Follower)
# dt_r4.changeControlMode(CANTalon.ControlMode.Follower)
dt_l2.changeControlMode(CANTalon.ControlMode.Follower)
# dt_l3.changeControlMode(CANTalon.ControlMode.Follower)
# dt_l4.changeControlMode(CANTalon.ControlMode.Follower)
dt_r2.set(11)
# dt_r3.set(1)
# dt_r4.set(1)
dt_l2.set(3)
# dt_l3.set(7)
# dt_l4.set(7)

dt = DriveTrain(dt_left, dt_right, left_encoder=None, right_encoder=None)


#Skeleton sensor poller
#gyro = Gyro(1)
# define sensor poller
# sp = SensorPoller()


# Drive Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
ac = ArcadeDriveController(dt, driver_stick)
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices



# Mech Talons, objects, and controller

# define MechController
mc = MechController(opener, ramp, driver_stick, xbox_controller)

# define DriverStation
ds = DriverStation.getInstance()





