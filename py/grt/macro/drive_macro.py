__author__ = 'dhruv and alex m'

from grt.core import GRTMacro
import wpilib
import threading
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class DriveMacro(GRTMacro):
    """
    Drive Macro; drives forwards a certain distance while
    maintaining orientation
    """
    leftSF = 1
    rightSF = -1
 

    distance = None
    previously_on_target = False

    def __init__(self, dt, distance, timeout):
        """
        Pass drivetrain, distance to travel (ft), and timeout (secs)
        """
        super().__init__(timeout)
        self.dt = dt
        self.left_encoder = dt.left_encoder
        self.right_encoder = dt.right_encoder
        self.setpoint = distance
    

    def engage(self):
        self.left_initial_distance = self.left_encoder.e.GetDistance()
        self.right_initial_distance = self.right_encoder.e.GetDistance()
        self.right_thread = threading.thread(target=self.run_right_drive_macro)
        self.left_thread = threading.thread(target=self.run_left_drive_macro)
        self.right_thread.start()
        self.left_thread.start()

    def right_traveled_distance(self):
        return self.right_encoder.distance - self.right_initial_distance

    def left_traveled_distance(self):
        return self.left_encoder.distance - self.left_initial_distance

    def get_distance_traveled(self):
        """
        Return average of left_traveled_distance and right_traveled_distance
        """
        return (self.left_traveled_distance() + self.right_traveled_distance()) / 2

    def run_right_drive_macro(self):
        while(self.right_traveled_distance() < self.setpoint * .8):
            self.dt.set_right_motor(1)
        while(self.right_traveled_distance() < self.setpoint):
            self.dt.set_right_motor(.5)
        self.dt.set_right_motor(0)

    def run_left_drive_macro(self):
        while(self.left_traveled_distance() < self.setpoint * .8):
            self.dt.set_left_motor(1)
        while(self.left_traveled_distance() < self.setpoint):
            self.dt.set_left_motor(.5)
        self.dt.set_left_motor(0)
   
    
    class DTSource(wpilib.interfaces.PIDSource):
        """
        PIDSource implementation for DT PID controller.

        Use avg of left, right distance traveled to control distance.
        """
        def __init__(self, drive_macro):
            super().__init__()
            self.drive_macro = drive_macro

        def PIDGet(self):
            return (self.drive_macro.right_traveled_distance() + self.drive_macro.left_traveled_distance()) / 2

    class DTOutput(wpilib.interfaces.PIDOutput):
        """
        PIDOutput implementation for DT PID controller.
        """
        def __init__(self, drive_macro):
            super().__init__()
            self.drive_macro = drive_macro

        def PIDWrite(self, output):
            self.drive_macro.speed = output
            self.drive_macro.update_motor_speeds()

    class StraightSource(wpilib.interfaces.PIDSource):
        """
        PIDSource implementation for straight PID controller.

        Use distance difference (between L/R DTs), to keep
        robot straight.
        """
        def __init__(self, drive_macro):
            super().__init__()
            self.drive_macro = drive_macro

        def PIDGet(self):
            return self.drive_macro.right_traveled_distance() - self.drive_macro.left_traveled_distance()

    class StraightOutput(wpilib.interfaces.PIDOutput):
        """
        PIDOutput implementation for straight PID controller.
        """
        def __init__(self, drive_macro):
            super().__init__()
            self.drive_macro = drive_macro

        def PIDWrite(self, output):
            modifier = abs(output)
            #rookie puzzle
            self.drive_macro.leftSF = 1 - (modifier if self.drive_macro.speed * output < 0 else 0)
            self.drive_macro.rightSF = 2 - modifier - self.drive_macro.leftSF
            self.drive_macro.update_motor_speeds()
