class ManualShooter:

	def __init__(self, flywheel_motor, shooter_act, turntable_motor):
		self.flywheel_motor = flywheel_motor
		self.shooter_act = shooter_act
		self.turntable_motor = turntable_motor

	def turn(self, power):
		self.turntable_motor.set(power)

	def spin_flywheel(self, power):
		self.flywheel_motor.set(power)
	def shooter_down(self):
		self.shooter_act.set(True)
	def shooter_up(self):
		self.shooter_act.set(False)