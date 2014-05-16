import math

class MecanumDT:
    """
    Standard 6-motor drivetrain, with standard tankdrive.
    """
    power = 1.0

    def __init__(self,
                 fl_motor, rl_motor, rr_motor, fr_motor,
                 left_shifter=None, right_shifter=None,
                 left_encoder=None, right_encoder=None, gyro=None):
        """
        Initializes the drivetrain with some motors (or MotorSets),
        optional shifters and encoders
        """
        self.fl_motor = fl_motor
        self.rl_motor = rl_motor
        self.rr_motor = rr_motor
        self.fr_motor = fr_motor
        self.left_shifter = left_shifter
        self.right_shifter = right_shifter
        self.left_encoder = left_encoder
        self.right_encoder = right_encoder
        self.gyro = gyro

    def set_dt_output(self, magnitude, direction, rotation):
        """
        Sets the DT output values; should be between -1 and 1.
        """
        direction += 45  # Rotate the angle to drive 45 degrees clockwise for use with mechanum wheels.
        magnitude = self.limited(magnitude) * math.sqrt(2)  # Multiply magnitude by sqrt(2) to allow for full power in
                                                            # Cartesian form.
        math_direction = -direction + 90  # Convert from airplane to trig coordinates.
        rad_direction = direction * 3.14159 / 180  # Convert to radians
        x_power = math.cos(rad_direction) * magnitude
        y_power = math.sin(rad_direction) * magnitude
        """
        The front left and rear right motors map to "y_power"
        The front right and rear left motors map to "x_power"
        Rotation is factored in like it always is during a normal arcade drive.
        """
        fl_power = y_power + rotation
        rr_power = y_power - rotation
        fr_power = x_power - rotation
        rl_power = x_power + rotation
        motor_power = [fl_power, rr_power, fr_power, rl_power]
        self.normalize(motor_power)
        self.fl_motor.Set(motor_power[0])
        self.rr_motor.Set(motor_power[1])
        self.fr_motor.Set(motor_power[2])
        self.rl_motor.Set(motor_power[3])

    def limited(self, num):
        if num > 1:
            return 1
        if num < -1:
            return -1
        return -1

    @staticmethod
    def normalize(self, motor_power):
        #Find the maximum magnitude in the array.
        max_magnitude = motor_power[0]
        for i in motor_power:
            temp = abs(motor_power[i])
            if max_magnitude < temp:
                max_magnitude = temp
        #If the max magnitude is greater than 1, divide all wheel speeds by the max magnitude
        # to normalize the values.
        if max_magnitude > 1:
            for i in motor_power:
                motor_power[i] = motor_power[i] / max_magnitude

    def set_power(self, power):
        """
        Sets the power level of the DT (should be between 0-1)
        Scales all the motor outputs by this factor.
        """
        self.power = sorted([0, power, 1])[1]  # clamp :)

    def up_shift(self):
        """
        Upshifts, if shifters are present.
        """
        if self.left_shifter:
            self.left_shifter.Set(False)
        if self.right_shifter:
            self.right_shifter.Set(False)

    def down_shift(self):
        """
        Downshifts, if shifters are present.
        """
        if self.left_shifter:
            self.left_shifter.Set(True)
        if self.right_shifter:
            self.right_shifter.Set(True)
