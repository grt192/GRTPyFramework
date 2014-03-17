"""
Two ball auto. Carries 2nd ball in front, shoots first, picks up and shoots second.
"""

__author__ = "Calvin Huang"

from grt.core import GRTMacroController, GRTMacro, Constants
from grt.macro.drive_macro import DriveMacro
from grt.macro.shoot_macro import ShootMacro
from grt.macro.wind_macro import WindMacro
from grt.macro.extend_macro import ExtendMacro
from grt.macro.pickup_macro import PickupMacro


class TwoBallAuto(GRTMacroController):
    """
    Two ball auto.
    """

    def __init__(self, dt, shooter, intake):
        c = Constants()
        self.extend_macro = ExtendMacro(intake, 1.5)
        self.drive_macro = DriveMacro(dt, c['2balldrivedist'], c['2balldmtimeout'])
        self.wait_macro = GRTMacro(0.5)
        self.shoot_macro = ShootMacro(shooter, 0.5)
        self.wind_macro = WindMacro(shooter)
        self.pickup_macro = PickupMacro(intake)
        self.macros = [self.extend_macro, self.drive_macro, self.wait_macro, self.shoot_macro, self.wind_macro,
                       self.pickup_macro, self.shoot_macro, self.wind_macro]
        super().__init__(macros=self.macros)
        c.add_listener(self._constants_listener)

    def _constants_listener(self, sensor, state_id, datum):
        if state_id == '2balldrivedist':
            self.drive_macro.distance = datum
        elif state_id == '2balldmtimeout':
            self.drive_macro.timeout = datum
        elif state_id == '2ballpickuptime':
            self.pickup_macro.timeout = datum
