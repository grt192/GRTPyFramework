"""
Wind_macro.py

Winds the shooter
"""

__author__ = "Sidd Karamcheti"

from grt.core import GRTMacro
import grt.networktables as networktables
import wpilib


class WindMacro(GRTMacro):
    """
    Winds the shooter to some angle.
    """

    def __init__(self, shooter, target, timeout=5):
        """
        Create a wind macro with a five second timeout
        """
        super().__init__(timeout)
        self.shooter = shooter
        self.target = target

    def initialize(self):
        self.shooter.set_angle(self.target)

    def perform(self):
        """
        Checks if shooter is still winding, kills macro if finished
        """
        print("winding")
        if not self.shooter.autowinding:
            self.kill()

    def die(self):
        self.shooter.winch_stop()
