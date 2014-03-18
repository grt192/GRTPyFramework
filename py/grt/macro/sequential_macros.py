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
    curr_macro_index = 0

    def __init__(self, macros, timeout=20, daemon=False):
        super().__init__(timeout, daemon=daemon)
        self.macros = macros

    def initialize(self):
        self.curr_macro = None
        self.macro_queue = list(self.macros)

    def perform(self):
        if self.curr_macro is None or not self.curr_macro.running:
            if not self.macro_queue:  # no more child macros
                self.kill()
                return
            self.curr_macro = self.macro_queue.pop(0)
            print('starting sequential macro')
            self.curr_macro.reset()
            self.curr_macro.run()
        # if curr_macro is still running, do nothing

    def die(self):
        if self.curr_macro is not None:
            self.curr_macro.kill()
        for m in self.macros:
            m.kill()
