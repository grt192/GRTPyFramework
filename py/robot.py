__author__ = "Sidd Karamcheti, Calvin Huang"

import wpilib
from config import sp, hid_sp, dt, ds
import time

auto = basicauto


class MyRobot(wpilib.SimpleRobot):
    def Disabled(self):
        auto.stop_autonomous()
        while self.IsDisabled():
            tinit = time.time()
            sp.poll()
            wpilib.Wait(0.04 - (time.time() - tinit))

    def Autonomous(self):
        global auto
        dt.upshift()
        self.GetWatchdog().SetEnabled(False)

        if ds.GetDigitalIn(1):
            auto = twoballauto
        else:
            auto = basicauto

        auto.run_autonomous()
        while self.IsAutonomous() and self.IsEnabled():
            tinit = time.time()
            sp.poll()
            wpilib.Wait(0.04 - (time.time() - tinit))
        auto.stop_autonomous()

    def OperatorControl(self):
        dt.downshift()  # start in low gear for tele
        dog = self.GetWatchdog()
        dog.SetExpiration(0.25)
        dog.SetEnabled(True)
        auto.stop_autonomous()

        while self.IsOperatorControl() and self.IsEnabled():
            dog.Feed()
            tinit = time.time()
            sp.poll()
            hid_sp.poll()
            wpilib.Wait(0.04 - (time.time() - tinit))


def run():
    robot = MyRobot()
    robot.StartCompetition()
