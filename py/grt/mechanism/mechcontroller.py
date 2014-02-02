class AttackMechController:
    def __init__(self, l_joystick, r_joystick, intake, defense, shooter):
        self.l_joystick = l_joystick
        self.r_joystick = r_joystick
        self.intake = intake
        self.defense = defense
        self.shooter = shooter
        l_joystick.add_listener(self._l_joystick_listener)
        r_joystick.add_listener(self._r_joystick_listener)

    def _l_joystick_listener(self, sensor, state_id, datum):
            #Intake Control
            if state_id is 'trigger':
                if datum:
                    self.intake.start_ep()
                else:
                    self.intake.stop_ep()
            elif state_id is 'button3':
                if datum:
                    self.intake.reverse_ep()
                else:
                    self.intake.stop_ep()
            #elif state_id is 'button2':
                #if datum:
                    #self.intake.extend()
                #else:
                    #self.intake.retract()

    def _r_joystick_listener(self, sensor, state_id, datum):
            if state_id is 'trigger':
                if datum:
                    self.shooter.winch_wind(1)
                else:
                    self.shooter.winch_stop()
            elif state_id is 'button2':
                if datum:
                    self.shooter.unlatch()
                else:
                    self.shooter.latch()
                    #Defense Control
            if state_id is 'button11':
                if datum:
                    self.defense.extend()
                else:
                    self.defense.retract()
            elif state_id is 'y_axis':
                self.intake.forward_angle_change(datum)
