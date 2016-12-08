

class MechController:
	def __init__(self, opener, ramp, driver_joystick, xbox_controller):
		self.driver_joystick = driver_joystick
		self.xbox_controller = xbox_controller
		self.opener = opener
		self.ramp = ramp
		driver_joystick.add_listener(self._driver_joystick_listener)
		xbox_controller.add_listener(self._xbox_controller_listener)

	def _xbox_controller_listener(self, sensor, state_id, datum):
		if state_id == "a_button": 
			if datum:
				self.opener.extend()
		if state_id == "b_button":
			if datum:
				self.opener.retract()
		if state_id == "x_button": 
			if datum:
				self.opener.go_to_drawers()
		if state_id == "y_button":
			if datum:
				self.opener.go_back_from_drawers()
		if state_id == "r_y_axis":
			if abs(datum) > 0.1:
				self.opener.open_1(datum)
				print(datum)
				print("opening drawers")
			else:
				self.opener.open_1(0)
		if state_id == "l_y_axis":
			if abs(datum) > 0.1:
				self.opener.open_2(datum)
			else:
				self.opener.open_2(0)
		
		if state_id == "l_shoulder":
			if datum:
				self.ramp.ramp_down()
		if state_id == "r_shoulder":
			if datum:
				self.ramp.ramp_tilt()

	def _driver_joystick_listener(self, sensor, state_id, datum):
		if state_id == "button2":
			if datum:
				self.ramp.arm_out()
		if state_id == "button3":
			if datum:
				self.ramp.arm_back()
		if state_id == "button4":
			if datum:
				self.ramp.flap_down()
		if state_id == "button5":
			if datum:
				self.ramp.flap_up()

	def _universal_abort_listener(self, sensor, state_id, datum):
		if state_id == 'button8':
			if datum:
				pass