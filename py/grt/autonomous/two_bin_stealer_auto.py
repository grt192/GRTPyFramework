"""
basic_auto.py
"""



from . import MacroSequence
from grt.core import Constants, GRTMacro
from collections import OrderedDict
from record_controller import PlaybackMacro
from grt.macro.two_steal_macro import TwoStealMacro
from grt.macro.quick_speed_macro import QuickSpeedMacro



class TwoBinSteal(MacroSequence):
    """
    Basic autonomous mode. Drives and shoots. Pretty straightforward.
    """

    def __init__(self, talon_arr, bin_steal_mech, dt):
        self.two_steal_macro = TwoStealMacro(bin_steal_mech)
        #instructions = OrderedDict([("1, <class 'wpilib.cantalon.CANTalon'>", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.16226783968719452, 0.1935483870967742, 0.35581622678396874, 0.3870967741935484, 0.3870967741935484, 0.37438905180840665, 0.37438905180840665, 0.3118279569892473, 0.2619745845552297, 0.24926686217008798, 0.3118279569892473, 0.3304007820136852, 0.3304007820136852, 0.3304007820136852, 0.3304007820136852, 0.3304007820136852, 0.3304007820136852, 0.34310850439882695, 0.34310850439882695, 0.34310850439882695, 0.2434017595307918, 0.23069403714565004, 0.024437927663734114, 0.03714565004887586, 0.03714565004887586, 0.03714565004887586, 0.03714565004887586, 0.03714565004887586]), ("7, <class 'wpilib.cantalon.CANTalon'>", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.16226783968719452, -0.1935483870967742, -0.35581622678396874, -0.3870967741935484, -0.3870967741935484, -0.3998044965786901, -0.3998044965786901, -0.3626588465298143, -0.3118279569892473, -0.30009775171065495, -0.3626588465298143, -0.3812316715542522, -0.3812316715542522, -0.3812316715542522, -0.3812316715542522, -0.3812316715542522, -0.3812316715542522, -0.3939393939393939, -0.3939393939393939, -0.3939393939393939, -0.3313782991202346, -0.34408602150537637, 0.011730205278592375, 0.03714565004887586, 0.03714565004887586, 0.03714565004887586, 0.03714565004887586, 0.03714565004887586]), ("100, <class 'grt.macro.assistance_macros.ElevatorMacro'>", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ("5, <class 'wpilib.cantalon.CANTalon'>", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])])
        #self.playback_macro = PlaybackMacro(instructions, talon_arr)
        self.quick_speed_macro = QuickSpeedMacro(dt)
        self.macros = [self.two_steal_macro, self.quick_speed_macro]
        #[self.drive_macro, self.elevator_macro, self.drive_macro2, self.elevator_macro2]
        super().__init__(macros=self.macros)  