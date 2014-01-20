__author__ = 'dhruv'

import time
from grt.core import Sensor


class Ticker(Sensor):
    """
    Do something every now and then.
    """

    def __init__(self, duration):
        super().__init__()
        self.time = time.time()
        self.duration = duration

    def poll(self):
        if time.time() - self.time > self.duration:
            self.time = time.time()
            self.tick()

    def tick(self):
        """
        That something.
        """
        pass
