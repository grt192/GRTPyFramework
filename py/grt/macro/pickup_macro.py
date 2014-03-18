"""
Picks up balls.
"""

__author__ = "Calvin Huang"

from grt.core import GRTMacro


class PickupMacro(GRTMacro):
    """
    Picks up balls.

    Starts EP for a little bit, then brings EP up and down.
    """

    def __init__(self, intake, timeout=5):
        """
        Specify the duration to pick up balls.
        """
        super().__init__(timeout)  # only necessary if limit switches broken
        self.intake = intake

    def initialize(self):
        self.intake.start_ep()
        self.intake.angle_change(-1)
        self._wait(0.2)
        self.intake.angle_change(1)
        self._wait(0.4)
        self.intake.angle_change(0)
        self._wait(1.0)
        self.intake.stop_ep()
        self.intake.angle_change(-1)
        self._wait(0.7)
        self.intake.angle_change(1)

    def perform(self):
        if self.intake.limit_lf.pressed and self.intake.limit_rf.pressed:
            self.kill()

    def die(self):
        self.intake.stop_ep()
        self.intake.angle_change(0)
