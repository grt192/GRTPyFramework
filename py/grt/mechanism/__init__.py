from grt.core import Constants

constants = Constants()


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

    def set_ep(self, power):
        self.roller.Set(power * self.motor_power)

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
        if power > -.5 or power < .5:
            self.achange_l.Set(0)
            self.achange_r.Set(0)

        if power == 0 or\
           power > 0 and not self.limit_lf.pressed or\
           power < 0 and not self.limit_lr.pressed:
            self.achange_l.Set(-power)
        if power == 0 or\
           power > 0 and not self.limit_rf.pressed or\
           power < 0 and not self.limit_rr.pressed:
            self.achange_r.Set(-power)

    def stop_angle_change(self):
        self.angle_changer.Set(0)

    def _limit_listener(self, source, state_id, datum):
        if state_id == 'pressed' and datum:
            if source == self.limit_lf and self.achange_l.Get() < 0:
                self.achange_l.Set(0)
            if source == self.limit_lr and self.achange_l.Get() > 0:
                self.achange_l.Set(0)
            if source == self.limit_rf and self.achange_r.Get() < 0:
                self.achange_r.Set(0)
            if source == self.limit_rr and self.achange_r.Get() > 0:
                self.achange_r.Set(0)


class Shooter:
    """
    Shooter mechanism, using winch.
    Pass winch args to constructor.
    """
    SP = constants['SP']
    SC = constants['SC']  # uses a constant offset, instead of an integral term
    LIMIT = constants['SLimit']
    target = 0
    autowinding = False

    def __init__(self, winch_motor, actuator, winch_limit, potentiometer):
        self.winch_motor = winch_motor
        self.actuator = actuator
        self.winch_limit = winch_limit
        self.potentiometer = potentiometer

        constants.add_listener(self._constants_listener)
        #potentiometer.add_listener(self._potentiometer_listener)

    def _potentiometer_listener(self, source, state_id, datum):
        '''
        Stops winding if going too far.
        Controls automatic winding if autowinding is enabled.
        '''
        if state_id == 'angle':
            if datum > self.LIMIT or self.winch_limit.presed:
                self.winch_stop()
            elif self.autowinding:
                if datum > self.target:  # passed target
                    self.winch_stop()
                else:
                    self.winch_motor.Set(self.SC + self.SP * (self.target - datum))

    def _constants_listener(self, sensor, state_id, datum):
        if state_id in ('SP', 'SC'):
            self.__dict__[state_id] = datum
        elif state_id == 'SLimit':
            self.LIMIT = datum

    def winch_wind(self, power):
        '''
        Winds the winch. Cancels autowinding when called.
        '''
        self.autowinding = False
        if power >= 0 and self.potentiometer.angle < self.LIMIT and not self.winch_limit.pressed:
            self.winch_motor.Set(-power)

    def winch_stop(self):
        '''
        Stops winding the winch. Cancels autowinding.
        '''
        self.autowinding = False
        self.winch_motor.Set(0)

    def latch(self):
        self.actuator.Set(False)

    def unlatch(self):
        self.actuator.Set(True)

    def set_angle(self, target):
        '''
        Starts automatically winding shooter.
        '''
        self.target = target
        self.autowinding = True


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
