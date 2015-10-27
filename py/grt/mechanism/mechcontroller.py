from grt.macro import *

class MechController:
    def __init__(self, elmo, headpunch, staircase, headless_monkey, skeleton, body_bag, record_macro, driver_joystick, xbox_controller):
        self.elmo = elmo
        self.head_punch = headpunch
        self.staircase = staircase
        self.headless_monkey = headless_monkey
        self.skeleton = skeleton
        self.body_bag = body_bag
        self.record_macro = record_macro
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

        # Elmo
        self.elmo_macro = ElmoMacro(elmo)
        self.elmo_macro.run_threaded()

        # self.headpunch_macro = PlaybackMacro(self.headpunch_instructions, [self.head_punch.motor, self.head_punch.pneumatic])

        # Staircase
        self.staircase_macro = StaircaseMacro(self.staircase)
        self.staircase_macro.run_threaded()

        # Headless Monkey
        self.headless_monkey_macro = HeadlessMonkeyMacro(self.headless_monkey)
        self.headless_monkey_macro.run_threaded()

        # Skeleton
        self.skeleton_macro = SkeletonMacro(self.skeleton)
        self.skeleton_macro.run_threaded()

        # HeadPunch
        self.head_punch_macro = HeadPunchMacro(self.head_punch)
        self.head_punch_macro.run_threaded()

        # Body Bag
        self.body_bag_macro = BodyBagMacro(self.body_bag)
        self.body_bag_macro.run_threaded()

    def _xbox_controller_listener(self, sensor, state_id, datum):

        if state_id == "a_button":
            if datum:
                self.elmo_macro.enabled = True

        if state_id == "b_button":
            if datum:
                self.elmo_macro.enabled = False

        if state_id == "x_button":
            if datum:
                self.head_punch_macro.enabled = True

        if state_id == "y_button":
            if datum:
                self.head_punch_macro.enabled = False

        if state_id == "l_shoulder":
            if datum:
                self.body_bag_macro.enabled = True

        if state_id == "r_shoulder":
            if datum:
                self.body_bag_macro.enabled = False

    def _driver_joystick_listener(self, sensor, state_id, datum):
        if state_id == "button2":
            if datum:
                self.headless_monkey.enabled = True

        if state_id == "button3":
            if datum:
                self.headless_monkey.enabled = False

        if state_id == "button4":
            if datum:
                self.staircase_macro.enabled = True

        if state_id == "button5":
            if datum:
                self.staircase_macro.enabled = False

        if state_id == "button6":
            if datum:
                self.skeleton_macro.enabled = True

        if state_id == "button7":
            if datum:
                self.skeleton_macro.enabled = False

        if state_id == 'button10':
            if datum:
                self.elmo_macro.run_threaded()

    def _universal_abort_listener(self, sensor, state_id, datum):
        if state_id == 'button8':
            if datum:
                pass


