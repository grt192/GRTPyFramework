"""
shoot_macro.py

Macro for autonomous shooting. Built on the assumption that winch is pre-wound, and that the only step to shoot is to
unlatch the shooter

Will only activate after the Vision Macro either returns True, or undergoes a time out
"""

__author__ = "Sidd Karamcheti"

from grt.core import GRTMacro
import time


class ShootMacro(GRTMacro):
    """
    Shoot Macro; Shoots the ball by unlatching it
    """
    def __init__(self, shooter, timeout=5):
        super().__init__(timeout)
        self.shooter = shooter

    def perform(self):
        print("shooter perform")
        self.shooter.unlatch()
        time.sleep(0.5)
        self.shooter.latch()
        self.kill()
