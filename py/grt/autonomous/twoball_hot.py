__author__ = 'dhruv'

"""
Assumes that we start in the middle. We turn towards the not-hot goal, and set up, then fire one ball at 4.8 seconds,
and pick up and shoot the next one into the hot goal.
Uses split_vision logic
"""

from grt.core import GRTMacroController, GRTMacro, Constants
from grt.macro.drive_macro import DriveMacro
from grt.macro.shoot_macro import ShootMacro
from grt.macro.wind_macro import WindMacro
from grt.macro.extend_macro import ExtendMacro
from grt.macro.pickup_macro import PickupMacro
from grt.macro.turn_macro import TurnMacro
from grt.macro.vision_macro import VisionMacro
from grt.macro.conditional_macro import ConditionalMacro
from grt.macro.concurrent_macros import ConcurrentMacros


class TwoBallHotAuto(GRTMacroController):
    """
    Two ball hot auto
    """

    locked_key = 'locked'

    def __init__(self, dt, shooter, intake, gyro, table):
        c = Constants()

        self.vision_macro = VisionMacro(table, self.locked_key)
        self.turn_macro_right = TurnMacro(dt, gyro, c['2ballhotturnangle'])
        self.turn_macro_left = TurnMacro(dt, gyro, -c['2ballhotturnangle'])
        self.turn_macro_right2 = TurnMacro(dt, gyro, 2 * c['2ballhotturnangle'])
        self.turn_macro_left2 = TurnMacro(dt, gyro, -2 * c['2ballhotturnangle'])
        self.drive_macro = DriveMacro(dt, c['2ballhotdrivedistance'], c['2ballhotdmtimeout'])
        self.wait_macro = GRTMacro(c['2ballhotwait'])
        self.shoot_macro = ShootMacro(shooter, intake, 2.5)
        self.wind_macro = WindMacro(shooter)
        self.extend_macro = ExtendMacro(intake, 1.5)
        self.pickup_macro = PickupMacro(intake)

        self.macros = [ConcurrentMacros(self.extend_macro, self.drive_macro),
                       ConditionalMacro(self.vision_macro.left_hot,
                                        self.turn_macro_left,
                                        self.turn_macro_right),
                       self.wait_macro, self.shoot_macro,
                       ConcurrentMacros(self.pickup_macro, self.wind_macro), self.shoot_macro]
        super().__init__(macros=self.macros)
        c.add_listener(self._constants_listener)

    def _constants_listener(self, sensor, state_id, datum):
        if state_id == '2ballhotturnangle':
            self.turn_macro_right.turn_angle = datum
            self.turn_macro_left.turn_angle = -datum
        elif state_id == '2ballhotdrivedistance':
            self.drive_macro.distance = datum
        elif state_id == '2ballhotdmtimeout':
            self.drive_macro.timeout = datum
        elif state_id == '2ballhotwait':
            self.wait_macro.timeout = datum
