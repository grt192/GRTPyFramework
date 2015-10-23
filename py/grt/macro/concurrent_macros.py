__author__ = "Trevor Nielsen"

"""
Executes all of the macros in a list/tuple/whatever at the same time. It waits for all of the specified
macros to finish if they aren't daemons.
"""

from grt.core import GRTMacro


class ConcurrentMacros(GRTMacro):
    """
    Executes all macros concurrently.
    """

    def __init__(self, macros, timeout=0, daemon=False):
        super().__init__(timeout, daemon=daemon)
        self.macros = macros

    def initialize(self):
        for m in self.macros:
            m.reset()
            print('starting concurrent macro')
            m.run()

    def perform(self):
        if all((not m.running or m.daemon for m in self.macros)):
            self.kill()

    def die(self):
        print('concurrent macro finished')
        for m in self.macros:
            m.kill()
