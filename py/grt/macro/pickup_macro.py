"""
Picks up balls.
"""

__author__ = "Calvin Huang"

from grt.core import GRTMacro
import time


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
        time.sleep(0.5)
        self.intake.stop_ep()
        self.intake.angle_change(-1)
        time.sleep(0.5)
        self.intake.angle_change(1)

    def perform(self):
        if self.intake.limit_lf.pressed and self.intake.limit_rf.pressed:
            self.kill()

    def die(self):
        self.intake.stop_ep()
        self.intake.angle_change(0)
