"""
Config File for Robot
"""

#@dhruv_rajan is editing config.py
from wpilib import Solenoid, CANTalon, Compressor, DriverStation, DigitalInput

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
#from grt.sensors.gyro import Gyro
from grt.core import SensorPoller
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset
from grt.sensors.ticker import Ticker
from grt.sensors.encoder import Encoder
from grt.sensors.talon import Talon
from grt.mechanism.mechcontroller import MechController
from grt.mechanism.pickup import Pickup
from grt.mechanism.manual_shooter import ManualShooter

pickup_achange_motor1 = CANTalon(4) #.
pickup_achange_motor2 = CANTalon(4) #.
pickup_achange_motor1.changeControlMode(CANTalon.ControlMode.Follower)
pickup_achange_motor1.set(7) #.
pickup_achange_motor1.reverseOutput(True)

pickup_roller_motor = CANTalon(9) #good
pickup = Pickup(pickup_achange_motor1, pickup_achange_motor2, pickup_roller_motor)
flywheel_motor = CANTalon(8) #good
shooter_act = Solenoid(1)
turntable_motor = CANTalon(12)
manual_shooter = ManualShooter(flywheel_motor, shooter_act, turntable_motor)

#DT Talons and Objects

dt_right = CANTalon(1)#1
#dt_r2 = CANTalon(2)#2
#dt_r3 = CANTalon(3)#3
dt_left = CANTalon(10)#11
#dt_l2 = CANTalon(11)#12
#dt_l3 = CANTalon(12)#13
dt_shifter = Solenoid(0)


#dt_r2.changeControlMode(CANTalon.ControlMode.Follower)
#dt_r3.changeControlMode(CANTalon.ControlMode.Follower)
#dt_l2.changeControlMode(CANTalon.ControlMode.Follower)
#dt_l3.changeControlMode(CANTalon.ControlMode.Follower)
#dt_r2.set(dt_right.getDeviceID())
#dt_r3.set(dt_right.getDeviceID())
#dt_l2.set(dt_left.getDeviceID())
#dt_l3.set(dt_left.getDeviceID())
#dt_r2.set(1)
#dt_r3.set(1)
#dt_l2.set(4)
#dt_l3.set(4)


# shooter1_m1 = CANTalon(11)
# shooter1_m2 = CANTalon(9)



#Skeleton sensor poller
#gyro = Gyro(1)
# define sensor poller
# sp = SensorPoller()
dt = DriveTrain(dt_left, dt_right, left_encoder=None, right_encoder=None)

# Drive Controllers
driver_stick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices

ac = ArcadeDriveController(dt, driver_stick)

# Mech Talons, objects, and controller

# define MechController
mc = MechController(driver_stick, xbox_controller, pickup, manual_shooter)

# define DriverStation
ds = DriverStation.getInstance()





