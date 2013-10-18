from wpilib import Encoder, CounterBase
from grt.core import Sensor

class Encoder(Sensor):
    '''
    Sensor wrapper for a quadrature encoder.

    Has double attributes for distance, degrees (degrees rotated),
    rate (distance/second);
    boolean attributes stopped and direction
    '''

    def __init__(self, channel_a, channel_b, pulse_dist=1.0,
                 reverse=False, modnum=1, cpr=128,
                 enctype=CounterBase.k4x):
        '''
        Initializes the encoder with two channels,
        distance per pulse (default 1), no reversing by default,
        on module number 1 by default, 128 CPR, and with 4x counting by default
        '''
        super().__init__()
        self.e = Encoder(modnum, channel_a, channel_b, reverse, enctype)
        self.cpr = cpr
        self.pulse_dist = pulse_dist

    def poll(self):
        dist = self.e.GetDistance()
        self.update_state('distance', dist)
        self.update_state('degrees', dist / self.pulse_dist *
                          self.cpr / 360.0)
        self.update_state('rate', self.e.GetRate())
        self.update_state('stopped', self.e.GetStopped())
        self.update_state('direction', self.e.GetDirection())
