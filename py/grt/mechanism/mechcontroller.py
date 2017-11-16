class MechController:

    def __init__(self, driver_joystick, xbox_controller, swerve): # mechanisms belong in arguments
        # define mechanisms here
        self.swerve = swerve
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id in ('r_y_axis', 'r_x_axis'):

            
            x = self.xbox_controller.r_x_axis
            y = self.xbox_controller.r_y_axis

            
            if abs(x) > .2 or abs(y) > .2:
                angle = math.atan2(x,-y)
                
                power = math.sqrt(x ** 2 + y ** 2)

                self.swerve.strafe(angle, power, self.strafe_power)

            else:

                self.swerve.set_power(0)


    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass