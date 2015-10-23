__author__ = 'dhruv'

from wpilib import AnalogPotentiometer as WPotentiometer
from grt.core import Sensor


class Potentiometer(Sensor):
    """
    Sensor wrapper for an analog gyroscope.

    Has double attribute angle for total angle rotated.
    """
    angle = 0

    def __init__(self, channel, scale=1, offset=0):
        """
        Initializes the gyroscope on some analog channel.
        """
        super().__init__()
        self.p = WPotentiometer(channel, scale, offset)

    def poll(self):
        self.angle = self.p.get()
