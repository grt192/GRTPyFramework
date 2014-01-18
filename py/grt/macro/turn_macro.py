__author__ = "Sidd Karamcheti"

from grt.core import GRTMacro
import wpilib


class TurnMacro(GRTMacro):
    P = 1
    I = 0
    D = 0
    TOLERANCE = 1

    class PIDTurnSource(wpilib.PIDSource):
        def PIDGet(self):
            return self.gyro.getAngle()

    class PIDTurnOutput(wpilib.PIDOutput):
        def PIDWrite(self, output):
            self.dt.set_dt_output(output, -output)

    def __init__(self, dt, gyro, turn_angle, timeout):
        self.dt = dt
        self.gyro = gyro
        self.turn_angle = turn_angle
        self.timeout = timeout
        self.pid_source = self.PIDTurnSource()
        self.pid_output = self.PIDTurnOutput()
        self.previously_on_target = False

        self.controller = wpilib.PIDController(self.P, self.I, self.D,
                                               self.pid_source, self.pid_output)
        self.controller.SetOutputRange(-1, 1)
        self.controller.SetAbsoluteTolerance(self.TOLERANCE)

    def perform(self):
        if self.controller.onTarget():
            if self.previously_on_target:
                self.kill()
            else:
                self.previously_on_target = True
        else:
            self.previously_on_target = False

    def die(self):
        self.dt.set_dt_output(0, 0)
        self.controller.disable()

    def initialize(self):
        start_angle = self.gyro.getAngle()
        target_angle = start_angle + self.turn_angle
        self.controller.SetSetpoint(target_angle)
        self.controller.Enable()
        print('MacroTurn is initialized')
