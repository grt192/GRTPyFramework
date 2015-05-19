
from wpilib.interfaces import CounterBase
from wpilib import Encoder as WEncoder
from grt.core import Sensor


class Encoder(Sensor):
    """
    Sensor wrapper for a quadrature encoder.

    Has double attributes distance, rate (distance/second);
    boolean attributes stopped and direction.
    """

    distance = rate = 0
    stopped = direction = True

    def __init__(self, channel_a, channel_b, pulse_dist=1.0,
                 reverse=False, modnum=1, cpr=128,
                 enctype=CounterBase.EncodingType.k4X):
        """
        Initializes the encoder with two channels,
        distance per pulse (usu. feet, default 1), no reversing,
        on module number 1, 128 CPR, and with 4x counting.
        """
        super().__init__()
        self.e = WEncoder(channel_a, channel_b, reverse, enctype)
        self.cpr = cpr
        self.e.setDistancePerPulse(pulse_dist)
    def poll(self):
        self.distance = self.e.getDistance()
        self.rate = self.e.getRate()
        self.stopped = self.e.getStopped()
        self.direction = self.e.getDirection()
