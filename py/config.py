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
from grt.mechanism.cat import Cat
from grt.mechanism.apple import Apple
from grt.mechanism.big_ghost import BigGhost
from grt.mechanism.cookie import Cookie
from grt.mechanism.giraffe import Giraffe
from grt.mechanism.spider import Spider
from grt.mechanism.hand import Hand
from grt.mechanism.stair_monster import StairMonster

apple_motor = CANTalon(11)
apple_p1 = Solenoid(0)
apple_p2 = Solenoid(1)
apple = Apple(apple_motor, apple_p1, apple_p2)

spider_p1 = Solenoid(2)
spider = Spider(spider_p1)

cookie_p1 = Solenoid(3)
cookie = Cookie(cookie_p1)

big_ghost_p1 = Solenoid(4)
big_ghost = BigGhost(big_ghost_p1)

giraffe_p1 = Solenoid(5)
giraffe = Giraffe(giraffe_p1)

# hand_p1 = Solenoid(6)
# hand_mech = Hand(hand_p1)
hand = None

cat_motor = CANTalon(1)


#Skeleton sensor poller
#gyro = Gyro(1)
# define sensor poller
# sp = SensorPoller()


stair_motor = CANTalon(0)
stair_p1 = Solenoid(6)
stair_p2 = Solenoid(7)
stair_monster = StairMonster(stair_motor, stair_p1, stair_p2)

# Drive Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)

# ac = ArcadeDriveController(dt, driver_stick)
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices



# Mech Talons, objects, and controller

cat = Cat(cat_motor)

# define MechController

mc = MechController(apple, cookie, spider, big_ghost, giraffe, hand, stair_monster, cat, driver_stick, xbox_controller)

# define DriverStation
ds = DriverStation.getInstance()
