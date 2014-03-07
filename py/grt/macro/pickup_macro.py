"""
Picks up balls.
"""

__author__ = "Calvin Huang"

from grt.core import GRTMacro


class PickupMacro(GRTMacro):
    """
    Picks up balls.
    """

    def __init__(self, intake, duration=1):
        """
        Specify the duration to pick up balls.
        """
        super().__init__(duration)
        self.intake = intake

    def initialize(self):
        self.intake.start_ep()

    def die(self):
        self.intake.stop_ep()
