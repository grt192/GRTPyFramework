class Cat:
	def __init__(self, motor):
		self.motor = motor
		
	def turn(self):
		self.motor.set(0.5)
		
	def stop_turning(self):
		self.motor.set(0)