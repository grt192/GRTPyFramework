import wpilib
from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller

class Intake:

	def __init__(self, joystick, epmotor, beltsmotor):

		self.joystick = joystick
		self.epmotor = epmotor
		self.beltsmotor = beltsmotor

		self.joystick.add_listener(self.intake_listener)

	def intake_listener(self, source, id, datum):
		if id == 'button2':
			if datum: 
				self.epmotor.Set(1)
				self.beltsmotor.Set(-1) 
			else:
				self.epmotor.Set(0)
				self.beltsmotor.Set(0)
		elif id == 'button3':
			if datum:
				self.epmotor.Set(-1)
				self.beltsmotor.Set(1)
			else:
				self.epmotor.Set(0)
				self.beltsmotor.Set(0) 