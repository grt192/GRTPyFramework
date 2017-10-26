class Apple:
    def __init__(self,apple_mech,m1,p1,p2):
        self.m1=m1
        self.p1=p1
        self.p2=p2
        self.apple_mech=apple_mech
    def close_curtain(self):
        self.p1.set(True)
        self.p2.set(True)
    def rotate(self):
        self.m1.set(0.5)
        time.sleep(4)
        self.m1.set(0)
    def close_curtain(self):
        self.p1.set(False)
        self.p2.set(False)