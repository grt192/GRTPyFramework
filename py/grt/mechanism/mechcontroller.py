class AttackMechController:
    def __init__(self, l_joystick, intake):
        self.l_joystick = l_joystick
        self.intake = intake
        self.defense = defense
        self.shooter = shooter
        l_joystick.add_listener(self._joystick_listener)

    def _joystick_listener(self, sensor, state_id, datum):
        if sensor is self.l_joystick and state_id in ('button2', 'button3'):
            #Intake Control
            if not datum:
                self.intake.stop_ep()
            elif state_id is 'button2':
                self.intake.start_ep()
            elif state_id is 'button3':
                self.intake.reverse()
        elif sensor in self.l_joystick and state_id in ('button4', 'trigger'):
            #Shooter Control
            if not datum:
                self.shooter.winch_stop()
            elif state_id is 'button4':
                self.shooter.winch_wind(1)
            elif state_id is 'trigger':
                self.shooter.latch()
        elif sensor in self.l_joystick and state_id in ('button8', 'button9', 'button5'):
            #Defense Control
            if not datum:
                self.defense.winch_stop()
            elif state_id is 'button8':
                self.defense.winch_wind(1)
            elif state_id is 'button5':
                self.defense.extend()
            elif state_id is 'button9':
                self.defense.latch() 
