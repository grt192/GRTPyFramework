"""
Config File for Robot
"""

#@dhruv_rajan is editing config.py
from wpilib import Solenoid, Compressor, DriverStation, DigitalInput
from ctre import CANTalon

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick

from grt.core import SensorPoller
#from grt.sensors.gyro import Gyro
from grt.sensors.encoder import Encoder
from grt.sensors.talon import Talon
from grt.mechanism.mechcontroller import MechController
from grt.mechanism.spider import Spider
from grt.mechanism.cookie import Cookie


spider_actuator = Solenoid(1)

spider = Spider(spider_actuator)

p3 = Solenoid(1)
cookie = Cookie(p3)


# Drive Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices



# Mech Talons, objects, and controller

# define MechController
mc = MechController(cookie, spider, driver_stick, xbox_controller)

# define DriverStation
ds = DriverStation.getInstance()
