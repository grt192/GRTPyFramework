import time

class StairMonster:
    def __init__(self,m,p1,p2):
        self.m=m
        self.p1=p1
        self.p2=p2
        self.t1=0.5 #time needed for plate to reach good position
        self.t2=4 #time for the monster to stay extended
        self.t3=0.5 #time for stair to close

    def open_stair(self):
        print("open stair")
        self.m.set(0.5) #starts to open the plate
        time.sleep(self.t1) #opening plate
        self.m.set(0) #holds plate in place

    def pop(self):
        self.p1.set(True)
        self.p2.set(True)
        time.sleep(self.t2)
        self.p1.set(False)
        self.p2.set(False)

    def close_stair(self):
        print("close stair")
        self.m.set(-0.2)
        time.sleep(self.t3)
        self.m.set(0)