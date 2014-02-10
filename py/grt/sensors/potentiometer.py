__author__ = 'dhruv'

try:
    from wpilib import AnalogPotentiometer as WPotentiometer
except ImportError:
    from pyfrc.wpilib import AnalogPotentiometer as WPotentiometer

from grt.core import Sensor


class Gyro(Sensor):
    """
    Sensor wrapper for an analog gyroscope.

    Has double attribute angle for total angle rotated.
    """
    angle = 0

    def __init__(self, channel):
        """
        Initializes the gyroscope on some analog channel.
        """
        super().__init__()
        self.p = WPotentiometer(channel)

    def poll(self):
        self.angle = self.p.Get()
