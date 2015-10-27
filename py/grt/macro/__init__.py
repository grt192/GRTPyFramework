__author__ = 'dhruv'

from grt.core import GRTMacro
from grt.mechanism import Elmo, HeadlessMonkey
import time

class ElmoMacro(GRTMacro):
    def __init__(self, elmo: Elmo, timeout=None):
        super().__init__(timeout=timeout)
        self.elmo = elmo
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.elmo.start_motor(0.2)
            time.sleep(2)
            self.elmo.stop()
            time.sleep(5)
            self.elmo.start_motor(-0.2)
            time.sleep(2)
            self.elmo.stop()

    def macro_stop(self):
        self.enabled = False
        self.elmo.stop()


class HeadlessMonkeyMacro(GRTMacro):
    def __init__(self, headless_monkey: HeadlessMonkey, timeout=None):
        super().__init__(timeout=timeout)
        self.headless_monkey = headless_monkey
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.headless_monkey.actuate_1()
            self.headless_monkey.retract_1()
            self.headless_monkey.actuate_2()
            self.headless_monkey.retract_2()

    def macro_stop(self):
        self.enabled = False
        self.headless_monkey.retract_all()
