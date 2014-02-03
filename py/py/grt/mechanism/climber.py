import wpilib
from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller

class Climber:

	def __init__(self, joystick, climber):
		self.joystick = joystick
		self.climber = climber

		self.joystick.add_listener(self.climber_listener)


	def climber_listener(self, source, id, datum):
		if id == 'button4':
			self.climber.Set(datum)
