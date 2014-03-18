__author__ = "Calvin Huang"

"""
Executes macros in a list/tuple/whatever sequentially.
"""

from grt.core import GRTMacro


class SequentialMacros(GRTMacro):
    """
    Executes macros sequentially. Less efficient compared to GRTMacroController,
    but has timeout functionality.
    """
    curr_macro = None

    def __init__(self, macros, timeout=20, daemon=False):
        super().__init__(timeout, daemon=daemon)
        self.macros = macros

    def initialize(self):
        self.curr_macro = None

    def perform(self):
        if self.curr_macro is None or not self.curr_macro.running:
            if not self.macros:  # no more child macros
                self.kill()
                return
            self.curr_macro = self.macros.pop(0)
            self.curr_macro.run()
        # if curr_macro is still running, do nothing

    def die(self):
        if self.curr_macro is not None:
            self.curr_macro.kill()
        for m in self.macros:
            m.kill()
