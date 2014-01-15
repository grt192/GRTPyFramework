class Intake:
    """
    Intake mechanism
    """
    motor_power = .8

    def __init__(self, roller, extender):
        self.roller = roller
        self.extender = extender  # remainder of code assumes this is a pneumatic

    def start_ep(self):
        self.roller.Set(self.motor_power)

    def end_ep(self):
        self.roller.Set(0)

    def reverse(self):
        self.roller.Set(-self.motor_power)

    def extend(self):
        self.extender.Set(True)

    def retract(self):
        self.extender.Set(False)


class Winch:
    """
    Winch mechanism
    """
    def __init__(self, winchmotor, actuator):
        self.winchmotor = winchmotor
        self.actuator = actuator

    def winch_wind(self, power):
        self.winchmotor.Set(power)

    def winch_stop(self):
        self.winchmotor.Set(0)

    def release(self):
        self.actuator.Set(True)

    def unrelease(self):
        self.actuator.Set(False)


class Shooter:
    """
    Shooter mechanism, using winch.
    Pass winch args to constructor.
    """
    def __init__(self, *args):
        self.winch = Winch(*args)
        self.winch_wind = self.winch.winch_wind
        self.winch_stop = self.winch.winch_stop
        self.extend = self.winch.release
        self.latch = self.winch.unrelease


class Defense:
    """
    Defense mechanism, using winch.
    Pass winch args to constructor.
    """
    def __init__(self, *args):
        self.winch = Winch(*args)
        self.winch_wind = self.winch.winch_wind
        self.winch_stop = self.winch.winch_stop
        self.extend = self.winch.release
        self.latch = self.winch.unrelease
