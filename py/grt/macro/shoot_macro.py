"""
shoot_macro.py

Macro for autonomous shooting. Built on the assumption that winch is pre-wound, and that the only step to shoot is to
unlatch the shooter

Will only activate after the Vision Macro either returns True, or undergoes a time out
"""

__author__ = "Sidd Karamcheti"

from grt.core import GRTMacro
from grt.mechanism import Shooter
import time
import wpilib


class ShootMacro(GRTMacro):
    """
    Shoot Macro; Shoots the ball by unlatching it
    """
    def __init__(self, shooter, timeout=5):
        super().__init___(timeout)
        self.shooter = shooter

    def perform(self):
        self.shooter.unlatch()
        time.sleep(1)
        self.shooter.latch()
        self.kill()
