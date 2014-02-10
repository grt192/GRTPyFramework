__author__ = 'dhruv'

from grt.core import GRTMacro
import wpilib

class TurnMacro(GRTMacro):
    """
    Macro that winds the winch a certain distance
    """
    P = 0
    I = 0
    D = 0
    TOLERANCE = 1

    class PIDWindSource(wpilib.PIDSource):
        """
        PIDSource for winding; uses potentiometer as feedback
        """
        def __init__(self, wind_macro):
            super().__init__()
            self.wind_macro = wind_macro
        def PIDGet(self):
            return self.wind_macro.potentiometer.p.Get()

    class PIDWindOutput(wpilib.PIDOut):
        def __init__(self, wind_macro):
            super().__init__()
            self.wind_macro = wind_macro
        def PIDWrite(self, output):
            self.wind_macro.dt.set_dt_output(output, output)
    def __init__(self, dt, potentiometer, wind_angle, timeout=None):
        self.dt = dt
        self.potentiometer = potentiometer
        self.wind_angle = wind_angle
        self.timeout = timeout
        self.pid_source = self.PIDWindSource(self)
        self.pid_output = self.PIDWindOutput(self)
        self.previously_on_target = False

        self.controller = wpilib.PIDController(self.P, self.I, self.D, self.pid_source, self.pid_output)
        self.controller.SetOutputRange(-1, 1)
        self.controller.SetAbsoluteTolerance(self.TOLERANCE)

    def perform(self):
        if self.controller.OnTarget():
            if self.previously_on_target:
                self.kill()
                #self.kill will only work if this is called from a multithreaded setup.
            else:
                self.previously_on_target = False
        else:
            self.previously_on_target = False

    def die(self):
        self.dt.set_dt_output(0, 0)
        self.controller.Disable()
    def stop(self):
        self.dt.set_dt_output(0, 0)
    def initialize(self):
        start_angle = self.potentiometer.angle
        target_angle = start_angle + self.wind_angle
        self.controller.SetSetpoint(target_angle)
        self.controller.Enable()
        print("Wind is winding.")