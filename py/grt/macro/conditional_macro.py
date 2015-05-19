__author__ = 'dhruv'

"""
Executes one macro or another depending on the return value of a function.
"""

from grt.core import GRTMacro


class ConditionalMacro(GRTMacro):
    """
    Executes one macro or another depending on a function call.
    """
    currmacro = None

    def __init__(self, function, macro1, macro2):
        """
        If function() returns true upon initialization of this macro,
        macro1 is run. Otherwise, macro2 is run.
        """
        self.currmacro = self.macro1 = macro1
        self.macro2 = macro2
        self.function = function

    def initialize(self):
        self.currmacro = self.macro1 if self.function() else self.macro2
        self.curmacro.reset()
        self.currmacro.run()

    def perform(self):
        if not self.currmacro.running:
            self.kill()

    def die(self):
        self.currmacro.kill()
