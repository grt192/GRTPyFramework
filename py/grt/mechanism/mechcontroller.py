class MechController:

    def __init__(self, cat_mech, driver_joystick, xbox_controller): # mechanisms belong in arguments
        # define mechanisms here
		self.cat_mech = cat_mech
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if datum:
			self.cat_mech.turn()
		else:
			self.cat_mech.stop_turning()

    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass