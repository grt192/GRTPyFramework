from grt.core import GRTMacro
from grt.mechanism import *
import time

class BatsMacro(GRTMacro):

    def __init__(self, bats: Bats, timeout=None):
        super().__init__(timeout=timout)
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

    def __init__(self, door_body: DoorBody, timeout=None):
        super().__init__(timeout=timout)
        self.door_body = door_body
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.door_body.set_motor(0.7)
            time.sleep(5)
            self.door_body.set_motor(0)
            time.sleep(1)
            self.door_body.actuate()
            time.sleep(1)
            self.door_body.retract()
            time.sleep(1)
            self.door_body.set_motor(-0.7)
            time.sleep(5)
            self.door_body.set_motor(0)
            time.sleep(1)

    def macro_stop(self):
        self.door_body.set_motor(0)
        self.door_body.retract()
        sel.enabled = False

class StairMouthMacro(GRTMacro):

    def __init__(self, stair_mouth: StairMouth, timeout=None):
        super().__init__(timeout=timout)
        self.stair_mouth = stair_mouth
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.stair_mouth.mouth_and_eyes(.7)
            time.sleep(.2)
            self.stair_mouth.set_motor(0)
            time.sleep(.1)
            self.stair_mouth.set_motor(.2)
            time.sleep(.1)
            self.stair_mouth.set_motor(0)
            time.sleep(.1)
            self.stair_mouth.set_motor(.2)
            time.sleep(.1)
            self.stair_mouth.set_motor(-.7)
            time.sleep(.2)
            self.stair_mouth.set_motor(0)
            time.sleep(1)
            self.stair_mouth.retract()
            time.sleep(5)

    def macro_stop(self):
        self.stair_mouth.set_motor(0)
        self.stair_mouth.retract()
        self.enabled = False

class RockingChairMacro(GRTMacro):

    def __init__(self, rocking_chair: RockingChair, timeout=None):
        super().__init__(timeout=timout)
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

    def __init__(self, leaning_out: LeaningOut, timeout=None):
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
     def __init__(self, spike_mat: SpikeMat, timeout=None):
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

#check the order
class CatMacro(GRTMacro):
     def __init__(self, cat: Cat, timeout=None):
        super(). __init__(timeout=timeout)
        self.cat = cat
        self.enabled = False

    def macro_periodic(self):
         if self.enabled:
            self.cat.actuate()
            self.cat.set_motor(.7)
            time.sleep(1)
            self.cat.set_motor(-.7)
            time.sleep(1)

    def macro_stop(self):

        self.cat.retract()
        self.cat.motor(0)
        self.enabled = False

#check the order
class MarionetteHandsMacro(GRTMacro):
     def __init__(self, marionette_hands: MarionetteHands, timeout=None):
        super(). __init__(timeout=timeout)
        self.marionette_hands = marionette_hands
        self.enabled = False

    def macro_periodic(self):
        if self.enabled:
            self.set_all(.7)
            time.sleep(5)
            self.set_all(-.7)
            time.sleep(5)


    def macro_stop(self):

        self.set_all(0)
        self.enabled = False

#check the order
class BloodyHandsMacro(GRTMacro):
     def __init__(self, bloody_hands: BloodyHands, timeout=None):
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
     def __init__(self, shanked_guy: ShankedGuy, timeout=None):
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
