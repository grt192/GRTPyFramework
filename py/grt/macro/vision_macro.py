"""
vision_macro.py

Macro to detect vision target for autonomous hot goals. Hits network table every few milliseconds for 5 seconds, waits
for boolean value.

Macro times out after five seconds, so robot is guaranteed to shoot.
"""

__author__ = "Sidd Karamcheti"

from grt.core import GRTMacro


class VisionMacro(GRTMacro):
    """
    VisionMacro: polls Network Table searching for boolean value
    """

    def __init__(self, table, locked_key, timeout=5):
        """
        Create a vision macro with a five second timeout
        """
        super().__init__(timeout)
        self.table = table
        self.locked_key = locked_key

    def perform(self):
        """
        Checks for the boolean value every tick, kills macro if successful
        """
        if self.table[self.locked_key] and self.table[self.side_key] is self.side:
            print("GOAL IS HOT, big G little O, GOGOGO!!!!")
            self.kill()

    def whichGoal(self):
        if self.table[self.locked_key] and self.table[self.side_key] is 'left':
            return True
        return False
