__author__ = "Sidd Karamcheti"

import wpilib

class TurnMacro:

    class PIDTurnSource(PIDSource):
        def __init__(self):
            super.__init__(self)

        def pidGet(self):
            return self.gyro.getAngle()

    class PIDTurnOutput(PIDOutput):
        def __init__(self):
            super.__init__(self)

        def pidWrite(self, output):
            self.dt.set_dt_output(output, -output)

    def __init__(self, dt, gyro, turnAngle, timeout):
        self.dt = dt
        self.gyro = gyro
        self.turnAngle = turnAngle
        self.timeout = timeout
        self.pidSource = PIDTurnSource(wpilib.PIDSource())
        self.pidOutput = PIDTurnOutput(wpilib.PIDOutput())
        self.previouslyOnTarget = False

        self.P = 1
        self.I = 0
        self.D = 0

        self.controller = wpilib.PIDController(0, 0, 0, self.pidSource, self.pidOutput, .01)
        self.controller.setPID(self.P, self.I, self.D)

    def perform(self):
        if self.controller.onTarget():
            if self.previouslyOnTarget:
                notifyFinished()
            else:
                self.previouslyOnTarget = True
        else:
            self.previouslyOnTarget = False

    def die(self):
        self.controller.disable()

    def initialize(self):
        startAngle = self.gyro.getAngle()
        targetAngle = startAngle + self.turnAngle
        self.controller.setOutputRange(-1, 1)
        self.controller.setAbsoluteTolerance(1)
        self.controller.setSetpoint(targetAngle)
        self.controller.enable();


