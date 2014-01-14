__author__ = "Trevor Nielsen"

class Pickup:
	"""
	Describes the squarePickup mechanism.
	"""

	def __init__(self, roller, joystick):
		self.roller = roller
		self.joystick = joystick
		joystick.add_listener(self._joystick_listener)

	def _joystick_listener(self, sensor, state_id, datum):
		if not datum:
			self.roller.Set(0)
		elif state_id is 'button2':
			self.roller.Set(.5)
		else:
			self.roller.Set(-.5)