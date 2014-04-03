"""
shoot_macro.py

Macro for autonomous shooting. Built on the assumption that winch is pre-wound, and that the only step to shoot is to
unlatch the shooter
"""

__author__ = "Sidd Karamcheti"

from grt.core import GRTMacro, Constants


class ShootMacro(GRTMacro):
    """
    Shoot Macro; Shoots the ball by unlatching it
    """
    shoot_delay = 0.25

    def __init__(self, shooter, intake, timeout=5):
        super().__init__(timeout)
        c = Constants()
        self.shooter = shooter
        self.intake = intake
        self.autoshoot_wait = c['autoshoot_wait']
        c.add_listener(self._constants_listener)

    def initialize(self):
        self.intake.angle_change(1)

    def perform(self):
        if self.intake.limit_lf.pressed and self.intake.limit_rf.pressed:
            print('shooting')
            self._wait(self.autoshoot_wait)
            self.shooter.unlatch()
            self._wait(self.shoot_delay)
            self.kill()

    def die(self):
        self.shooter.latch()
        self.intake.angle_change(0)

    def _constants_listener(self, sensor, state_id, datum):
        if state_id == 'autoshoot_wait':
            self.autoshoot_wait = datum
