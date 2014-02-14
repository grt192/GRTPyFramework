__author__ = "Sidd Karamcheti, Calvin Huang"

import wpilib
from config import auto, sp, auto_sp
import time


class MyRobot(wpilib.SimpleRobot):
    def Disabled(self):
        auto.stop_autonomous()
        while self.IsDisabled():
            wpilib.Wait(0.01)


    def Autonomous(self):
        self.GetWatchdog().SetEnabled(False)
        auto.run_autonomous()
        while self.IsAutonomous() and self.IsEnabled():
            auto_sp.poll()
            wpilib.Wait(.3)
        auto.stop_autonomous

    def OperatorControl(self):
        dog = self.GetWatchdog()
        dog.SetExpiration(0.25)
        dog.SetEnabled(True)
        auto.stop_autonomous()

        while self.IsOperatorControl() and self.IsEnabled():
            dog.Feed()
            a = time.time()
            sp.poll()
            b = time.time()
            wpilib.Wait(0.04 - (b - a))


def run():
    robot = MyRobot()
    robot.StartCompetition()
