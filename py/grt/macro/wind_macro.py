"""
Wind_macro.py

Winds the shooter
"""

__author__ = "Sidd Karamcheti"

from grt.core import GRTMacro


class WindMacro(GRTMacro):
    """
    Winds the shooter to some angle.
    """

    def __init__(self, shooter, timeout=5):
        """
        Create a wind macro with a five second timeout
        """
        super().__init__(timeout)
        self.shooter = shooter

    def initialize(self):
        self.shooter.winch_wind(1)

    def perform(self):
        """
        Checks if shooter is still winding, kills macro if finished
        """
        if self.shooter.winch_limit.pressed:
            self.kill()

    def die(self):
        self.shooter.winch_stop()
