"""
basic_auto.py
"""


__author__ = "Sidd Karamcheti"

from grt.core import GRTMacroController, Constants
from grt.macro.drive_macro import DriveMacro
#from grt.macro.vision_macro import VisionMacro
from grt.macro.shoot_macro import ShootMacro
from grt.macro.wind_macro import WindMacro
from grt.macro.extend_macro import ExtendMacro


class BasicAuto(GRTMacroController):
    """
    Basic autonomous mode. Drives and shoots. Pretty straightforward.
    """

    def __init__(self, dt, shooter, intake, table, potentiometer, gyro):
        #self.vision_macro = VisionMacro(table, self.side, self.locked_key, self.side_key)
        c = Constants()
        self.shoot_macro = ShootMacro(shooter, 0.5)
        self.extend_macro = ExtendMacro(intake, 1.5)
        self.drive_macro = DriveMacro(dt, c['1balldrivedist'], c['1balldmtimeout'])
        self.wind_macro = WindMacro(shooter)
        #self.macros = [self.vision_macro, self.shoot_macro, self.wind_macro, self.drive_macro]
        self.macros = [self.drive_macro, self.extend_macro, self.shoot_macro, self.wind_macro]
        super().__init__(macros=self.macros)
        c.add_listener(self._constants_listener)

    def _constants_listener(self, sensor, state_id, datum):
        if state_id == '1balldrivedist':
            self.drive_macro.distance = datum
        elif state_id == '1balldmtimeout':
            self.drive_macro.timeout = datum
