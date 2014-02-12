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

    def __init__(self, dt, drive_distance, shooter, table, locked_key, side_key, side, potentiometer, gyro, turn_angle, wind_angle, timeout=None):
        self.vision_macro = VisionMacro(table, side, locked_key, side_key)
        self.shoot_macro = ShootMacro(shooter, timeout)
        self.drive_macro = DriveMacro(dt, drive_distance, timeout)
        self.wind_macro = WindMacro(dt, potentiometer, wind_angle)
        self.turn_macro = TurnMacro(dt, gyro, turn_angle)
        self.macros = [self.vision_macro, self.shoot_macro, self.drive_macro, self.wind_macro]
        super().__init__(macros=self.macros)