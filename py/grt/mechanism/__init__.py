from grt.core import Constants

constants = Constants()


class Elevator:

    motor_power = .75

    def __init__(self, motor):
        self.motor = motor
        self.set_ep(self.motor_power)

    def set_ep(self, power):
        self.motor.Set(power * self.motor_power)

    def start_ep(self):
        self.motor.Set(self.motor_power)

    def stop_ep(self):
        self.motor.Set(0)

    def reverse_ep(self):
        self.motor.Set(-self.motor_power)

class Intake:

    motor_power = 1

    def __init__(self, roller):
        self.roller = roller
        self.set_ep(self.motor_power)

    def set_ep(self, power):
        self.roller.Set(power * self.motor_power)

    def start_ep(self):
        self.roller.Set(self.motor_power)

    def stop_ep(self):
        self.roller.Set(0)

    def reverse_ep(self):
        self.roller.Set(-self.motor_power)

class PneumaticRelease:

    def __init__(self, pneumatic):
        self.pneumatic = pneumatic

    def release_open(self):
        self.pneumatic.Set(1)

    def release_closed(self):
        self.pneumatic.Set(0)