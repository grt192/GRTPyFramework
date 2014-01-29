class AttackMechController:
    def __init__(self, joystick1, joystick2, intake, defense, shooter):
        self.joystick1 = joystick1
        self.joystick2 = joystick2
        self.intake = intake
        self.defense = defense
        self.shooter = shooter
        joystick1.add_listener(self._joystick_listener)
        joystick2.add_listener(self._joystick_listener)


def _joystick_listener(self, sensor, state_id, datum):
        if sensor is self.joystick1:
            #Intake Control
            if state_id is 'trigger':
                if datum:
                    self.intake.start_ep()
                else:
                    self.intake.stop_ep()
            elif state_id is 'button4' or state_id is 'button5':
                if datum:
                    self.intake.reverse_ep()
                else:
                    self.intake.stop_ep()

            elif state_id is 'button3':
                if datum:
                    self.intake.forward_angle_change()
                else:
                    self.intake.stop_angle_change()
            elif state_id is 'button2':
                if datum:
                    self.intake.reverse_angle_change()
                else:
                    self.intake.stop_angle_change()

            #Shooter Control
            elif state_id is 'button10':
                if datum:
                    self.shooter.winch_wind(1)
                else:
                    self.shooter.winch_stop()
            elif state_id is 'button7':
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
        if sensor is self.joystick2:
            #
