"""
Extends the intake
"""

__author__ = "Calvin Huang"

from grt.core import GRTMacro


class ExtendMacro(GRTMacro):
    """
    Extends the intake.
    """
    def __init__(self, intake, timeout=3):
        super().__init__(timeout)
        self.intake = intake

    def initialize(self):
        self.intake.angle_change(1)

    def perform(self):
        if self.intake.limit_lf.pressed and self.intake.limit_rf.pressed:
            self.kill()

    def die(self):
        self.intake.angle_change(0)
