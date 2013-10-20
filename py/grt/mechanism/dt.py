class DriveTrain:
    '''
    Standard 4-motor drivetrain, with standard tankdrive.
    '''

    left_front_sf = left_back_sf = 1.0
    right_front_sf = right_back_sf = -1.0
    power = 1.0

    def __init__(self,
                 left_front_motor, right_front_motor,
                 left_rear_motor, right_rear_motor,
                 left_shifter=None, right_shifter=None,
                 left_encoder=None, right_encoder=None):
        '''
        Initializes the drivetrain with some motors, shifters, encoders
        '''
        self.left_front_motor = left_front_motor
        self.left_back_motor = left_back_motor
        self.right_front_motor = right_front_motor
        self.right_back_motor = right_back_motor
        self.left_shifter = left_shifter
        self.right_shifter = right_shifter
        self.left_encoder = left_encoder
        self.right_encoder = right_encoder

    def set_scale_factors(self,
                          left_front_sf, right_front_sf,
                          left_rear_sf, right_rear_sf):
        '''
        Depending on robot orientation, drivetrain configuration, controller
        configuration, motors on different parts of the drivetrain may need to be
        driven in differing directions. These "scale factor" numbers change the
        magnitude and/or direction of the different motors; they are multipliers
        for the speed fed to the motors.
        '''
        self.left_front_sf = left_front_sf
        self.left_back_sf = left_back_sf
        self.right_front_sf = right_front_sf
        self.right_back_sf = right_back_sf

    def set_dt_output(self, left_output, right_output):
        '''
        Sets the DT output values; should be between -1 and 1.
        '''
        left_front_motor.Set(left_output * left_front_sf * power)
        left_back_motor.Set(left_output * left_back_sf * power)
        right_front_motor.Set(right_output * right_front_sf * power)
        right_back_motor.Set(right_output * right_back_sf * power)

    def set_power(self, power):
        '''
        Sets the power level of the DT (should be between 0-1)
        Scales all the motor outputs by this factor.
        '''
        self.power = sorted([0, power, 1])[1]  # clamp :)

    def upshift(self):
        '''
        Upshifts, if shifters are present.
        '''
        if (left_shifter and right_shifter):
            left_shifter.Set(False)
            right_shifter.Set(False)

    def downshift(self):
        '''
        Downshifts, if shifters are present.
        '''
        if (left_shifter and right_shifter):
            left_shifter.Set(True)
            right_shifter.Set(True)
