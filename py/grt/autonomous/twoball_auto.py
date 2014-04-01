"""
Two ball auto. Carries 2nd ball in front, shoots first, picks up and shoots second.
"""

__author__ = "Calvin Huang"

from . import MacroSequence
from grt.core import GRTMacro, Constants
from grt.macro.concurrent_macros import ConcurrentMacros
from grt.macro.drive_macro import DriveMacro
from grt.macro.shoot_macro import ShootMacro
from grt.macro.wind_macro import WindMacro
from grt.macro.extend_macro import ExtendMacro
from grt.macro.pickup_macro import PickupMacro


class TwoBallAuto(MacroSequence):
    """
    Two ball auto.
    """

    def __init__(self, dt, shooter, intake):
        c = Constants()

        self.polite_macro = GRTMacro(c['2ballpoliteness'])
        self.extend_macro = ExtendMacro(intake, 1.5)
        self.drive_macro_a = DriveMacro(dt, c['2balldrivehalfdist'], c['2balldmtimeout'])
        self.drive_macro_b = DriveMacro(dt, c['2balldriveremainingdist'], c['2balldmtimeout'])
        self.wait_macro = GRTMacro(c['2ballwait'])
        self.shoot_macro = ShootMacro(shooter, intake, 2.5)
        self.wind_macro = WindMacro(shooter)
        self.pickup_macro = PickupMacro(intake)
        self.macros = [self.polite_macro, self.extend_macro, self.drive_macro_a,
                       self.wait_macro, self.shoot_macro, self.wind_macro,
                       ConcurrentMacros((self.drive_macro_b, self.pickup_macro)),
                       self.shoot_macro, self.wind_macro]
        super().__init__(macros=self.macros)
        c.add_listener(self._constants_listener)

    def _constants_listener(self, sensor, state_id, datum):
        if state_id == '2balldrivehalfdist':
            self.drive_macro_a.distance = datum
        elif state_id == '2balldriveremainingdist':
            self.drive_macro_b.distance = datum
        elif state_id == '2balldmtimeout':
            self.drive_macro_a.timeout = self.drive_macro_b.timeout = datum
        elif state_id == '2ballwait':
            self.wait_macro.timeout = datum
        elif state_id == '2ballpoliteness':
            self.polite_macro.timeout = datum
