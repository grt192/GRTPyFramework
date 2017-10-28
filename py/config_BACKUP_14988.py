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
<<<<<<< HEAD
from grt.mechanism.apple import Apple
from grt.mechanism.spider import Spider
=======
from grt.mechanism.cat import Cat
>>>>>>> jonnny



<<<<<<< HEAD
m1 = CANTalon(11)
p1 = Solenoid(1)
p2 = Solenoid(2)

apple_mech = Apple(m1, p1, p2)

spider_actuator = Solenoid(1)

spider = Spider(spider_actuator)
=======
motor = CANTalon(1)


#Skeleton sensor poller
#gyro = Gyro(1)
# define sensor poller
# sp = SensorPoller()
>>>>>>> jonnny


# Drive Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices



# Mech Talons, objects, and controller

cat = Cat(motor)

# define MechController
<<<<<<< HEAD
mc = MechController(apple_mech, spider, driver_stick, xbox_controller)
=======
mc = MechController(cat, driver_stick, xbox_controller)
>>>>>>> jonnny

# define DriverStation
ds = DriverStation.getInstance()
