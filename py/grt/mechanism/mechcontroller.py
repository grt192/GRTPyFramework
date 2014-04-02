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

    def __init__(self, driver_joystick, xbox_controller, intake, defense, shooter):
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        self.intake = intake
        self.defense = defense
        self.shooter = shooter
        self.shoot_macro = ShootMacro(shooter, intake)
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _driver_joystick_listener(self, sensor, state_id, datum):
        #Pickup -- EP Intake
        if state_id == 'button3':
            if datum:
                self.intake.start_ep()
            else:
                self.intake.stop_ep()
        elif state_id == 'button2':
            #reverse intake
            if datum:
                self.intake.reverse_ep()
            else:
                self.intake.stop_ep()
        elif state_id == 'button6':
            self.intake.angle_change(1.0 if datum else 0)
        elif state_id == 'button9':
            self.intake.angle_change(-1.0 if datum else 0)
        elif state_id == 'button8':
            self.shooter.unlatch()
        elif state_id == 'button7':
            #autoshooting capability for driver on joystick
            if datum and not self.shoot_macro.running:  # start auto shooting on press
                self.shoot_macro.reset()
                self.shoot_macro.run()
            else:  # cancel auto shooting on release
                self.shoot_macro.kill()

    def _xbox_controller_listener(self, sensor, state_id, datum):

        #Shooter -- Winding winch
        if state_id == 'y_button':
            if datum:
                self.shooter.winch_wind(1)
            else:
                self.shooter.winch_stop()
        if state_id == 'l_shoulder':
            if datum:
                self.shooter.winch_wind(1)
        #Shooter -- Releasing Winch
        if state_id == 'r_shoulder':
            if datum and not self.shoot_macro.running:  # start auto shooting on press
                self.shoot_macro.run()
            else:  # cancel auto shooting on release
                self.shoot_macro.kill()
                self.shoot_macro.reset()

        #Shooter -- Winch release backup
        if state_id == 'x_button':
            self.auto_shooting = False
            if datum:
                self.shooter.unlatch()
            else:
                self.shooter.latch()

        #Pickup -- Angle Change
        if state_id == 'l_y_axis':
            if not self.xbox_controller.r_shoulder:
                self.intake.angle_change(-datum)

        if state_id == 'trigger_pos':
            self.intake.set_ep(int(-datum / .2))
