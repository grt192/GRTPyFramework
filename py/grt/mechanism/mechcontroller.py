class mechcontroller:
	def __init__(self, intake, joystick):
		self.intake = intake
		self.joystick = joystick
		self.joystick.add_listener(self._joystick_listener)
	def _joystick_listener(self, sensor, state_id, datum):
		if state_id == 'button3':
			if datum:
				self.intake.up()
			else:
				self.intake.elev_stop()
		if state_id == 'button2':
			if datum:
				self.intake.down()
			else:
				self.intake.elev_stop()
		if state_id == 'button4':
			if datum:
				self.intake.extend()
		if state_id == 'button5':
			if datum:
				self.intake.retract()
		if state_id == 'button6':
			if datum:
				self.intake.roll_in()
			else:
				self.intake.roll_stop()
		if state_id == 'button7':
			if datum:
				self.intake.roll_out()
			else:
				self.intake.roll_stop()