class MechController:

    def __init__(self, rails_actuator, turntablemotor, driver_joystick, xbox_controller): # mechanisms belong in arguments
        # define mechanisms here

        self.turntablemotor = turntablemotor
        self.rails_actuator = rails_actuator

        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id == "l_x_axis":
            if datum:
                self.turntablemotor.set(-datum*.5)
        if state_id == "x_button":
            if datum:
                self.rails_actuator.set(True)
        if state_id == "y_button":
            if datum:
                self.rails_actuator.set(False)



    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass