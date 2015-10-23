
class BinStealMech:
	def __init__(self, solenoid1, solenoid2, solenoid3, solenoid4):
		self.solenoid1 = solenoid1
		self.solenoid2 = solenoid2
		self.solenoid3 = solenoid3
		self.solenoid4 = solenoid4
	def extend(self):
		self.solenoid2.set(1)
		self.solenoid1.set(0)

		self.solenoid4.set(1)
		self.solenoid3.set(0)
	def retract(self):
		self.solenoid1.set(1)
		self.solenoid2.set(0)

		self.solenoid4.set(0)
		self.solenoid3.set(1)