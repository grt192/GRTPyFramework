<<<<<<< HEAD
class MechController:
    def __init__(self, elevator, intake, driver_joystick):
        self.elevator = elevator
        self.intake = intake
        self.driver_joystick = driver_joystick
        driver_joystick.add_listener(self._driver_joystick_listener)

    def _driver_joystick_listener(self, sensor, state_id, datum):
        #elevator
        if state_id == 'button2':
            if datum:
                self.elevator.start_ep()
            else:
                self.elevator.stop_ep()

        #elevator reverse
        if state_id == 'button3':
            if datum:
                self.elevator.reverse_ep()
            else:
                self.elevator.stop_ep()

        #intake
        if state_id == 'button4':
            if datum:
                self.intake.start_ep()
            else:
                self.intake.stop_ep()

        #intake reverse
        if state_id == 'button5':
            if datum:
                self.intake.reverse_ep()
            else:
                self.intake.stop_ep()

        #RELEASE THE PNEUMATICS
        if state_id == 'button6':
            if datum:
                self.elevator.release_open()

        if state_id == 'button7':
            if datum:
                self.elevator.release_close()
=======
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
>>>>>>> cc5efce64613d916322c687868b2b8ec27cb494e
