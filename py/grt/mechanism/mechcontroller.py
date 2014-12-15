class MechController:
    def __init__(self, elevator, intake, pn, driver_joystick):
        self.elevator = elevator
        self.intake = intake
        self.pn = pn
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
                self.pn.release_open()

        if state_id == 'button7':
            if datum:
                self.pn.release_close()