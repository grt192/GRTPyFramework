"""
basic_auto.py

Basic autonomous mode for the 2014 season. Waits for vision input to detect hot goal, then shoots into goal. Finally,
drives into white zone.
"""


__author__ = "Sidd Karamcheti"

import wpilib
from grt.core import GRTMacroController, GRTMacro
from grt.macro.drive_macro import DriveMacro
from grt.macro.vision_macro import VisionMacro
from grt.macro.shoot_macro import ShootMacro
from grt.macro.wind_macro import WindMacro
from grt.macro.turn_macro import TurnMacro

class BasicAuto(GRTMacroController):
    """
    Basic autonomous mode. Waits for vision input, shoots, and drives. Pretty straightforward.
    """

    drive_distance = 10
    turn_angle = 90
    wind_dist = 30
    locked_key = "locked"
    side_key = "left"
    side = "left"

    def __init__(self, dt, shooter, table, potentiometer, gyro, timeout=None):
        self.vision_macro = VisionMacro(table, self.side, self.locked_key, self.side_key)
        self.shoot_macro = ShootMacro(shooter, timeout)
        self.drive_macro = DriveMacro(dt, self.drive_distance, timeout)
        self.wind_macro = WindMacro(shooter, self.wind_dist)
        self.turn_macro = TurnMacro(dt, gyro, self.turn_angle)
        self.macros = [self.vision_macro, self.shoot_macro, self.drive_macro, self.wind_macro]
        super().__init__(macros=self.macros)
