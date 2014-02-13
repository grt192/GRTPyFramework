__author__ = "Sidd Karamcheti, Calvin Huang"

try:
    import wpilib
except ImportError:
    from pyfrc import wpilib
from config import auto, sp, hid_sp
import time


class MyRobot(wpilib.SimpleRobot):
    def Disabled(self):
        auto.stop_autonomous()
        while self.IsDisabled():
            tinit = time.time()
            sp.poll()
            wpilib.Wait(0.04 - (time.time() - tinit))

    def Autonomous(self):
        self.GetWatchdog().SetEnabled(False)
        auto.run_autonomous()
        while self.IsAutonomous() and self.IsEnabled():
            tinit = time.time()
            sp.poll()
            wpilib.Wait(0.04 - (time.time() - tinit))
        auto.stop_autonomous

    def OperatorControl(self):
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
    return robot

if __name__ == '__main__':
    wpilib.run()
