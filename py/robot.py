__author__ = "Sidd Karamcheti, Calvin Huang, Alex Mallery"


import wpilib
import inspect
from config import hid_sp
import time

auto_exists = False


class MyRobot(wpilib.SampleRobot):
    def __init__(self):
        super().__init__()
        import config
        
        self.hid_sp = hid_sp
        self.ds = config.ds
        


    def disabled(self):
        global auto_exists
        if auto_exists:
            pass
        while self.isDisabled():
            tinit = time.time()
            #self.sp.poll()
            self.safeSleep(tinit, .04)
    if auto_exists:
        def autonomous(self):
        
            print("Autonomous started")
            while self.isAutonomous() and self.isEnabled():
                tinit = time.time()
                #self.sp.poll()
                self.safeSleep(tinit, .04)
            
    else:
        def autonomous(self):
            pass
    
    def operatorControl(self):
        if auto_exists:
            pass
        while self.isOperatorControl() and self.isEnabled():
            tinit = time.time()
            #self.sp.poll()
            self.hid_sp.poll()
            self.safeSleep(tinit, .04)
            
    def safeSleep(self, tinit, duration):
        tdif = .04 - (time.time() - tinit)
        if tdif > 0:
            time.sleep(tdif)
        if tdif <= 0:
            #print("Code running slowly!")
            pass


if __name__ == "__main__":
    wpilib.run(MyRobot)
