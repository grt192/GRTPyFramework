"""
Extends the intake
"""

__author__ = "Calvin Huang"

from grt.core import GRTMacro
import time


class ExtendMacro(GRTMacro):
    """
    Extends the intake.
    """
    pressedtime = 0
    extension_delay = 0.5

    def __init__(self, intake, timeout=3):
        super().__init__(timeout)
        self.intake = intake

    def initialize(self):
        self.intake.angle_change(1)

    def perform(self):
        if self.pressedtime != 0:  # has been pressed
            if time.time() - self.pressedtime > self.extension_delay:  # wait till .5 seconds after switch press
                self.kill()
        elif self.intake.limit_lf.pressed and self.intake.limit_rf.pressed:
            self.pressedtime = time.time()

    def die(self):
        self.pressedtime = 0
        self.intake.angle_change(0)
