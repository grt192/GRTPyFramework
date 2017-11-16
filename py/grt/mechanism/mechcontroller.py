class MechController:

    def __init__(self, dt1, driver_joystick, xbox_controller): # mechanisms belong in arguments
        # define mechanisms here
        self.dt1 = dt1
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id == 'a_button':
            if datum:
                print("a_button")
                self.dt1.set(.5)


    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass