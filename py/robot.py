__author__ = "Sidd Karamcheti, Calvin Huang"

import wpilib
from config import *


def CheckRestart():
    if lstick.GetRawButton(10):
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
            wpilib.Wait(0.01)

    def OperatorControl(self):
        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)

        while self.IsOperatorControl() and self.IsEnabled():
            dog.Feed()
            CheckRestart()

            # Motor control
            print(lstick.GetY())
            if lstick.GetRawButton(2):
                solenoid.Set(True)
                print("ON")
            elif lstick.GetRawButton(3):
                solenoid.Set(False)
                print("OFF")

            wpilib.Wait(0.04)


def run():
    robot = MyRobot()
    robot.StartCompetition()
