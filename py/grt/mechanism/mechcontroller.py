class AttackMechController:
    def __init__(self, l_joystick, intake, defense, shooter):
        self.l_joystick = l_joystick
        self.intake = intake
        self.defense = defense
        self.shooter = shooter
        l_joystick.add_listener(self._joystick_listener)

    def _joystick_listener(self, sensor, state_id, datum):
        if sensor is self.l_joystick:
            #Intake Control
            if state_id is 'button2':
                if datum:
                    self.intake.start_ep()
                else:
                    self.intake.stop_ep()
            elif state_id is 'button3':
                if datum:
                    self.intake.reverse()
                else:
                    self.intake.stop_ep()

            elif state_id is 'button5':
                if datum:
                    self.intake.extend()
                else:
                    self.intake.stop_extend()
            elif state_id is 'button4':
                if datum:
                    self.intake.retract()
                else:
                    self.intake.stop_extend()

            #Shooter Control
            elif state_id is 'button7':
                if datum:
                    self.shooter.winch_wind(1)
                else:
                    self.shooter.winch_stop()
            elif state_id is 'trigger':
                if datum:
                    self.shooter.unlatch()
                else:
                    self.shooter.latch()

            #Defense Control
            if state_id is 'button8':
                if datum:
                    self.defense.extend()
                else:
                    self.defense.retract()
