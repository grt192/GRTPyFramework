__author__ = "Sidd Karamcheti, Calvin Huang"

import wpilib
from config importw
import time

class MyRobot(wpilib.SimpleRobot):
    def Disabled(self):
        while self.IsDisabled():
            tinit = time.time()
            sp.poll()
            wpilib.Wait(0.04 - (time.time() - tinit))

    def Autonomous(self):
        global auto
        dt.upshift()
        self.GetWatchdog().SetEnabled(False)

        while self.IsAutonomous() and self.IsEnabled():
            tinit = time.time()
            sp.poll()
            wpilib.Wait(0.04 - (time.time() - tinit))

    def OperatorControl(self):
        dt.downshift()  # start in low gear for tele
        dog = self.GetWatchdog()
        dog.SetExpiration(0.25)
        dog.SetEnabled(True)

        while self.IsOperatorControl() and self.IsEnabled():
            dog.Feed()
            tinit = time.time()
            sp.poll()
            hid_sp.poll()
            wpilib.Wait(0.04 - (time.time() - tinit))


def run():
    robot = MyRobot()
    robot.StartCompetition()
