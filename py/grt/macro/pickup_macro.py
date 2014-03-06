"""
Wind_macro.py

Winds the shooter
"""

__author__ = "Sidd Karamcheti"

from grt.core import GRTMacro


class ExtendMacro(GRTMacro):
    """
    Extends the intake.
    """

    def __init__(self, intake, timeout=1):
        super().__init__(timeout)
        self.intake = intake

    def initialize(self):
        self.intake.start_ep()

    def die(self):
        self.intake.stop_ep()
