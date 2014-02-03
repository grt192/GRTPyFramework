__author__ = 'dhruv'
__author__ = "Sidd Karamcheti"

from grt.core import GRTMacro
import wpilib


class TurnMacro(GRTMacro):
    """
    Macro that turns a set distance.
    """
    P = 1
    I = 0
    D = 0
    TOLERANCE = 1

    class PIDTurnSource(wpilib.PIDSource):
        """
        PIDSource for turning; uses gyro angle as feedback.
        """
        def __init__(self, turn_macro):
            super().__init__()
            self.turn_macro = turn_macro
        def PIDGet(self):
            return self.turn_macro.gyro.g.GetAngle()

    class PIDTurnOutput(wpilib.PIDOutput):
        def __init__(self, turn_macro):
            super().__init__()
            self.turn_macro = turn_macro
        def PIDWrite(self, output):
            self.turn_macro.dt.set_dt_output(output, -output)

    def __init__(self, dt, gyro, turn_angle, timeout=None):
        """
        Initialize with drivetrain, gyroscope, desired turn angle and timeout.
        """
        self.dt = dt
        self.gyro = gyro
        self.turn_angle = turn_angle
        self.timeout = timeout
        self.pid_source = self.PIDTurnSource(self)
        self.pid_output = self.PIDTurnOutput(self)
        self.previously_on_target = False

        self.controller = wpilib.PIDController(self.P, self.I, self.D,
                                               self.pid_source, self.pid_output)
        self.controller.SetOutputRange(-1, 1)
        self.controller.SetAbsoluteTolerance(self.TOLERANCE)

    def perform(self):
        if self.controller.OnTarget():
            if self.previously_on_target:
                self.kill()
            else:
                self.previously_on_target = True
        else:
            self.previously_on_target = False

    def die(self):
        self.dt.set_dt_output(0, 0)
        self.controller.Disable()

    def stop(self):
        self.dt.set_dt_output(0, 0)

    def initialize(self):
        start_angle = self.gyro.angle
        target_angle = start_angle + self.turn_angle
        self.controller.SetSetpoint(target_angle)
        self.controller.Enable()
        print('MacroTurn is initialized')
