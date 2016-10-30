from grt.core import GRTMacro
from grt.mechanism import *
import time

class BatsMacro(GRTMacro):

    def __init__(self, bats, timeout=None):
        super().__init__(timeout=timeout)
        self.bats = bats
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.bats.actuate()
            time.sleep(1)
            self.bats.retract()
            time.sleep(10)

    def macro_stop(self):
        self.bats.retract()
        self.enabled = False

class DoorBodyMacro(GRTMacro):

    def __init__(self, door_body, timeout=None):
        super().__init__(timeout=timeout)
        self.door_body = door_body
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.door_body.set_motor(-0.4)
            time.sleep(2.5)
            self.door_body.set_motor(0)
            time.sleep(1)
            self.door_body.actuate()
            time.sleep(1)
            self.door_body.retract()
            time.sleep(1)
            

    def macro_stop(self):
        self.door_body.set_motor(0)
        self.door_body.retract()
        sel.enabled = False

class StairMouthMacro(GRTMacro):

    def __init__(self, stair_mouth, timeout=None):
        super().__init__(timeout=timeout)
        self.stair_mouth = stair_mouth
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.stair_mouth.mouth_and_eyes(.7)
            time.sleep(.2)
            self.stair_mouth.set_motor(0)
            time.sleep(.5)
            self.stair_mouth.set_cat_motor(.3)
            self.stair_mouth.set_motor(.2)
            time.sleep(.5)
            self.stair_mouth.set_motor(0)
            time.sleep(.5)
            self.stair_mouth.set_motor(.2)
            time.sleep(.5)
            self.stair_mouth.set_motor(-.7)
            time.sleep(.2)
            self.stair_mouth.set_motor(0)
            time.sleep(1)
            self.stair_mouth.retract()
            time.sleep(3)
            self.stair_mouth.mouth_and_eyes(.7)
            time.sleep(.2)
            self.stair_mouth.set_motor(0)
            time.sleep(.5)
            self.stair_mouth.set_cat_motor(-.3)
            self.stair_mouth.set_motor(.2)
            time.sleep(.5)
            self.stair_mouth.set_motor(0)
            time.sleep(.5)
            self.stair_mouth.set_motor(.2)
            time.sleep(.5)
            self.stair_mouth.set_motor(-.7)
            time.sleep(.2)
            self.stair_mouth.set_motor(0)
            time.sleep(1)
            self.stair_mouth.retract()
            time.sleep(3)

    def macro_stop(self):
        self.stair_mouth.set_motor(0)
        self.stair_mouth.retract()
        self.enabled = False

class RockingChairMacro(GRTMacro):

    def __init__(self, rocking_chair, timeout=None):
        super().__init__(timeout=timeout)
        self.rocking_chair = rocking_chair
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.rocking_chair.set_motor(.7)
            time.sleep(1)
            self.rocking_chair.set_motor(0)
            time.sleep(.1)
            self.rocking_chair.set_motor(-.7)
            time.sleep(1)
            self.rocking_chair.set_motor(0)
            time.sleep(.1)

    def macro_stop(self):
        self.rocking_chair.set_motor(0)
        self.enabled = False


class LeaningOutMacro(GRTMacro):

    def __init__(self, leaning_out, timeout=None):
        super(). __init__(timeout=timeout)
        self.leaning_out = leaning_out
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.leaning_out.actuate()
            time.sleep(10)

    def macro_stop(self):
        self.leaning_out.retract()
        self.enabled = False

class SpikeMatMacro(GRTMacro):
    def __init__(self, spike_mat, timeout=None):
        super(). __init__(timeout=timeout)
        self.spike_mat = spike_mat
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.spike_mat.actuate()
            time.sleep(10)

    def macro_stop(self):

        self.spike_mat.retract()
        self.enabled = False

#UPDATED
class CatMacro(GRTMacro):
    def __init__(self, cat, timeout=None):
        super(). __init__(timeout=timeout)
        self.cat = cat
        self.enabled = False

    def macro_periodic(self):
         if self.enabled:
            self.cat.actuate()
            time.sleep(4)
            self.cat.set_motor(-.3)
            time.sleep(1)
            self.cat.set_motor(0)
            time.sleep(4)
            self.cat.retract()
            time.sleep(5)
            self.cat.actuate()
            time.sleep(4)
            self.cat.set_motor(.3)
            time.sleep(1)
            self.cat.set_motor(0)
            time.sleep(4)
            self.cat.retract()
            time.sleep(5)

    def macro_stop(self):

        self.cat.retract()
        self.cat.motor(0)
        self.enabled = False

#check the order
class MarionetteHandsMacro(GRTMacro):
    def __init__(self, marionette_hands, timeout=None):
        super(). __init__(timeout=timeout)
        self.marionette_hands = marionette_hands
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            print("running mhands macro")
            self.marionette_hands.set_all(.6)
            time.sleep(.5)
            self.marionette_hands.set_all(0)
            time.sleep(.1)
            self.marionette_hands.set_all(-.6)
            time.sleep(.5)
            self.marionette_hands.set_all(0)
            time.sleep(.1)


    def macro_stop(self):

        self.set_all(0)
        self.enabled = False

#check the order
class BloodyHandsMacro(GRTMacro):
    def __init__(self, bloody_hands, timeout=None):
        super(). __init__(timeout=timeout)
        self.bloody_hands = bloody_hands
        self.enabled = False

    def macro_periodic(self):
        self.bloody_hands.actuate_1()
        time.sleep(10)
        self.bloody_hands.actuate_2()
        time.sleep(10)

    def macro_stop(self):
        self.bloody_hands.retract_2()
        self.bloody_hands.retract_1()
        self.enabled = False


#check the order
class ShankedGuyMacro(GRTMacro):
    def __init__(self, shanked_guy, timeout=None):
        super(). __init__(timeout=timeout)
        self.shanked_guy = shanked_guy
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.shanked_guy.actuate()
            time.sleep(15)

    def macro_stop(self):

        self.shanked_guy.retract()
        self.enabled = False
