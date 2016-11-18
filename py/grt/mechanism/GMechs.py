class Opener:

    def __init__(self, motor1, motor2):

        self.motor1 = motor1
        self.motor2 = motor2

    def turnOpener(self, power):
        self.motor1.set(power)

    def moveOpener(self, power):
        self.motor2.set(power)

class Clamp:

    def __init__(self, pneumatic1, pneumatic2):

        self.updown = pneumatic1
        self.open = pneumatic2

    def actuateRaise(self):
        self.updown.set(1)

    def retractRaise(self):
        self.updown.set(0)

    def openClamp(self):
        self.open.set(1)

    def closeClamp(self):
        self.open.set(0)
