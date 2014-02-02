"""
Module for various drivetrain control mechanisms.
Listens to Attack3Joysticks, not wpilib.Joysticks.
"""


class ArcadeDriveController:
    """
    Class for controlling DT in arcade drive mode, with one or two joysticks.
    """

    def __init__(self, dt, joystick1, joystick2=None):
        """
        Initialize arcade drive controller with a DT and up to two joysticks.
        """
        self.dt = dt
        self.joystick1 = joystick1
        self.joystick2 = joystick2
        joystick1.add_listener(self._joylistener)
        if joystick2:
            joystick2.add_listener(self._joylistener)

    def _joylistener(self, sensor, state_id, datum):
        if sensor in (self.joystick1, self.joystick2) and state_id in ('x_axis', 'y_axis'):
            power = -self.joystick1.y_axis
            turnval = self.joystick2.x_axis if self.joystick2 else self.joystick1.x_axis
            # get turn value from joystick2 if it exists, else get it from joystick1
            self.dt.set_dt_output(power + turnval,
                                  power - turnval)


class TankDriveController:
    """
    Class for controlling DT in tank drive mode with two joysticks.
    """

    def __init__(self, dt, l_joystick, r_joystick):
        """
        Initializes self with a DT and left and right joysticks.
        """
        self.dt = dt
        self.l_joystick = l_joystick
        self.r_joystick = r_joystick
        l_joystick.add_listener(self._joylistener)
        r_joystick.add_listener(self._joylistener)

    def _joylistener(self, sensor, state_id, datum):
        if sensor in (self.joystick1, self.joystick2) and state_id in ('x_axis', 'y_axis'):
            self.dt.set_dt_output(self.l_joystick.y_axis,
                                  self.r_joystick.y_axis)
