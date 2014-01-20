__author__ = 'dhruv and alex m'

from grt.core import GRTMacro
import wpilib


class DriveMacro(GRTMacro):
    """
    Drive Macro; drives forwards a certain distance while
    maintaining orientation
    """
    leftSF = 1
    rightSF = -1
    DTP = 1.5
    DTI = 0
    DTD = 0
    CP = 0  # CP = 1
    CI = 0
    CD = 0
    TOLERANCE = 0.03
    MAX_MOTOR_OUTPUT = 1

    distance = None
    previously_on_target = False

    def __init__(self, dt, distance, timeout):
        """
        Pass drivetrain, distance to travel (ft), and timeout (secs)
        """
        GRTMacro.__init__(self, timeout)
        self.dt = dt
        self.distance = distance
        self.left_encoder = dt.left_encoder
        self.right_encoder = dt.right_encoder
        self.dt_output = self.DTOutput(self)
        self.dt_source = self.DTSource(self)
        self.straight_source = self.StraightSource(self)
        self.straight_output = self.StraightOutput(self)
        self.DTController = wpilib.PIDController(self.DTP, self.DTI, self.DTD, self.dt_source, self.dt_output)
        self.straight_controller = wpilib.PIDController(self.CP, self.CI, self.CD,
                                                        self.straight_source, self.straight_output)
        self.straight_controller.SetOutputRange(0, 1)

        self.DTController.SetPID(self.DTP, self.DTI, self.DTD)
        self.straight_controller.SetPID(self.CP, self.CI, self.CD)
        self.DTController.SetAbsoluteTolerance(self.TOLERANCE)
        self.DTController.SetOutputRange(-self.MAX_MOTOR_OUTPUT, self.MAX_MOTOR_OUTPUT)

    def initialize(self):
        self.left_initial_distance = self.left_encoder.distance
        self.right_initial_distance = self.right_encoder.distance

        self.DTController.SetSetpoint(self.distance)
        self.straight_controller.SetSetpoint(0)
        self.DTController.Enable()
        self.straight_controller.Enable()

        self.leftSF = self.rightSF = 1
        print("MACRODRIVE is initialized")

    def update_motor_speeds(self):
        self.dt.set_dt_output(self.speed * self.leftSF, self.speed * self.rightSF)

    def right_traveled_distance(self):
        return self.right_encoder.distance - self.right_initial_distance

    def left_traveled_distance(self):
        return self.left_encoder.distance - self.left_initial_distance

    def get_distance_traveled(self):
        """
        Return average of left_traveled_distance and right_traveled_distance
        """
        return (self.left_traveled_distance() + self.right_traveled_distance()) / 2

    def perform(self):
        print("DTerror: " + str(self.DTController.GetError()))
        print("Left Traveled Distance:" + str(self.left_traveled_distance()))
        print("Right Traveled Distance:" + str(self.right_traveled_distance()))

        print("Distance Traveled: " + str(self.get_distance_traveled()))
        if (self.DTController.OnTarget()):
            print("On target!")
            if (self.previously_on_target):
                self.kill()
            else:
                self.previously_on_target = True
        else:
            self.previously_on_target = False

    def die(self):
        self.dt.set_dt_output(0, 0)
        self.DTController.Disable()
        self.straight_controller.Disable()

    class DTSource(wpilib.PIDSource):
        """
        PIDSource implementation for DT PID controller.

        Use avg of left, right distance traveled to control distance.
        """
        def __init__(self, drive_macro):
            super().__init__()
            self.drive_macro = drive_macro

        def PIDGet(self):
            return (self.drive_macro.right_traveled_distance() + self.drive_macro.left_traveled_distance()) / 2

    class DTOutput(wpilib.PIDOutput):
        """
        PIDOutput implementation for DT PID controller.
        """
        def __init__(self, drive_macro):
            super().__init__()
            self.drive_macro = drive_macro

        def PIDWrite(self, output):
            self.drive_macro.speed = output
            self.drive_macro.update_motor_speeds()

    class StraightSource(wpilib.PIDSource):
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

    class StraightOutput(wpilib.PIDOutput):
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
