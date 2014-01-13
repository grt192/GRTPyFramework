__author__ = 'dhruv'

class Attack3MechController:
    """
    Class for controlling DT in drive mode, with one or two joysticks
    """
    def __init__(self, joystick1, joystick2, intake, shooter, catcher, defense):
        """
        Initialize arcade drive controller with a DT and up to two joysticks.
        """

        self.joystick1 = joystick1
        self.joystick2 = joystick2
        self.intake = intake
        self.shooter = shooter
        self.catcher = catcher
        self.defense = defense

        self.joystick1.add_listener(self._joy1listener)
        self.joystick2.add_listener(self._joy2listener)

    def _joy1listener(self, sensor, state_id, datum):
        if state_id == 'button2':
            if datum:
                self.intake.start_ep()
            else:
                self.intake.end_ep()
        elif state_id == 'button3':
            if datum:
                self.intake.reverse()
            else:
                self.intake.end_ep()