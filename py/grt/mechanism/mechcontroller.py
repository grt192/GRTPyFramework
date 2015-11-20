class MechController:

    def __init__(self, driver_joystick, xbox_controller, pickupshooter): # mechanisms belong in arguments
        # define mechanisms here
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        self.pickupshooter = pickupshooter
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id == "a_button":
            if datum:
                self.pickupshooter.start(1)
        if state_id == "b_button":
            if datum:
                self.pickupshooter.start(-1)
        if state_id == "x_button":
            if datum:
                self.pickupshooter.stop()

    def _driver_joystick_listener(self, sensor, state_id, datum):
        
        pass