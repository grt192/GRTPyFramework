__author__ = "Trevor Nielsen"

class Pickup:
	"""
	Describes the squarePickup mechanism.
	"""

	scale_factor = .8

	def __init__(self, roller, joystick):
		self.roller = roller
		self.joystick = joystick
		joystick.add_listener(self._joystick_listener)

	def _joystick_listener(self, sensor, state_id, datum):
		if sensor is self.joystick and state_id in ('button2', 'button3'):
			if not datum:
				self.roller.Set(0)
			elif state_id is 'button2':
				self.roller.Set(self.scale_factor)
			elif state_id is 'button3':
				self.roller.Set(-self.scale_factor)