__author__ = "Sidd Karamcheti, Calvin Huang"

try:
    import wpilib
except ImportError:
    from pyfrc import wpilib
from config import auto, sp, auto_sp
import time


class MyRobot(wpilib.SimpleRobot):
    def Disabled(self):
        while self.IsDisabled():
            wpilib.Wait(0.01)
            auto.stop_autonomous()


    def Autonomous(self):
        self.GetWatchdog().SetEnabled(False)
        auto.run_autonomous()
        while self.IsAutonomous() and self.IsEnabled():
            auto_sp.poll()
            wpilib.Wait(3)

    def OperatorControl(self):
        dog = self.GetWatchdog()
        dog.SetExpiration(0.25)
        dog.SetEnabled(True)
        auto.stop_autonomous()

        while self.IsOperatorControl() and self.IsEnabled():
            dog.Feed()
            # Motor control
            a = time.time()
            sp.poll()
            b = time.time()
            wpilib.Wait(0.04 - (b - a))


def run():
    robot = MyRobot()
    robot.StartCompetition()
    return robot

if __name__ == '__main__':
    wpilib.run()
