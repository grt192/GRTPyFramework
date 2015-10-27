"""
Config File for Robot
"""


from wpilib import Compressor, DriverStation, DigitalInput
import wpilib
import math

from wpilib import Solenoid, Compressor, DriverStation, DigitalInput

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
from grt.core import SensorPoller
from grt.sensors.solenoid import Solenoid
from grt.sensors.can_talon import CANTalon

from grt.mechanism.mechcontroller import MechController
from grt.mechanism import *

from record_controller import RecordMacro, PlaybackMacro
from collections import OrderedDict


# Motors / CANTalons
skeleton_motor = CANTalon(1)
head_punch_motor = CANTalon(2)
elmo_motor = CANTalon(3)
body_bag_motor = CANTalon(4)

# Pneumatic Actuators
javier_actuator = Solenoid(0)
roof_actuator = Solenoid(1)
staircase_actuator = Solenoid(2)
skeleton_actuator = Solenoid(3)
head_punch_actuator = Solenoid(4)
body_bag_actuator = Solenoid(5)
headless_linear_act = Solenoid(6)
headless_rotary_act = Solenoid(7)

compressor = Compressor()
compressor.start()

elmo = Elmo(elmo_motor)
javier = Javier(javier_actuator)
roof = Roof(roof_actuator)
head_punch = HeadPunch(head_punch_motor, head_punch_actuator)
staircase = Staircase(staircase_actuator)
headless_monkey = HeadlessMonkey(headless_linear_act, headless_rotary_act)
skeleton = Skeleton(skeleton_motor, skeleton_actuator)
body_bag = BodyBag(body_bag_motor,body_bag_actuator)

# elmo_arr = [elmo_motor]
# head_punch_arr = [head_punch_motor, head_punch_actuator]
# staircase_arr = [staircase_actuator]
# headless_arr = [headless_linear_act, headless_rotary_act]
# record_macro = RecordMacro(headless_arr)



# Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices

#elmo, headpunch, staircase, headless_monkey, skeleton, body_bag, record_macro, driver_joystick, xbox_controller

mc = MechController(elmo, head_punch, staircase, headless_monkey, skeleton, body_bag, roof, javier, driver_stick, xbox_controller)

ds = DriverStation.getInstance()
