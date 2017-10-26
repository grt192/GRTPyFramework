import time
class Stairmonster:
    def __init__(self,m,p1,p2):
        self.m=m
        self.p1=p1
        self.p2=p2
        t1=0.5 #time needed for plate to reach good position
        t2=4 #time for the monster to stay extended
        t3=4 #time for the monster to stay stowed.
    def open_stair(self):
        self.m.set(0.5) #starts to open the plate
        time.sleep(t1) #opening plate
        self.m.set(0.1) #holds plate in place
    def pop(self):
        self.p1.set(True)
        self.p2.set(True)
        time.sleep(t2)
        self.p1.set(False)
        self.p2.set(False)
    def close_stair(self):
        self.m.set(0)
        time.sleep(t3)