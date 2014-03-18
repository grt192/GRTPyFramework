"""
shoot_macro.py

Macro for autonomous shooting. Built on the assumption that winch is pre-wound, and that the only step to shoot is to
unlatch the shooter
"""

__author__ = "Sidd Karamcheti"

from grt.core import GRTMacro


class ShootMacro(GRTMacro):
    """
    Shoot Macro; Shoots the ball by unlatching it
    """
    shoot_delay = 0.5

    def __init__(self, shooter, timeout=5):
        super().__init__(timeout)
        self.shooter = shooter

    def perform(self):
        self.shooter.unlatch()
        self._wait(self.shoot_delay)
        self.shooter.latch()
        self.kill()
