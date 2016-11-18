class Opener:
    def __init__(self, p1, p2, m1, m2):
        self.p1 = p1
        self.p2 = p2
        self.m1 = m1
        self.m2 = m2
    def extend(self):
        self.p1.set(1)
    def retract(self):
        self.p1.set(0)
    def go_to_drawers(self):
        self.p2.set(1)
    def open_drawers(self, power):
        self.m1.set(power)
        self.m2.set(power)

class Ramp:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def arm_out(self):
        self.p1.set(1)
    def arm_back(self):
        self.p1.set(0)
    def flap_down(self)
        self.p2.set(1)
    def ramp_tilt(self)
        self.p3.set(1)
    def ramp_down(self)
        self.p3.set(0)