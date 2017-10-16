"""
Config File for Robot
"""

#@dhruv_rajan is editing config.py
from wpilib import Solenoid, Compressor, DriverStation, DigitalInput
from ctre import CANTalon

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
#from grt.sensors.gyro import Gyro
from grt.sensors.encoder import Encoder
from grt.sensors.talon import Talon
from grt.mechanism.mechcontroller import MechController
from grt.mechanism.apple import Apple
from grt.mechanism.spider import Spider
from grt.mechanism.cookie import Cookie



m1 = CANTalon(11)
p1 = Solenoid(1)
p2 = Solenoid(2)

apple_mech = Apple(m1, p1, p2)

spider_actuator = Solenoid(1)

spider = Spider(spider_actuator)

p3 = Solenoid(3)
cookie = Cookie(p3)


# Drive Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
ac = ArcadeDriveController(dt, driver_stick)
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices



# Mech Talons, objects, and controller

# define MechController
mc = MechController(apple_mech, spider, driver_stick, xbox_controller)

# define DriverStation
ds = DriverStation.getInstance()
