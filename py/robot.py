__author__ = "Sidd Karamcheti, Calvin Huang"

import wpilib
from config import sp, lstick, auto_sp

def CheckRestart():
    if lstick.button10:
        raise RuntimeError("Restart")

class MyRobot(wpilib.SimpleRobot):
    def Disabled(self):
        while self.IsDisabled():
            CheckRestart()
            wpilib.Wait(0.01)

    def Autonomous(self):
        self.GetWatchdog().SetEnabled(False)
        while self.IsAutonomous() and self.IsEnabled():
            CheckRestart()
            auto_sp.poll()
            wpilib.Wait(0.01)

    def OperatorControl(self):
        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)

        while self.IsOperatorControl() and self.IsEnabled():
            dog.Feed()
            CheckRestart()

            # Motor control
	     
            sp.poll()
	     

            wpilib.Wait(0.04)
            #Testing Github editor


def run():
    robot = MyRobot()
    robot.StartCompetition()
