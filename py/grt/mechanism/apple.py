import time

class Apple:
    def _init_(self, m1, p1, p2):
        self.m1 = m1
        self.p1 = p1
        self.p2 = p2
    
    def close_curtains(self):
        self.p1.set(True)
        self.p2.set(True)
        
    def rotate(self):
        self.m1.set(.5)
        time.sleep(2)
        self.m1.set(0)
        
    def open_curtains(self):
        self.p1.set(False)
        self.p2.set(False)
        
        
        