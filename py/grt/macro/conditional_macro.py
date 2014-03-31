__author__ = 'dhruv'

"""
Executes one macro or another depending on the return value of a function.
"""

from grt.core import GRTMacro

class ConditionalMacro(GRTMacro):
    def __init__(self, function, macro1, macro2):
        self.macro1 = macro1
        self.macro2 = macro2
        self.macros = [self.macro1, self.macro2]
        self.function = function

    def initialize(self):
        self.macro1.reset()
        self.macro2.reset()
        if self.function():
            self.macro1.run()
        else:
            self.macro2.run()

    def perform(self):
        if all((not m.running or m.daemon for m in self.macros)):
            self.kill()

    def die(self):
        print('Concurrent Macro Finished')
        for m in self.macros:
            m.kill()