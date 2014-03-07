"""
basic_auto.py

Basic autonomous mode for the 2014 season. Waits for vision input to detect hot goal, then shoots into goal. Finally,
drives into white zone.
"""


__author__ = "Sidd Karamcheti"

from grt.core import GRTMacroController
from grt.macro.drive_macro import DriveMacro
#from grt.macro.vision_macro import VisionMacro
from grt.macro.shoot_macro import ShootMacro
from grt.macro.wind_macro import WindMacro
from grt.macro.extend_macro import ExtendMacro


class BasicAuto(GRTMacroController):
    """
    Basic autonomous mode. Waits for vision input, shoots, and drives. Pretty straightforward.
    """

    drive_distance = 10.6
    turn_angle = 360
    locked_key = "locked"
    side_key = "left"
    side = "left"

    def __init__(self, dt, shooter, intake, table, potentiometer, gyro):
        #self.vision_macro = VisionMacro(table, self.side, self.locked_key, self.side_key)
        self.shoot_macro = ShootMacro(shooter, 1)
        self.extend_macro = ExtendMacro(intake, 3)
        self.drive_macro = DriveMacro(dt, self.drive_distance, 5)
        self.wind_macro = WindMacro(shooter)
        #self.macros = [self.vision_macro, self.shoot_macro, self.wind_macro, self.drive_macro]
        self.macros = [self.drive_macro, self.extend_macro, self.shoot_macro, self.wind_macro]
        super().__init__(macros=self.macros)
