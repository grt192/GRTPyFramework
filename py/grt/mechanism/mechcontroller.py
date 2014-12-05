class MechController:
	def __init__(self, pickup_mech, driver_joystick):
		self.pickup_mech = pickup_mech
		self.driver_joystick = driver_joystick
		driver_joystick.add_listener(self._driver_joystick_listener)

	def _driver_joystick_listener(self, sensor, state_id, datum):
		if state_id == 'button3':
			if datum:
				self.pickup_mech.achange_up()
			else:
				self.pickup_mech.achange_stop()

		if state_id == 'button2':
			if datum:
				self.pickup_mech.achange_down()
			else:
				self.pickup_mech.achange_stop()

		if state_id == 'button4':
			if datum:
				self.pickup_mech.release_open()

		if state_id == 'button5':
			if datum:
				self.pickup_mech.release_close()