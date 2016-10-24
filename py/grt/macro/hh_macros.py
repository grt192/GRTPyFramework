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

class SpikeMatMacro(GRTMacro):

class CatMacro(GRTMacro):

class MarionetteHandsMacro(GRTMacro):

class BloodyHandsMacro(GRTMacro):

class ShankedGuyMacro(GRTMacro):
