from wpilib import CANTalon as wCANTalon

class CANTalon:

	def __init__(self, channel):
		self.t = wCANTalon(channel)
		self.channel = channel
		self.state = 0.0
	def set(self, power):
		self.state = power
		self.t.set(power)

	def get(self):
		return self.state
		#print(self.t.Get())

	def getDeviceID(self):
		return self.channel