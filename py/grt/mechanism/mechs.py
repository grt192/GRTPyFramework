import wpilib
from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller

#Super Sketch Omega 1
class Mechanisms:

	def __init__(self, joystick, flyMotor1, flyMotor2, shooterMotor, beltsMotor, epMotor, luna, climber):
		self.shooter_pivot_motor = shooterMotor
		self.flywheel_1 = flyMotor1
		self.flywheel_2 = flyMotor2
		self.belts = beltsMotor
		self.ep = epMotor
		self.luna = luna
		self.climber = climber
		self.joystick = joystick
		self.joystick.add_listener(self.flywheel_listener)
		self.joystick.add_listener(self.shooter_pivot_listener)
		self.joystick.add_listener(self.ep_listener)
		self.joystick.add_listener(self.luna_listener)
		self.joystick.add_listener(self.climber_listener)

	def flywheel_listener(self, source, id, datum):
		if id == 'button3':
			self.flywheel_1.Set(1 if datum else 0)
			self.flywheel_2.Set(1 if datum else 0)

	def ep_listener(self, source, id, datum):
		if id == 'button2':
			self.ep.Set(1 if datum else 0)
			self.belts.Set(-1 if datum else 0)

	def shooter_pivot_listener(self, source, id, datum):
	    if id == 'y_axis':
	        self.shooter_pivot_motor.Set(datum * -0.25)

	def luna_listener(self, source, id, datum):
		if id == 'trigger':
			self.luna.Set(datum)

	def climber_listener(self, source, id, datum):
		if id == 'button4':
			self.climber.Set(datum)