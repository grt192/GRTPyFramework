class MechController:

    def __init__(self, apple_mech, driver_joystick, xbox_controller): # mechanisms belong in arguments
        # define mechanisms here
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        self.apple_mech = apple_mech
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        pass
        if state_id = 'a_botton'
            if datum:
                self.apple_mech.close_curtains()
                time.sleep(.5)
                self.apple_mech.rotate()
                time.sleep(.5)
                self.apple_mech.open_curtains()
                time.sleep(.5)
                

    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass