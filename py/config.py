"""
Config File for Robot
"""

#@dhruv_rajan is editing config.py
from wpilib import Solenoid, Compressor, DriverStation, DigitalInput
from ctre import CANTalon

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
# from grt.sensors.gyro import Gyro
from grt.core import SensorPoller
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset
from grt.sensors.ticker import Ticker
from grt.sensors.encoder import Encoder
from grt.sensors.talon import Talon
from grt.mechanism.mechcontroller import MechController
from grt.mechanism.apple import Apple
from grt.mechanism.big_ghost import BigGhost
from grt.mechanism.cookie import Cookie
from grt.mechanism.giraffe import Giraffe
from grt.mechanism.spider import Spider

apple_motor = CANTalon(11)
apple_p1 = Solenoid(0)
apple_p2 = Solenoid(1)
apple_mech = Apple(apple_motor, apple_p1, apple_p2)

spider_p1 = Solenoid(2)
spider = Spider(spider_p1)

cookie_p1 = Solenoid(3)
cookie = Cookie(cookie_p1)

big_ghost_p1 = Solenoid(4)
big_ghost = BigGhost(big_ghost_p1)

giraffe_p1 = Solenoid(5)
giraffe = Giraffe(giraffe_p1)


# Drive Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)

# ac = ArcadeDriveController(dt, driver_stick)
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices



# Mech Talons, objects, and controller

# define MechController

mc = MechController(apple, cookie, spider, big_ghost, giraffe, driver_stick, xbox_controller)

# define DriverStation
ds = DriverStation.getInstance()
