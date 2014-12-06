class Pickup:
    def __init__(self, achange_motor, release_pn):
        self.achange_motor = achange_motor
        self.release_pn = release_pn

    def achange_up(self):
        self.achange_motor.Set(-1)

    def achange_down(self):
        self.achange_motor.Set(1)

    def achange_stop(self):
        self.achange_motor.Set(0)

    def release_open(self):
        self.release_pn.Set(1)

    def release_close(self):
        self.release_pn.Set(0)