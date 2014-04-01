import threading
import time


class MechController:
    """
    Joystick Map:

    Drive Joystick (intended to be the left one):
        Axis: Drive (duh)
        Button 2: EP in
        Button 3: EP out

    Xbox Controller (intended to be the right one):
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
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _driver_joystick_listener(self, sensor, state_id, datum):
        #Pickup -- EP Intake
        if state_id is 'button2':
            if datum:
                self.intake.start_ep()
            else:
                self.intake.stop_ep()
        elif state_id is 'button4':
            #reverse intake
            if datum:
                self.intake.reverse_ep()
            else:
                self.intake.stop_ep()
        elif state_id is 'button3':
            #autoshooting capability for driver on joystick
            if datum:  # start auto shooting on press

                def autoshoot():
                    self.auto_shooting = True
                    while self.auto_shooting and not (self.intake.limit_lf.pressed
                                                      and self.intake.limit_rf.pressed):
                        time.sleep(.05)
                    if self.auto_shooting:
                        self.shooter.unlatch()
                        time.sleep(.5)
                        self.shooter.latch()
                        self.auto_shooting = False

                if not self.auto_shooting:
                    self.intake.angle_change(1)
                    threading.Thread(target=autoshoot).start()

            else:  # cancel auto shooting on release
                self.auto_shooting = False
                self.intake.angle_change(0)

    def _xbox_controller_listener(self, sensor, state_id, datum):

        #Shooter -- Winding winch
        if state_id is 'y_button':
            if datum:
                self.shooter.winch_wind(1)
            else:
                self.shooter.winch_stop()
        if state_id is 'l_shoulder':
            if datum:
                self.shooter.winch_wind(1)
        #Shooter -- Releasing Winch
        if state_id is 'r_shoulder':
            if datum:  # start auto shooting on press

                def autoshoot():
                    self.auto_shooting = True
                    while self.auto_shooting and not (self.intake.limit_lf.pressed
                                                      and self.intake.limit_rf.pressed):
                        time.sleep(.05)
                    if self.auto_shooting:
                        self.shooter.unlatch()
                        time.sleep(.5)
                        self.shooter.latch()
                        self.auto_shooting = False

                if not self.auto_shooting:
                    self.intake.angle_change(1)
                    threading.Thread(target=autoshoot).start()

            else:  # cancel auto shooting on release
                self.auto_shooting = False
                self.intake.angle_change(0)

        #Shooter -- Winch release backup
        if state_id is 'x_button':
            self.auto_shooting = False
            if datum:
                self.shooter.unlatch()
            else:
                self.shooter.latch()

        #Pickup -- Angle Change
        if state_id is 'l_y_axis':
            if not self.xbox_controller.r_shoulder:
                self.intake.angle_change(-datum)

        if state_id is 'trigger_pos':
            self.intake.set_ep(int(-datum / .2))
