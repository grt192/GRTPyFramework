"""
Wind_macro.py

Winds the shooter
"""

__author__ = "Sidd Karamcheti"

from grt.core import GRTMacro
import time


class ExtendMacro(GRTMacro):
    """
    Extends the intake.
    """
    pressedtime = 0

    def __init__(self, intake, timeout=1):
        super().__init__(timeout)
        self.intake = intake

    def initialize(self):
        self.intake.angle_change(1)

    def perform(self):
        """
        Checks if shooter is still winding, kills macro if finished
        """
        print("winding")
        if self.pressedtime != 0:  # has been pressed
            if time.time() - self.pressedtime > 0.5:  # wait till .5 seconds after switch press
                self.kill()
        elif self.intake.limit_lf.pressed and self.intake.limit_rf.pressed:
            self.pressedtime = time.time()

    def die(self):
        self.shooter.angle_change(0)
