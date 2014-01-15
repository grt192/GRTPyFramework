class AttackMechController:
    def __init__(self, l_joystick, intake):
        self.l_joystick = l_joystick
        self.intake = intake
        l_joystick.add_listener(self._joystick_listener)

    def _joystick_listener(self, sensor, state_id, datum):
        if sensor is self.l_joystick and state_id in ('button2', 'button3'):
            if not datum:
                self.intake.stop_ep()
            elif state_id is 'button2':
                self.intake.start_ep()
            elif state_id is 'button3':
                self.intake.reverse()
