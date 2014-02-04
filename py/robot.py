__author__ = "Sidd Karamcheti, Calvin Huang"

try:
    import wpilib
except ImportError:
    from pyfrc import wpilib
from config import sp, drive_macro, auto_sp, turn_macro, gyro
import time


class MyRobot(wpilib.SimpleRobot):
    def Disabled(self):
        #drive_macro.kill()
        turn_macro.die()
        while self.IsDisabled():
            wpilib.Wait(0.01)

    def Autonomous(self):
        self.GetWatchdog().SetEnabled(False)
        #drive_macro.reset()
        turn_macro.reset()
        #drive_macro.run()
        gyro.g.Reset()
        turn_macro.initialize()
        while self.IsAutonomous() and self.IsEnabled():
            auto_sp.poll()
            turn_macro.perform()
            turn_macro.stop()
            wpilib.Wait(3)
            gyro.g.Reset()
            #print(str(gyro.g.GetRate()))
        #drive_macro.kill()


    def OperatorControl(self):
        #drive_macro.kill()
        turn_macro.die()

        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)
        t = time.time()
        gyro.g.Reset()
        gyro.g.SetSensitivity(.007)

        #raw_gyro = wpilib.AnalogChannel(3)
        while self.IsOperatorControl() and self.IsEnabled():
            dog.Feed()
            # Motor control
            #print("Rate: " + str(gyro.g.GetRate()))
            #print("Angle: " + str(gyro.g.GetAngle()))
            #print("Raw: " + str(raw_gyro.GetVoltage()))
            #print("Rate: " + str(gyro.g.GetRate()))
            print("Angle: " + str(gyro.g.GetAngle()))
            a = time.time()
            sp.poll()
            b = time.time()
            #print("Loop Time: " + str(b - t))
            t = time.time()
            wpilib.Wait(0.04 - (b - a))
            #Testing Github editor


def run():
    robot = MyRobot()
    robot.StartCompetition()
    return robot

if __name__ == '__main__':
    wpilib.run()
