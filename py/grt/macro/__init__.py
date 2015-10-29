__author__ = 'dhruv'

from grt.core import GRTMacro
from grt.mechanism import *
import time


class RoofMacro(GRTMacro):
    def __init__(self, roof: Roof, timeout=None):
        super().__init__(timeout=timeout)
        self.roof = roof
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.roof.actuate()
            time.sleep(1)
            self.roof.retract()
            time.sleep(10)

    def macro_stop(self):
        self.roof.retract()
        self.enabled = False

class JavierMacro(GRTMacro):
    def __init__(self, javier: Javier, timeout=None):
        super().__init__(timeout=timeout)
        self.javier = javier
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.javier.actuate()
            time.sleep(1)
            self.javier.retract()
            time.sleep(7)

    def macro_stop(self):
        self.enabled = False

class BodyBagMacro(GRTMacro):
    def __init__(self, body_bag: BodyBag, timeout=None):
        super().__init__(timeout=timeout)
        self.body_bag = body_bag
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.body_bag.motor_start(0.7)
            time.sleep(1.5)
            self.body_bag.motor_stop()
            self.body_bag.actuate()
            time.sleep(4)
            self.body_bag.motor_start(-0.2)
            time.sleep(3)
            self.body_bag.motor_stop()
            self.body_bag.retract()
            time.sleep(10)

    def macro_stop(self):
        self.enabled = False

class HeadPunchMacro(GRTMacro):
    def __init__(self, headpunch: HeadPunch, timeout=None):
        super().__init__(timeout=timeout)
        self.headpunch = headpunch
        self.enabled=False

    def macro_periodic(self):
        if self.enabled:
            self.headpunch.motor_start(0.4)
            time.sleep(5)
            self.headpunch.motor_stop()
            time.sleep(0.3)
            self.headpunch.actuate()
            time.sleep(1)
            self.headpunch.retract()
            time.sleep(1)
            self.headpunch.actuate()
            time.sleep(1)
            self.headpunch.retract()
            time.sleep(1)
            self.headpunch.actuate()
            time.sleep(1)
            self.headpunch.retract()
            time.sleep(1)
            self.headpunch.motor_start(-0.45)
            time.sleep(5)
            self.headpunch.motor_stop()
            time.sleep(5)

    def macro_stop(self):
        self.enabled = False

# class SkeletonMacro(GRTMacro):
#     def __init__(self, skeleton: Skeleton, timeout=None):
#         super().__init__(timeout=timeout)
#         self.skeleton = skeleton
#         self.enabled=False
#
#     def macro_periodic(self):
#         if self.enabled:
#             self.skeleton.actuate()
#             time.sleep(0.3)
#             self.skeleton.motor_start(0.2)
#             time.sleep(2)
#             self.skeleton.motor_stop()
#             self.skeleton.retract()
#             time.sleep(10)
#             self.skeleton.actuate()
#             time.sleep(0.3)
#             self.skeleton.motor_start(-0.2)
#             time.sleep(2)
#             self.skeleton.retract()
#             time.sleep(10)
#
#     def macro_stop(self):
#         self.enabled = False

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
            time.sleep(5)

    def macro_stop(self):
        self.enabled = False
        self.elmo.stop()


class StaircaseMacro(GRTMacro):
    def __init__(self, staircase, timeout=None):
        super().__init__(timeout=timeout)
        self.staircase = staircase
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.staircase.staircase_up()
            time.sleep(5)
            self.staircase.staircase_down()
            time.sleep(8)

    def macro_stop(self):
        self.enabled = False
        self.staircase.staircase_down()


class HeadlessMonkeyMacro(GRTMacro):
    def __init__(self, headless_monkey: HeadlessMonkey, skeleton, timeout=None):
        super().__init__(timeout=timeout)
        self.headless_monkey = headless_monkey
        self.skeleton = skeleton
        self.counter = 0
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            print("Headless macro enabled")
            # Monkey
            self.headless_monkey.actuate_1()
            time.sleep(1)
            self.headless_monkey.actuate_2()
            time.sleep(3)
            self.headless_monkey.retract_1()
            time.sleep(1)
            self.headless_monkey.retract_2()
            time.sleep(10)

            # Skeleton
            self.skeleton.actuate()
            time.sleep(1)
            self.skeleton.motor_start(0.52)
            time.sleep(3.5)
            self.skeleton.motor_stop()
            self.skeleton.retract()
            time.sleep(10)
            self.skeleton.actuate()
            time.sleep(1)
            self.skeleton.motor_start(-0.5)
            time.sleep(3.5)
            self.skeleton.motor_stop()
            time.sleep(3)
            self.skeleton.retract()
            time.sleep(10)



        self.counter += 1

    def macro_stop(self):
        self.enabled = False
        self.headless_monkey.retract_all()
