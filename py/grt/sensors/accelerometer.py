__author__ = "Calvin Huang"

from wpilib import ADXL345_I2C
from grt.core import Sensor

class Accelerometer(Sensor):
    '''
    Sensor wrapper for the ADXL345 accelerometer, connected via I2C.

    Has double attributes for acceleration among the 3 axes: x/y/z_accel.
    '''

    def __init__(self, module=1,
                 fmt=ADXL345_I2C.DataFormat_Range.k8G):
        '''
        Initializes the accelerometer on some module.
        '''
        super().__init__()
        self.a = ADXL345_I2C(module, fmt)

    def poll(self):
        self.update_state('x_accel', self.a.GetAcceleration(ADXL345_I2C.Axes.kX))
        self.update_state('y_accel', self.a.GetAcceleration(ADXL345_I2C.Axes.kY))
        self.update_state('z_accel', self.a.GetAcceleration(ADXL345_I2C.Axes.kZ))
