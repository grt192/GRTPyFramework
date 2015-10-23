from grt.macro.fourbar_macro import FourBarMacro

class Pickup:
    def __init__(self, clamp_pn):
        self.clamp_pn = clamp_pn

    def pickup(self):
        self.clamp_pn.set(1)

    def release(self):
        self.clamp_pn.set(0)

class FourBar:
    def __init__(self, fourbar_motor, fourbar_encoder=None):
        self.fourbar_motor = fourbar_motor
        self.fourbar_encoder = fourbar_encoder
        self.fourbar_macro = FourBarMacro(self)

    def elevate(self):
        self.fourbar_motor.set(.7)

    def lower(self):
        self.fourbar_motor.set(-.5)

    def stop(self):
        self.fourbar_motor.set(0)

    def elevate_speed(self, power):
        self.fourbar_motor.set(power)

    def set_state(self, state):
        self.fourbar_macro.lift_to(state)

    def lower_step(self):
        self.step_logic(-1)
    def raise_step(self):
        self.step_logic(1)

    def step_logic(self, steps):
        current_index = list(self.lift_macro.STATE_DICT.keys()).index(self.lift_macro.current_state)
        adjusted_index = current_index + steps
        print(current_index)
        if adjusted_index >= 0: #Prevents wrap-around
            try:
                self.lift_macro.current_state = list(self.lift_macro.STATE_DICT.keys())[adjusted_index]
                self.lift_macro.setpoint = list(self.lift_macro.STATE_DICT.values())[adjusted_index]
            except IndexError:
                pass

class TwoMotorPickup:
    def __init__(self, motor1, motor2):
        self.motor1 = motor1
        self.motor2 = motor2

    def operate(self, power):
        self.motor1.set(power)
        self.motor2.set(-power)
    def stop(self):
        self.motor1.set(0)
        self.motor2.set(0)