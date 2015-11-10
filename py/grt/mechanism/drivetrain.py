__author__ = "Calvin Huang, Sidd Karamcheti"
from wpilib import Talon

class DriveTrain:
    """
    Standard 6-motor drivetrain, with standard tankdrive.
    """
    power = 1.0


    def __init__(self,
                 left_motor, right_motor,
                 left_shifter=None, right_shifter=None,
                 left_encoder=None, right_encoder=None):
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
        self.disabled = False
        self.left_output = 0
        self.right_output = 0
        self.left_scale = 1
        self.right_scale = 1
        self.left_add = 0
        self.right_add = 0

    def set_dt_output(self, left_output, right_output):
        """
        Sets the DT output values; should be between -1 and 1.
        """
        #self.left_output = left_output
        #self.right_output = right_output
        left_output *= self.left_scale
        right_output *= self.right_scale
        left_output += self.left_add
        right_output += self.right_add
        #if not left_output == 0:
        #    left_output = (left_output ** 3) / abs(left_output)
        #if not right_output == 0:
        #    right_output = (right_output ** 3) / abs(right_output)
        self.left_motor.set(-left_output)
        self.right_motor.set(+right_output)
        #print("left output %f" % left_output)
        #print("right travel: %f" % self.right_encoder.distance)
        #print("left travel: %f" % self.left_encoder.distance)
    def drive_controller_set_dt_output(self, left_output, right_output):
        if not self.disabled:
            self.set_dt_output(left_output, right_output)
    def enable(self):
        self.disabled = False
    def disable(self):
        self.disabled = True

    def add_to_dt_output(self, left_output, right_output):
        self.left_add = left_output
        self.right_add = right_output

    #def scale_dt_output(self, left_scale, right_scale):
    #    self.set_dt_output(self.left_output * left_scale, self.right_output * right_scale)

    def set_lf_scale_factors(self, left_scale, right_scale):
        self.left_scale = left_scale
        self.right_scale = right_scale

    def set_right_motor(self, power):
        self.right_motor.set(power)
    def set_left_motor(self, power):
        self.left_motor.set(-power)


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
        if self.left_shifter:
            self.left_shifter.set(False)
        if self.right_shifter:
            self.right_shifter.set(False)

    def downshift(self):
        """
        Downshifts, if shifters are present.
        """
        if self.left_shifter:
            self.left_shifter.set(True)
        if self.right_shifter:
            self.right_shifter.set(True)