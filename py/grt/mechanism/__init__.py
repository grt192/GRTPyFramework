import wpilib

class Shooter:
    out_interval = 0
    motor_power = 1

    def __init__(self, left_motor, right_motor, loading_actuator):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.loading_actuator = loading_actuator

    def start(self):
        self.left_motor.Set(self.motor_power)
        self.right_motor.Set(-self.motor_power)

    def stop(self):
        self.left_motor.Set(0)
        self.right_motor.Set(0)

    def shoot(self):
        self.loading_actuator.Set(1)
        wpilib.Wait(self.out_interval)
        self.loading_actuator.Set(0)

class AngleChange:
    def __init__(self, vertical_motor, horizontal_motor):
        self.vertical_motor = vertical_motor
        self.horizontal_motor = horizontal_motor

    def rotate_horizontal(self, power):
        self.horizontal_motor.Set(power)

    def tilt(self, power):
        self.vertical_motor.Set(power)

    # def _limit_listener(self, source, state_id, datum):
    #     if state_id == 'pressed' and datum:
    #         if source == self.turntable_upper_limit or self.achange_l.Get() < 0:
    #             self.achange_l.Set(0)
    #         if source == self.limit_lr or self.achange_l.Get() > 0:
    #             self.achange_l.Set(0)