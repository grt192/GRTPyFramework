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
    shoot_delay = 0.25

    def __init__(self, shooter, intake, timeout=5):
        super().__init__(timeout)
        self.shooter = shooter
        self.intake = intake

    def initialize(self):
        self.intake.angle_change(1)

    def perform(self):
        print(str(self.intake.limit_lf.pressed) + str(self.intake.limit_rf.pressed))
        if self.intake.limit_lf.pressed and self.intake.limit_rf.pressed:
            print('shooting')
            self.shooter.unlatch()
            self._wait(self.shoot_delay)
            self.kill()

    def die(self):
        self.shooter.latch()
