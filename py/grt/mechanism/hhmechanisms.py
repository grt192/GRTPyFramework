class Elmo:

	def __init__(self, motor):
		self.motor = motor
		self.pneumatic = pneumatic

	def raise_elmo(self):
		self.motor.set(1)

	def start_motor(self, power):
		self.motor.set(power)

	def lower_elmo(self):
		self.motor.set(-1)

	def stop_elmo(self):
		self.motor.set(0)

class HeadPunch:
	#1 motor 1 actuator
	def __init__(self, motor, pneumatic):
		self.motor = motor
		self.pneumatic = pneumatic

	def motor_start(self, power):
		self.motor.set(power)

	def motor_reverse(self):
		self.motor.set(-1)

	def motor_stop(self):
		self.motor.set(0)

	def actuate(self):
		self.pneumatic.set(1)

	def retract(self):
		self.pneumatic.set(0)

class Staircase:
	#1 actuator
	def __init__(self, pneumatic):
		self.pneumatic = pneumatic

	def staircase_up(self):
		self.pneumatic.set(1)

	def staircase_down(self):
		self.pneumatic.set(0)

class HeadlessMonkey:
	#two actuators
	def __init__(self, pneumatic_1, pneumatic_2):
		self.pneumatic_1 = pneumatic_1
		self.pneumatic_2 = pneumatic_2

	def actuate_1(self):
		self.pneumatic_1.set(1)

	def retract_1(self):
		self.pneumatic_1.set(0)

	def actuate_2(self):
		self.pneumatic_2.set(1)

	def retract_2(self):
		self.pneumatic_2.set(0)




