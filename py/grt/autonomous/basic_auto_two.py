"""
basic_auto.py
"""


__author__ = "Abraham Ryzhik"


from . import AutonomousMode
from grt.core import Constants, GRTMacro
from grt.macro.drive_macro import DriveMacro
from grt.macro.elevator_macro import ElevatorMacro



class BasicAuto(AutonomousMode):
    """
    Basic autonomous mode. Drives and shoots. Pretty straightforward.
    """

    def __init__(self, dt, elevator):

        self.elevator_macro = ElevatorMacro(elevator, 50, 1)
        self.drive_macro = DriveMacro(dt, 700, 30) 
        self.wait_macro = GRTMacro(0.5)  # blank macro just waits
        self.elevator_macro2 = ElevatorMacro(elevator, -50, 1)
        super().__init__() 