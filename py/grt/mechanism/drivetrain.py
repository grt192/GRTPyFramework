__author__ = "Calvin Huang, Sidd Karamcheti"
import wpilib
from grt.sensors.encoder import Encoder

class DriveTrain:
    """
    Standard 6-motor drivetrain, with standard tankdrive.
    """
    import math
    pi = math.pi
    left_front_sf = 1.0
    left_mid_sf = 1.0
    left_rear_sf = 1.0
    right_front_sf = -1.0
    right_mid_sf = -1.0
    right_rear_sf = -1.0
    power = 1.0
    dist_per_pulse = (pi * (1.75 ** 2))/128

    def __init__(self,
                 left_front_motor, right_front_motor,
                 left_mid_motor, right_mid_motor,
                 left_rear_motor, right_rear_motor,
                 left_shifter=None, right_shifter=None,
                 left_encoder=Encoder(2, 3, dist_per_pulse),
                 right_encoder=Encoder(4, 5, dist_per_pulse)):
        """
        Initializes the drivetrain with some motors;
        optional shifters and encoders
        """
        self.left_front_motor = left_front_motor
        self.left_mid_motor = left_mid_motor
        self.left_rear_motor = left_rear_motor
        self.right_front_motor = right_front_motor
        self.right_mid_motor = right_mid_motor
        self.right_rear_motor = right_rear_motor
        self.left_shifter = left_shifter
        self.right_shifter = right_shifter
        self.left_encoder = left_encoder
        self.right_encoder = right_encoder

    def set_scale_factors(self,
                          left_front_sf, right_front_sf,
                          left_mid_sf, right_mid_sf,
                          left_rear_sf, right_rear_sf):
        """
        Depending on robot orientation, drivetrain configuration, controller
        configuration, motors on different parts of the drivetrain may need to be
        driven in differing directions. These "scale factor" numbers change the
        magnitude and/or direction of the different motors; they are multipliers
        for the speed fed to the motors.
        """
        self.left_front_sf = left_front_sf
        self.left_mid_sf = left_mid_sf
        self.left_rear_sf = left_rear_sf
        self.right_front_sf = right_front_sf
        self.right_mid_sf = right_mid_sf
        self.right_rear_sf = right_rear_sf

    def set_dt_output(self, left_output, right_output):
        """
        Sets the DT output values; should be between -1 and 1.
        """
        self.left_front_motor.Set(left_output * self.left_front_sf * self.power)
        self.left_mid_motor.Set(left_output * self.left_mid_sf * self.power)
        self.left_rear_motor.Set(left_output * self.left_rear_sf * self.power)
        self.right_front_motor.Set(right_output * self.right_front_sf * self.power)
        self.right_mid_motor.Set(right_output * self.right_front_sf * self.power)
        self.right_rear_motor.Set(right_output * self.right_rear_sf * self.power)

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