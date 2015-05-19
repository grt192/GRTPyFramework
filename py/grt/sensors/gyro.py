__author__ = "Calvin Huang"

from wpilib import Gyro as WGyro
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
        self.g = WGyro(channel)

    def poll(self):
        self.angle = self.g.getAngle()
