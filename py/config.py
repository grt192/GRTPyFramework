"""
Config File for Robot
"""


from wpilib import Solenoid, Compressor, DriverStation, DigitalInput
import wpilib
import math

from wpilib import Solenoid, Compressor, DriverStation, CANTalon, DigitalInput

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
from grt.core import SensorPoller

from grt.mechanism.mechcontroller import MechController

from record_controller import RecordMacro, PlaybackMacro
from collections import OrderedDict

from grt.mechanism.hhmechanisms import Elmo, HeadPunch, Staircase, HeadlessMonkey


elmo_motor = CANTalon(1)
head_punch_motor = CANTalon(2)

head_punch_actuator = Solenoid(0)
staircase_actuator = Solenoid(1)
headless_linear_act = Solenoid(2)
headless_rotary_act = Solenoid(3)
compressor = Compressor()
compressor.start()

elmo = Elmo(elmo_motor)
head_punch = HeadPunch(head_punch_motor, head_punch_actuator)
staircase = Staircase(staircase_actuator)
headless_monkey = HeadlessMonkey(headless_linear_act, headless_rotary_act)

elmo_arr = [elmo_motor]
head_punch_arr = [head_punch_motor, head_punch_actuator]
staircase_arr = [staircase_actuator]
headless_arr = [headless_linear_act, headless_rotary_act]
record_macro = RecordMacro(elmo_arr)



# Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices


mc = MechController(elmo, head_punch, staircase, headless_monkey, record_macro, driver_stick, xbox_controller)

ds = DriverStation.getInstance()





