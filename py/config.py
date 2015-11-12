"""
Config File for Robot
"""


from wpilib import Compressor, DriverStation, DigitalInput
import wpilib
import math

from wpilib import Solenoid, Compressor, DriverStation, DigitalInput, CANTalon

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
from grt.core import SensorPoller
from grt.sensors.solenoid import Solenoid
#from grt.sensors.can_talon import CANTalon

from grt.mechanism.mechcontroller import MechController
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController

from record_controller import RecordMacro, PlaybackMacro
from collections import OrderedDict



compressor = Compressor()
compressor.start()


dt_right = CANTalon(1)
dt_r2 = CANTalon(2)
dt_r3 = CANTalon(3)
dt_r4 = CANTalon(4)

dt_left = CANTalon(7)
dt_l2 = CANTalon(8)
dt_l3 = CANTalon(9)
dt_l4 = CANTalon(10)

dt_r2.changeControlMode(CANTalon.ControlMode.Follower)
dt_r3.changeControlMode(CANTalon.ControlMode.Follower)
dt_r4.changeControlMode(CANTalon.ControlMode.Follower)
dt_l2.changeControlMode(CANTalon.ControlMode.Follower)
dt_l3.changeControlMode(CANTalon.ControlMode.Follower)
dt_l4.changeControlMode(CANTalon.ControlMode.Follower)
dt_r2.set(1)
dt_r3.set(1)
dt_r4.set(1)
dt_l2.set(7)
dt_l3.set(7)
dt_l4.set(7)

left_shifter = Solenoid(0)
right_shifter = Solenoid(1)

dt = DriveTrain(dt_left, dt_right, left_shifter=left_shifter, right_shifter=right_shifter)

# Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
ac = ArcadeDriveController(dt, driver_stick)
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices


#mc = MechController(elmo, head_punch, staircase, headless_monkey, skeleton, body_bag, roof, javier, driver_stick, xbox_controller)

ds = DriverStation.getInstance()
