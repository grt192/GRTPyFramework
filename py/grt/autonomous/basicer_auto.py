"""
basicer_auto.py

Basicer autonomous mode for the 2014 season. Waits for vision input to detect hot goal, then shoots into goal. Finally,
drives into white zone.
"""

__author__ = "Trevor Nielsen"

from grt.core import GRTMacroController
from grt.macro.shoot_macro import ShootMacro

class BasicerAuto(GRTMacroController):
    """
    Basicer autonomous mode. Waits for vision input, shoots, and drives. Pretty straightforward.
    """
    def __init__(self, shooter, timeout):
        self.shoot_macro = ShootMacro(shooter, timeout)
        self.macros = [self.shoot_macro]
        super().__init__(macros=self.macros)
