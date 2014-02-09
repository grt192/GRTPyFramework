class Intake:
    """
    Intake mechanism
    """
    motor_power = .8
    #extender_power = .5

    def __init__(self, roller, angle_changer, angle_solenoid=None):
        self.roller = roller
        self.angle_changer = angle_changer
        self.angle_solenoid = angle_solenoid

    def start_ep(self):
        self.roller.Set(self.motor_power)

    def stop_ep(self):
        self.roller.set(0)

    def reverse_ep(self):
        self.roller.set(-self.motor_power)

    def forward_angle_change(self, power):
        self.angle_changer.set(power)

    def stop_angle_change(self):
        self.angle_changer.set(0)

    def extend(self):
        self.angle_solenoid.Set(1)

    def retract(self):
        self.angle_solenoid.Set(0)


class Shooter:
    """
    Shooter mechanism, using winch.
    Pass winch args to constructor.
    """
    def __init__(self, winchmotor, actuator):
        self.winchmotor = winchmotor
        self.actuator = actuator

    def winch_wind(self, power):
        self.winchmotor.Set(-power)

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
