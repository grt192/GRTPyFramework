__author__ = "Calvin Huang, Sidd Karamcheti"


class DriveTrain:
    """
    Standard 6-motor drivetrain, with standard tankdrive.
    """
<<<<<<< HEAD
    import math
    pi = math.pi
    left_front_sf = 1.0
    left_mid_sf = 1.0
    left_rear_sf = 1.0
    right_front_sf = -1.0
    right_mid_sf = -1.0
    right_rear_sf = -1.0
=======
>>>>>>> 5292550774d8122f8006db2e51d6d0fd2e72c157
    power = 1.0
    dist_per_pulse = (pi * (1.75 ** 2))/128

    def __init__(self,
                 left_motor, right_motor,
                 left_shifter=None, right_shifter=None,
                 left_encoder=encoder(5, 4, dist_per_pulse),
                 right_encoder=encoder(2, 3, dist_per_pulse)):
        """
        Initializes the drivetrain with some motors (or MotorSets),
        optional shifters and encoders
        """
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.left_shifter = left_shifter
        self.right_shifter = right_shifter
        self.left_encoder = left_encoder
        self.right_encoder = right_encoder

    def set_dt_output(self, left_output, right_output):
        """
        Sets the DT output values; should be between -1 and 1.
        """
        left_output *= self.power
        right_output *= self.power
        self.left_motor.Set(left_output)
        self.right_motor.Set(right_output)

    def set_power(self, power):
        """
        Sets the power level of the DT (should be between 0-1)
        Scales all the motor outputs by this factor.
        """
        self.power = sorted([0, power, 1])[1]  # clamp :)

    def upshift(self):
        """
        Upshifts, if shifters are present.
        """
        if self.left_shifter and self.right_shifter:
            self.left_shifter.Set(False)
            self.right_shifter.Set(False)

    def downshift(self):
        """
        Downshifts, if shifters are present.
        """
        if self.left_shifter and self.right_shifter:
            self.left_shifter.Set(True)
            self.right_shifter.Set(True)

    def drive_distance(self, feet):
        """
        Drives forward a certain number of feet (negative feet = backwards)
        """
        self.left_encoder.reset()
        self.right_encoder.reset()
        desired_pulses = feet/dist_per_pulse

        while (self.left_encoder.get() + self.right_encoder.get)/2 < desired_pulses:
            set_dt_output(1, 1)
