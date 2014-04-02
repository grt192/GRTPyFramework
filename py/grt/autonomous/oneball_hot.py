__author__ = 'dhruv'

"""
We start facing one goal, so we only see one vision target.
"""

from . import MacroSequence
from grt.core import GRTMacro, Constants
from grt.macro.drive_macro import DriveMacro
from grt.macro.shoot_macro import ShootMacro
from grt.macro.wind_macro import WindMacro
from grt.macro.extend_macro import ExtendMacro
from grt.macro.vision_macro import VisionMacro


class OneBallHotAuto(MacroSequence):
    """
    OneBallHotAuto
    """

    locked_key = 'locked'

    def __init__(self, dt, shooter, intake, table):
        c = Constants()

        self.drive_macro = DriveMacro(dt, c['1balldrivedist'], c['1balldmtimeout'])
        self.extend_macro = ExtendMacro(intake, 1.5)
        self.wait_macro = GRTMacro(1.5)
        self.vision_macro = VisionMacro(table, self.locked_key)
        self.shoot_macro = ShootMacro(shooter, intake, 0.5)
        self.wind_macro = WindMacro(shooter)
        self.macros = [self.drive_macro, self.extend_macro, self.wait_macro,
                       self.vision_macro, self.shoot_macro, self.wind_macro]
        super().__init__(macros=self.macros)
        c.add_listener(self._constants_listener)

    def _constants_listener(self, sensor, state_id, datum):
        if state_id == '1balldrivedist':
            self.drive_macro.distance = datum
        elif state_id == '1balldmtimeout':
            self.drive_macro.timeout = datum
