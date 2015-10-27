from wpilib import Solenoid as wSolenoid

class Solenoid:
	def __init__(self, channel):
		self.s = wSolenoid(channel)
		self.channel = channel
		self.state = False
	def set(self, state):
		self.state = state
		self.s.set(state)
	def get(self):
		return self.state
	def getDeviceID(self):
		return self.channel