"""
Field-Centric Drive Controller
For now, takes the joystick values (x, y), converts them into polar form (r, theta),
and then factors in the gyro angle.
"""

class CentricDriveController:
    def __init__(self, dt, move_joystick):
        """
        Initialize arcade drive controller with a DT and up to two joysticks.
        """
        self.dt = dt
        self.move_joystick = move_joystick
        move_joystick.add_listener(self._joylistener)


    def _joylistener(self, sensor, state_id, datum):
        if sensor == self.move_joystick and state_id in ('x_axis', 'y_axis'):
            #power = -self.l_joystick.y_axis
            #turnval = self.r_joystick.x_axis if self.r_joystick else self.l_joystick.x_axis
            # get turn value from r_joystick if it exists, else get it from l_joystick
            #self.dt.set_dt_output(power - turnval, power + turnval)
            """
            This assumes north to be 0 degrees and degrees to be positive going clockwise.
            """
            magnitude = self.move_joystick.magnitude
            desired_direction = self.move_joystick.direction
            current_direction = 0 #self.dt.gyro.angle
            direction = desired_direction - current_direction
            rotation = self.move_joystick.twist_axis
            print(str(rotation))
            self.dt.set_dt_output(magnitude, direction, rotation)



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
