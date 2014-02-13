class Intake:
    """
    Intake mechanism, with roller motor, two independent angle
    change motors and 4 (left front/rear, right front/rear) limits
    """
    motor_power = .8

    def __init__(self, roller, achange_left, achange_right,
                 achange_limit_lf, achange_limit_lr,
                 achange_limit_rf, achange_limit_rr):
        self.roller = roller
        self.achange_l = achange_left
        self.achange_r = achange_right
        self.limit_lf = achange_limit_lf
        self.limit_lr = achange_limit_lr
        self.limit_rf = achange_limit_rf
        self.limit_rr = achange_limit_rr
        self.limit_lf.add_listener(self._limit_listener)
        self.limit_lr.add_listener(self._limit_listener)
        self.limit_rf.add_listener(self._limit_listener)
        self.limit_rr.add_listener(self._limit_listener)

    def start_ep(self):
        self.roller.Set(self.motor_power)

    def stop_ep(self):
        self.roller.Set(0)

    def reverse_ep(self):
        self.roller.Set(-self.motor_power)

    def angle_change(self, power):
        '''
        Set power of angle change. Power > 1 --> forwards.
        '''
        if power == 0 or\
           power > 0 and not self.achange_limit_lf.pressed or\
           power < 0 and not self.achange_limit.lr.pressed:
            self.achange_left.Set(-power)
        if power == 0 or\
           power > 0 and not self.achange_limit_rf.pressed or\
           power < 0 and not self.achange_limit.rr.pressed:
            self.achange_right.Set(-power)

    def stop_angle_change(self):
        self.angle_changer.Set(0)

    def _limit_listener(self, source, state_id, datum):
        if state_id == 'pressed' and datum:
            if source == self.limit_lf and self.achange_l.Get() > 0:
                self.achange_l.Set(0)
            if source == self.limit_lr and self.achange_l.Get() < 0:
                self.achange_l.Set(0)
            if source == self.limit_rf and self.achange_r.Get() > 0:
                self.achange_r.Set(0)
            if source == self.limit_rr and self.achange_r.Get() < 0:
                self.achange_r.Set(0)


class Shooter:
    """
    Shooter mechanism, using winch.
    Pass winch args to constructor.
    """
    def __init__(self, winch_motor, actuator, potentiometer):
        self.winch_motor = winchmotor
        self.actuator = actuator
        self.potentiometer = potentiometer
        # TODO: Potentiometer logic, limits

    def winch_wind(self, power):
        self.winch_motor.Set(-power)

    def winch_stop(self):
        self.winch_motor.Set(0)

    def latch(self):
        self.actuator.Set(False)

    def unlatch(self):
        self.actuator.Set(True)

    def set_angle(self, target):
        pass
        # TODO: not by Dhruv


class Defense:
    """
    Defense mechanism, using pneumatic solenoid.
    Pass winch args to constructor.
    """
    def __init__(self, solenoid):
        self.solenoid = solenoid

    def extend(self):
        self.solenoid.Set(True)

    def retract(self):
        self.solenoid.Set(False)
