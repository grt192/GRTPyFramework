__author__ = "Trevor Nielsen"

"""
Executes all of the macros in a list/tuple/whatever at the same time. It waits for all of the specified
macros to finish.

Ex. (macroOne, macroTwo, macroThree), (True, False, True) will wait for macros one and three to finish,
and cut off two.
"""

from grt.core import GRTMacro


class ConcurrentMacros(GRTMacro):
    """
    Executes all macros concurrently.
    """

    def __init__(self, macros, waits, timeout=20):
        super().__init__(timeout)
        self.macros = zip(macros, waits)

    def initialize(self):
        for m, w in self.macros:
            m.run()

    def perform(self):
        for m, w in self.macros:
            if w and m.running:
                return
        self.kill()

    def die(self):
        for m, w in self.macros:
            m.kill()
