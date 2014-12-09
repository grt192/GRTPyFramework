class Pickup:
	def __init__(self, roller, elev, actuator):
		'''
		roller: the roller motor
		elev: the elevation motor
		actuator: the penumatic
		'''
		self.roller = roller
		self.elev = elev
		self.actuator = actuator
	def roll_in(self):
		self.roller.Set(0.5)
	def roll_out(self):
		self.roller.Set(-0.5)
	def roll_stop(self):
		self.roller.Set(0)
	def extend(self):
		self.actuator.Set(True)
	def retract(self):
		self.actuator.Set(False)
	def up(self):
		self.elev.Set(1)
	def down(self):
		self.elev.Set(-1)
	def elev_stop(self):
		self.elev.Set(0)