from pyfrc import wpilib

class Talon:

	def __init__(self, channel):
		self.t = wpilib.Talon(channel)
		self.channel = channel
	def Set(self, power):
		self.t.Set(power)

	def Get(self):
		return self.t.Get()

	def GetChannel(self):
		return self.channel