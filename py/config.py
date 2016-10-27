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

#from record_controller import RecordMacro, PlaybackMacro
from collections import OrderedDict


# Motors / CANTalons
door_body_motor = CANTalon(1)
stair_mouth_motor = CANTalon(2)
rocking_chair_motor = CANTalon(3)
spike_mouth_motor = CANTalon(4)
cat_motor = CANTalon(5)
marionette_hands_motor1 = CANTalon(6)
marionette_hands_motor2 = CANTalon(7)


# Pneumatic Actuators
#bat_actuator = Solenoid(0)
door_body_actuator = Solenoid(1)
leaning_out_actuator = Solenoid(2)
spike_mouth_actuator = Solenoid(4)
cat_actuator = Solenoid(5)
body_bag_actuator = Solenoid(6)
bloody_hands_actuator2 = Solenoid(7)
shanked_guy_actuator = Solenoid(0)

compressor = Compressor()
compressor.start()

bats = Bats(bat_actuator)
door_body = DoorBody(door_body_actuator, door_body_motor)
stair_mouth = StairMouth(stair_mouth_actuator, stair_mouth_motor)
rocking_chair = RockingChair(rocking_chair_motor)
leaning_out = LeaningOut(leaning_out_actuator)
spike_mat = SpikeMat(spike_mouth_actuator, spike_mouth_motor)
cat = Cat(cat_actuator, cat_motor)
marionette_hands = MarionetteHands(marionette_hands_motor1, marionette_hands_motor2)
bloody_hands = BloodyHands(bloody_hands_actuator1, bloody_hands_actuator2)
shanked_guy = ShankedGuy(shanked_guy_actuator)





# Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices



mc = MechController(bats, door_body, stair_mouth, rocking_chair, leaning_out, spike_mat, cat, marionette_hands, bloody_hands, shanked_guy, driver_stick, xbox_controller)

ds = DriverStation.getInstance()