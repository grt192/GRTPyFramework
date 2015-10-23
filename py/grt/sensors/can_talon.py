import wpilib

class GRTCANTalon:

	def __init__(self, channel):
		self.t = wpilib.CANTalon(channel)
		self.channel = channel
	def set(self, power):
		self.t.set(power)

	def Get(self):
		return self.t.get()
		print(self.t.Get())

	def GetChannel(self):
		return self.channel