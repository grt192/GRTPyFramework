from grt.macro.shoot_macro import ShootMacro


class MechController:
    """
    Joystick Map:

    Drive Joystick:
        Button 2: EP out
        Button 3: EP in
        Button 6: AC out
        Button 7: Autoshoot
        Button 8: Winch Release
        Button 9: AC in

    Xbox Controller:
        Left Bumper: Winding winch
        Right Bumper: Lower pickup and releasing winch
        X-Button: Manual winch release
        Y-Button: Manual winch wind
        Left-Stick Y-Axis: Pickup angle change
    """
    auto_shooting = False

    def __init__(self, driver_joystick, xbox_controller, shooter, angle_change):
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        self.angle_change = angle_change
        self.shooter = shooter
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass

    def _xbox_controller_listener(self, sensor, state_id, datum):

        #Shooter
        if state_id == 'y_button':
            if datum:
                self.shooter.start()
            else:
                self.shooter.stop()

        if state_id == 'a_button':
            if datum:
                self.shooter.shoot()

        #Angle Change
        if state_id == 'r_x_axis':
            if datum:
                self.angle_change.tilt(datum)
        if state_id == 'r_y_axis':
            if datum:
                self.angle_change.rotate_horizontal(datum)
