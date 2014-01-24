class Intake:
    """
    Intake mechanism
    """
    motor_power = .8
    extender_power = .5

    def __init__(self, roller, extender):
        self.roller = roller
        self.extender = extender  # remainder of code assumes this is a pneumatic

    def start_ep(self):
        self.roller.Set(self.motor_power)

    def stop_ep(self):
        self.roller.Set(0)

    def reverse(self):
        self.roller.Set(-self.motor_power)

    def extend(self):
        self.extender.Set(self.extender_power)

    def stop_extend(self):
        self.extender.Set(0)

    def retract(self):
        self.extender.Set(-self.extender_power)


class Shooter:
    """
    Shooter mechanism, using winch.
    Pass winch args to constructor.
    """
    def __init__(self, winchmotor, actuator):
        self.winchmotor = winchmotor
        self.actuator = actuator

    def winch_wind(self, power):
        self.winchmotor.Set(power)

    def winch_stop(self):
        self.winchmotor.Set(0)

    def latch(self):
        self.actuator.Set(False)

    def unlatch(self):
        self.actuator.Set(True)


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
