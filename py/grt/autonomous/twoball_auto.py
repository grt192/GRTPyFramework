"""
Two ball auto. Carries 2nd ball in front, shoots first, picks up and shoots second.
"""

__author__ = "Calvin Huang"

from grt.core import GRTMacroController
from grt.macro.drive_macro import DriveMacro
#from grt.macro.vision_macro import VisionMacro
from grt.macro.shoot_macro import ShootMacro
from grt.macro.wind_macro import WindMacro
from grt.macro.extend_macro import ExtendMacro
from grt.macro.pickup_macro import PickupMacro


class TwoBallAuto(GRTMacroController):
    """
    Two ball auto.
    """

    drive_distance = 12.6
    pickup_time = 1.5

    def __init__(self, dt, shooter, intake, table, potentiometer, gyro):
        #self.vision_macro = VisionMacro(table, self.side, self.locked_key, self.side_key)
        self.extend_macro = ExtendMacro(intake, 3)
        self.drive_macro = DriveMacro(dt, self.drive_distance, 5)
        self.shoot_macro = ShootMacro(shooter, 1)
        self.wind_macro = WindMacro(shooter)
        self.pickup_macro = PickupMacro(intake, self.pickup_time)
        self.macros = [self.extend_macro, self.drive_macro, self.shoot_macro, self.wind_macro,
                       self.pickup_macro, self.shoot_macro, self.wind_macro]
        super().__init__(macros=self.macros)
