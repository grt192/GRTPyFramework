import wpilib
from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController

#Super Sketch Omega 1
class Mechanisms:

	def __init__(self, joystick, flyMotor1, flyMotor2, shooterMotor):
		self.shooter_pivot_motor = shooterMotor
		self.flywheel_1 = flyMotor1
		self.flywheel_2 = flyMotor2
		self.joystick = joystick
		self.joystick.add_listener(self.flywheel_listener)
		self.joystick.add_listener(self.shooter_pivot_listener)

	def flywheel_listener(self, source, id, datum):
		if id == 'button3' and self.joystick.button3:
			self.flywheel_1.Set(1)
			self.flywheel_2.Set(1)
		elif id == 'button3' and not self.joystick.button3:
			self.flywheel_1.Set(0)
			self.flywheel_2.Set(0)


	def shooter_pivot_listener(self, source, id, datum):
	    if id == 'y_axis':
	        self.shooter_pivot_motor.Set(datum * -0.25)