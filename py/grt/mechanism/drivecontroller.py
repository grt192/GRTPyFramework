"""
Module for various drivetrain control mechanisms.
Listens to Attack3Joysticks, not wpilib.Joysticks.
"""


class ArcadeDriveController:
    """
    Class for controlling DT in arcade drive mode, with one or two joysticks.
    """

    def __init__(self, dt, l_joystick, r_joystick=None):
        """
        Initialize arcade drive controller with a DT and up to two joysticks.
        """
        self.dt = dt
        self.l_joystick = l_joystick
        self.r_joystick = r_joystick
        l_joystick.add_listener(self._joylistener)
        if r_joystick:
            r_joystick.add_listener(self._joylistener)

    def _joylistener(self, sensor, state_id, datum):
        if sensor in (self.l_joystick, self.r_joystick) and state_id in ('x_axis', 'y_axis'):
            power = -self.l_joystick.y_axis
            turnval = self.r_joystick.x_axis if self.r_joystick else self.l_joystick.x_axis
            # get turn value from r_joystick if it exists, else get it from l_joystick
            self.dt.set_dt_output(power - turnval,
                                  power + turnval)
        elif sensor == self.l_joystick and state_id == 'trigger':
            if datum:
                self.dt.up_shift()
            else:
                self.dt.down_shift()

    def update(self, is_recording = False):
        power = -self.l_joystick.get_y()
        turnval = self.r_joystick.get_x() if self.r_joystick else self.l_joystick.get_x()
        # get turn value from r_joystick if it exists, else get it from l_joystick
        self.dt.set_dt_output(power - turnval,
                                  power + turnval)
        if self.l_joystick.get_trigger():
            self.dt.up_shift()
        elif not self.l_joystick.get_trigger():
            self.dt.down_shift()

        if is_recording:
            self.record()

    def record(self):
        pass        


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
        if sensor in (self.l_joystick, self.r_joystick) and state_id in ('x_axis', 'y_axis'):
            self.dt.set_dt_output(self.l_joystick.y_axis,
                                  self.r_joystick.y_axis)
