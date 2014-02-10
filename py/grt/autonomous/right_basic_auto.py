"""
right_basic_auto.py

Basic autonomous mode for the 2014 season. Waits for vision input to detect hot goal, then shoots into goal. Finally,
drives into white zone.
"""

__author__ = "Sidd Karamcheti"

import wpilib
from grt.core import GRTMacroController, GRTMacro
from grt.macro.drive_macro import DriveMacro
from grt.macro.left_vision_macro import LeftVisionMacro
from grt.macro.shoot_macro import ShootMacro


class RightBasicAuto(GRTMacroController):
    """
    Basic autonomous mode. Waits for vision input, shoots, and drives. Pretty straightforward.
    """

    def __init__(self, dt, drive_distance, shooter, table, key):
        self.vision_macro = VisionMacro(table, key)
        self.shoot_macro = ShootMacro(shooter, timeout)
        self.drive_macro = DriveMacro(dt, drive_distance, timeout)
        self.macros = [self.right_vision_macro, self.shoot_macro, self.drive_macro]
        super().__init__(macros=self.macros)
