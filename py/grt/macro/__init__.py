__author__ = 'dhruv'

from grt.core import GRTMacro
from grt.mechanism import Elmo, HeadlessMonkey, Staircase, Skeleton, HeadPunch
import time


class HeadPunchMacro(GRTMacro):
    def __init__(self, headpunch: HeadPunch, timeout=None)
        super().__init__(timeout=timeout)
        self.headpunch = headpunch
        self.enabled=False

    def macro_periodic(self):
        if self.enabled:
            self.headpunch.motor_start(0.2)
            time.sleep(3)
            self.headpunch.motor_stop()
            time.sleep(0.3)
            self.headpunch.actuate()
            time.sleep(0.3)
            self.headpunch.retract()
            time.sleep(0.3)
            self.headpunch.actuate()
            time.sleep(0.3)
            self.headpunch.retract()
            time.sleep(1)
            self.headpunch.actuate()
            time.sleep(0.3)
            self.headpunch.retract()
            time.sleep(0.3)
            self.headpunch.motor_start(-0.2)
            time.sleep(3)
            self.headpunch.motor_stop()

    def macro_stop(self):
        self.enabled = False

class SkeletonMacro(GRTMacro):
    def __init__(self, skeleton: Skeleton, timeout=None)
        super().__init__(timeout=timeout)
        self.skeleton = skeleton
        self.enabled=False

    def macro_periodic(self):
        if self.enabled:
            self.skeleton.actuate()
            time.sleep(0.3)
            self.skeleton.motor_start(0.2)
            time.sleep(2)
            self.skeleton.motor_stop()
            self.skeleton.retract()
            time.sleep(10)
            self.skeleton.actuate()
            time.sleep(0.3)
            self.skeleton.motor_start(-0.2)
            time.sleep(2)
            self.skeleton.retract()
            time.sleep(10)

    def macro_stop(self):
        self.enabled = False

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


class StaircaseMacro(GRTMacro):
    def __init__(self, staircase: Staircase, timeout=None):
        super().__init__(timeout=timeout)
        self.staircase = staircase
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.staircase.staircase_up()
            time.sleep(0.5)
            self.staircase.staircase_down()
            time.sleep(0.5)

    def macro_stop(self):
        self.enabled = False
        self.staircase.staircase_down()


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
