import 

#Super Sketch Omega 1
class Mechanisms:

	def __init__(self, joystick, flyMotor1, flyMotor2, shooterMotor):
		self.shooter_pivot_motor = shooterMotor
		self.flywheel_1 = flyMotor1
		self.flywheel_2 = flyMotor2
		self.joystick = joystick

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

	for r in (self.flywheel_listener, self.shooter_pivot_listener):
	    self.joystick.add_listener(r)#Super Sketch Omega 1
	self.shooter_pivot_motor = wpilib.Talon(8)

	self.flywheel_1 = wpilib.Talon(9)
	self.flywheel_2 = wpilib.Talon(10)

	def flywheel_listener(self, source, id, datum):
		if id == 'button3' and self.joystick.button3:
			self.flywheel_1.Set(1)
			self.flywheel_2.Set(1)
		elif id == 'button3' and not self.joystick.button3:
			self.flywheel_1.Set(0)
			self.flywheel_2.Set(0)


	def shooter_pivot_listener(self, id, datum):
	    if id == 'y_axis':
	        self.shooter_pivot_motor.Set(datum * -0.25)

	for r in (self.flywheel_listener, self.shooter_pivot_listener):
	    self.joystick.add_listener(r)