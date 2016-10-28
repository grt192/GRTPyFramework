class Bats:

    def __init__(self, pneumatic):

        self.pneumatic = pneumatic

    def actuate(self):
        self.pneumatic.set(1)

    def retract(self):
        self.pneumatic.set(0)

class DoorBody:

#negative power to bring homer up

    def __init__(self, pneumatic, motor):

        self.pneumatic = pneumatic
        self.motor = motor

    def actuate(self):
        self.pneumatic.set(1)

    def retract(self):
        self.pneumatic.set(0)

    def set_motor(self, power):
        self.motor.set(power)

class StairMouth:

    def __init__(self, pneumatic, motor):

        self.pneumatic = pneumatic
        self.motor = motor

    def actuate(self):
        self.pneumatic.set(1)

    def retract(self):
        self.pneumatic.set(0)

    def set_motor(self, power):
        self.motor.set(power)

    def mouth_and_eyes(self,power):
        self.motor.set(power)
        self.pneumatic.set(1)

class RockingChair:

    def __init__(self,motor):
        self.motor = motor

    def set_motor(self,power):
        self.motor.set(power)

class LeaningOut:

    def __init__(self, pneumatic):

        self.pneumatic = pneumatic

    def actuate(self):
        self.pneumatic.set(1)

    def retract(self):
        self.pneumatic.set(0)

class SpikeMat:

    def __init__(self, pneumatic, motor):

        self.pneumatic = pneumatic
        self.motor = motor

    def actuate(self):
        self.pneumatic.set(1)

    def retract(self):
        self.pneumatic.set(0)


class Cat:

# NOTE: positive turns the cat alive, negative power kills it

    def __init__(self, pneumatic, motor):

        self.pneumatic = pneumatic
        self.motor = motor

    def actuate(self):
        self.pneumatic.set(1)

    def retract(self):
        self.pneumatic.set(0)

    def set_motor(self, power):
        self.motor.set(power)

class MarionetteHands:

    def __init__(self, motor1, motor2):

        self.motor1 = motor1
        self.motor2 = motor2

    def set_motor1(self,power):
        self.motor1.set(power)

    def set_motor2(self,power):
        self.motor2.set(-power)

    def set_all(self,power):

        self.motor1.set(power)
        self.motor2.set(-power)

class BloodyHands:

    def __init__(self, pneumatic1, pneumatic2):

        self.pneumatic1 = pneumatic1
        self.pneumatic2 = pneumatic2

    def actuate_1(self):
        self.pneumatic1.set(1)

    def retract_1(self):
        self.pneumatic1.set(0)

    def actuate_2(self):
        self.pneumatic2.set(1)

    def retract_2(self):
        self.pneumatic2.set(0)

class ShankedGuy:

    def __init__(self, pneumatic):

        self.pneumatic = pneumatic

    def actuate(self):
        self.pneumatic.set(1)

    def retract(self):
        self.pneumatic.set(0)

