class MechController:

    def __init__(self, driver_joystick, xbox_controller, Opener, Clamp): # mechanisms belong in arguments
        # define mechanisms here
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)
        self.Opener = Opener
        self.Clamp = Clamp


    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id == "x_button":
            if datum:

                self.Clamp.actuateRaise()

        if state_id == "y_button":
            if datum:

                self.Clamp.retractRaise()

        if state_id == "r_shoulder":
            if datum:

                self.Clamp.openClamp()
        if state_id == "l_shoulder":
            if datum:

                self.Clamp.closeClamp()

        if state_id == 'r_y_axis':
            if abs(datum) > 0.05:

                self.Opener.turnOpener(datum)

        #    elif datum < -0.05:
        #        self.Opener.turnOpener(datum)

            else:
                self.Opener.turnOpener(0)

        if state_id == 'l_y_axis':
            if abs(datum) > 0.05:

                self.Opener.moveOpener(datum)

            #elif datum < -0.05:

            #    self.Opener.moveOpener(datum)

            else:
                self.Opener.moveOpener(0)

    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass
