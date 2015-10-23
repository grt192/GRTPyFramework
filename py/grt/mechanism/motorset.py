class Motorset:
    """
    Drop-in replacement for wpilib.SpeedController. Useful for grouping
    bunches of motors together.
    """
    val = 0

    def __init__(self, motors, scalefactors=None):
        """
        Takes a tuple of motors and possibly a tuple of
        scalefactors, with which the motor outputs are multiplied.
        """
        self.motors = motors
        self.num_motors = len(motors)
        self.setscalefactors(scalefactors)
        self.Set = self.set
        self.Get = self.get

    def set(self, value):
        """
        Set motor value.
        This function is called identically to that for a normal single Talon.
        """
        self.val = value
        for motor, scalefactor in zip(self.motors, self.scalefactors):
            motor.set(scalefactor * value)

    def get(self):
        """
        Get motor output.
        """
        return self.val

    def setscalefactors(self, scalefactors):
        """
        Depending on robot orientation, drivetrain configuration, controller
        configuration, motors in the same gearbox may need to be
        driven in differing directions. These "scale factor" numbers change the
        magnitude and/or direction of the different motors; they are multipliers
        for the speed fed to the motors.
        """
        if scalefactors:
            if self.num_motors != len(scalefactors):
                raise ValueError("Scalefactors must have the same number of elements as motors")
        else:
            scalefactors = (1, ) * self.num_motors
        self.scalefactors = scalefactors

    def disable(self):
        for motor in self.motors:
            motor.disable()
