"""
Picks up balls.
"""

__author__ = "Calvin Huang"

from grt.core import GRTMacro


class PickupMacro(GRTMacro):
    """
    Picks up balls.

    Starts EP for a little bit, then brings EP up.
    """

    def __init__(self, intake, timeout=10):
        """
        Specify the duration to pick up balls.
        """
        super().__init__(timeout)  # only necessary if limit switches broken
        self.intake = intake

    def initialize(self):
        print('Picking up')
        self.intake.start_ep()
        print('bounce up')
        self.intake.angle_change(-1)
        self._wait(0.2)
        print('bounce down')
        self.intake.angle_change(1)
        self._wait(0.4)
        self.intake.angle_change(0)
        print('wait')
        self._wait(1.0)
        self.intake.stop_ep()
        print('raise')
        self.intake.angle_change(-1)
        self._wait(1.0)
        self.kill()

    def die(self):
        self.intake.stop_ep()
        self.intake.angle_change(0)
