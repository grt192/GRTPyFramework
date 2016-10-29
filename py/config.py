from wpilib import Compressor, DriverStation, DigitalInput
import wpilib
import math

from wpilib import Solenoid, Compressor, DriverStation, CANTalon, DigitalInput

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
from grt.core import SensorPoller
#from grt.sensors.solenoid import Solenoid
#from grt.sensors.can_talon import CANTalon

from grt.mechanism.mechcontroller import MechController
from grt.mechanism import *
from grt.mechanism.mechs import *

#from record_controller import RecordMacro, PlaybackMacro
from collections import OrderedDict


# Motors / CANTalons
door_body_motor = CANTalon(12)
stair_mouth_motor = CANTalon(6)
rocking_chair_motor = CANTalon(8)
spike_mouth_motor = CANTalon(4)
cat_motor = CANTalon(7)
marionette_hands_motor1 = CANTalon(10)
marionette_hands_motor2 = CANTalon(11)
spider_motor = CANTalon(9)


# Pneumatic Actuators
bat_actuator = None
door_body_actuator = Solenoid(4)
leaning_out_actuator = Solenoid(2)
spike_mouth_actuator = Solenoid(1)
cat_actuator = None
bloody_hands_actuator1 = Solenoid(0)
bloody_hands_actuator2 = Solenoid(6)
shanked_guy_actuator = None
stair_mouth_actuator = Solenoid(5)

compressor = Compressor()
compressor.start()

bats = Bats(bat_actuator)
door_body = DoorBody(door_body_actuator, door_body_motor)
stair_mouth = StairMouth(stair_mouth_actuator, stair_mouth_motor, cat_motor)
rocking_chair = RockingChair(rocking_chair_motor)
leaning_out = LeaningOut(leaning_out_actuator)
spike_mat = SpikeMat(spike_mouth_actuator, spike_mouth_motor)
cat = Cat(cat_actuator, cat_motor)
marionette_hands = MarionetteHands(marionette_hands_motor1, marionette_hands_motor2)
bloody_hands = BloodyHands(bloody_hands_actuator1, bloody_hands_actuator2)
shanked_guy = ShankedGuy(shanked_guy_actuator)
spider = Spider(spider_motor)





# Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices



mc = MechController(bats, door_body, stair_mouth, rocking_chair, leaning_out, spike_mat, cat, marionette_hands, bloody_hands, shanked_guy, spider, driver_stick, xbox_controller)

ds = DriverStation.getInstance()