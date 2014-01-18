__author__ = 'dhruv and alex m'

from grt.core import GRTMacro
import wpilib


class DriveMacro(GRTMacro):
    """
    Drive Macro
    """
    isAlive = True
    leftSF = 1
    rightSF = 1
    DTP = 1
    DTI = 0
    DTD = 0
    CP = 1
    CI = 0
    CD = 0
    TOLERANCE = 0.03
    MAX_MOTOR_OUTPUT = 1

    distance = None
    previously_on_target = False

    def __init__(self, dt, distance, timeout):
        """
        Pass drivetrain, distance to travel, and timeout (secs)
        """
        GRTMacro.__init__(self, timeout)
        self.dt = dt
        self.distance = distance
        self.left_encoder = dt.left_encoder
        self.right_encoder = dt.right_encoder
        self.dt_output = self.DTOutput()
        self.dt_source = self.DTSource()
        self.straight_source = self.StraightSource()
        self.straight_output = self.StraightOutput()
        self.DTController = wpilib.PIDController(self.DTP, self.DTI, self.DTD, self.dt_source, self.dt_output)
        self.straight_controller = wpilib.PIDController(self.CP, self.CI, self.CD,
                                                        self.straight_source, self.straight_output)
        self.straight_controller.SetOutputRange(0, 1)

        self.DTController.SetPID(self.DTP, self.DTI, self.DTD)
        self.straight_controller.SetPID(self.CP, self.CI, self.CD)
        self.DTController.SetAbsoluteTolerance(self.TOLERANCE)
        self.DTController.SetOutputRange(-self.MAX_MOTOR_OUTPUT, self.MAX_MOTOR_OUTPUT)

    def initialize(self):
        self.leftInitialDistance = self.left_encoder.distance
        self.rightInitialDistance = self.right_encoder.distance

        self.DTController.SetSetpoint(self.distance)
        self.straight_controller.SetSetpoint(0)
        self.DTController.Enable()
        self.straight_controller.Enable()

        self.leftSF = self.rightSF = 1
        print("MACRODRIVE is initialized")

    class DTSource(wpilib.PIDSource):
        def __init__(self):
            super().__init__()

        def PIDGet(self):
            self.distance = -(self.right_traveled_distance() + self.left_traveled_distance()) / 2
            print("Distance Traveled: " + self.distance)
            return self.distance

    class DTOutput(wpilib.PIDOutput):
        def __init__(self):
            super().__init__()

        def PIDWrite(self, output):
            self.setSpeed(output)
            self.update_motor_speeds()

    def update_motor_speeds(self):
        self.dt.setMotorSpeeds(self.speed * self.leftSF, self.speed * self.rightSF)

    def right_traveled_distance(self):
        return self.right_encoder.distance - self.rightInitialDistance

    def left_traveled_distance(self):
        return self.left_encoder.distance - self.leftInitialDistance

    """
    * Use distance difference, rather than speed difference, to keep
    * robot straight
    """
    class StraightSource(wpilib.PIDSource):
        def __init__(self):
            super().__init__()

        def PIDGet(self):
            return self.right_traveled_distance() - self.left_traveled_distance()

    class StraightOutput(wpilib.PIDOutput):
        def __init__(self):
            super().__init__()

        def PIDWrite(self, output):
            modifier = abs(output)
#rookie puzzle
            self.leftSF = 1 - (modifier if self.speed * output < 0 else 0)
            self.rightSF = 2 - modifier - self.leftSF
            self.update_motor_speeds()

    def perform(self):
        print("DTerror: " + str(self.DTController.GetError()))

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

    def get_distance_traveled(self):
        return (self.left_traveled_distance() + self.right_traveled_distance()) / 2
