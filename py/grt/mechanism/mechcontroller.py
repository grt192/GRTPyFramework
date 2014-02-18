class MechController:
    """
    Joystick Map:

    Drive Joystick (intended to be the left one):
        Axis: Drive (duh)
        Button 2: EP In
        Button 3: EP Out

    Non-Drive Joystick (intended to be the right one):
        Left Bumper: Winding Winch
        Right Bumber: Releasing Winch
        Y-Button: Manual Winch Wind
        Left-Stick Y-Axis: Pickup Angle Change
    """

    def __init__(self, driver_joystick, xbox_controller, intake, defense, shooter):
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        self.intake = intake
        self.defense = defense
        self.shooter = shooter
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _driver_joystick_listener(self, sensor, state_id, datum):
        #Pickup -- EP Intake
            if state_id is 'button2':
                if datum:
                    self.intake.start_ep()
                else:
                    self.intake.stop_ep()
            elif state_id is 'button3':
                if datum:
                    self.intake.reverse_ep()
                else:
                    self.intake.stop_ep()

    def _xbox_controller_listener(self, sensor, state_id, datum):

        #Shooter -- Winding winch
            if state_id is 'y_button':
                if datum:
                    self.shooter.winch_wind(1)
                else:
                    self.shooter.winch_stop()
            if state_id is 'l_shoulder':
                if datum:
                    self.shooter.set_angle(0)
        #Shooter -- Releasing Winch
            if state_id is 'r_shoulder':
                if datum:
                    self.shooter.unlatch()
                else:
                    self.shooter.latch()

        #Pickup -- Angle Change
            if state_id is 'l_y_axis':
                self.intake.angle_change(-datum)

            if state_id is 'trigger_pos':
                self.intake.set_ep(int(-datum / .2))
