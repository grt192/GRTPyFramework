"""
Config File for Robot
"""

#@dhruv_rajan is editing config.py
from wpilib import Solenoid, Compressor, DriverStation, CANTalon

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
from grt.mechanism.GMechs import *


#DT Talons and Objects

dt_right = CANTalon(1)
dt_r2 = CANTalon(2)
#dt_r3 = CANTalon(3)
#dt_r4 = CANTalon(4)

dt_left = CANTalon(3)
dt_l2 = CANTalon(4)
#dt_l3 = CANTalon(9)
#dt_l4 = CANTalon(10)

dt_r2.changeControlMode(CANTalon.ControlMode.Follower)
#dt_r3.changeControlMode(CANTalon.ControlMode.Follower)
#dt_r4.changeControlMode(CANTalon.ControlMode.Follower)
dt_l2.changeControlMode(CANTalon.ControlMode.Follower)
#dt_l3.changeControlMode(CANTalon.ControlMode.Follower)
#dt_l4.changeControlMode(CANTalon.ControlMode.Follower)
dt_r2.set(3)
#dt_r3.set(1)
#dt_r4.set(1)
dt_l2.set(1)
#dt_l3.set(3)
#dt_l4.set(3)

dt = DriveTrain(dt_left, dt_right, left_encoder=None, right_encoder=None)

om_open = CANTalon(5)
om_move = CANTalon(6)
pu_open = Solenoid(0)
pu_up = Solenoid(1)

om = Opener(om_open, om_move)
pu = Clamp(pu_up, pu_open)

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
mc = MechController(driver_stick, xbox_controller, om, pu)

# define DriverStation
ds = DriverStation.getInstance()
