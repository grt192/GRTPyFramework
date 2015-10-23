__author__ = "dhruv, Sidd Karamcheti"

from grt.core import GRTMacro
import wpilib

#constants = Constants()

class TurnMacro(GRTMacro):
    """
    Macro that turns a set distance.
    """
   # TP = constants['TP']
    #TI = constants['TI']
    #TD = constants['TD']
    #TOLERANCE = constants['TMtol']

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
        super().__init__(timeout)
        self.dt = dt
        self.gyro = gyro
        self.turn_angle = turn_angle
        self.timeout = timeout
        self.pid_source = self.PIDTurnSource(self)
        self.pid_output = self.PIDTurnOutput(self)
        self.previously_on_target = False

        self.controller = wpilib.PIDController(self.TP, self.TI, self.TD,
                                               self.pid_source, self.pid_output)
        self.controller.SetOutputRange(-1, 1)
        self.controller.SetAbsoluteTolerance(self.TOLERANCE)
        constants.add_listener(self._constant_listener)

    def _constant_listener(self, sensor, state_id, datum):
        if state_id in ('TP', 'TI', 'TD'):
            self.__dict__[state_id] = datum
            self.controller.setPID(self.TP, self.TI, self.TD)
        elif state_id == 'TMtol':
            self.TOLERANCE = datum
            self.controller.SetAbsoluteTolerance(datum)

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
