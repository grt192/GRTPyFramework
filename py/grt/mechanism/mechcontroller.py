from grt.macro.hh_macros import *

class MechController:
    def __init__(self, bats, door_body, stair_mouth, rocking_chair, leaning_out, spike_mat, cat, marionette_hands, bloody_hands, shanked_guy, spider, driver_joystick, xbox_controller):
        self.bats = bats
        self.door_body = door_body
        self.stair_mouth = stair_mouth
        self.rocking_chair = rocking_chair
        self.leaning_out = leaning_out
        self.spike_mat = spike_mat
        self.cat = cat
        self.marionette_hands = marionette_hands
        self.bloody_hands = bloody_hands
        self.shanked_guy = shanked_guy
        self.spider = spider

        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

        # Elmo
        self.bats_macro = BatsMacro(self.bats)
        #self.bats_macro.run_threaded()

        # self.headpunch_macro = PlaybackMacro(self.headpunch_instructions, [self.head_punch.motor, self.head_punch.pneumatic])

        # Staircase
        self.door_body_macro = DoorBodyMacro(self.door_body)
        #self.door_body_macro.run_threaded()

        # Headless Monkey
        self.stair_mouth_macro = StairMouthMacro(self.stair_mouth)
        #self.stair_mouth_macro.run_threaded()

        # Skeleton
        self.rocking_chair_macro = RockingChairMacro(self.rocking_chair)
        #self.rocking_chair_macro.run_threaded()

        # HeadPunch
        self.leaning_out_macro = LeaningOutMacro(self.leaning_out)
        #self.leaning_out_macro.run_threaded()

        # Body Bag
        self.spike_mat_macro = SpikeMatMacro(self.spike_mat)
        #self.spike_mat_macro.run_threaded()

        # Roof
        self.cat_macro = CatMacro(self.cat)
        #self.cat_macro.run_threaded()

        # Javier
        self.marionette_hands_macro = MarionetteHandsMacro(self.marionette_hands)
        self.marionette_hands_macro.run_threaded()

        # self.body_bag_macro = BodyBagMacro(self.body_bag)
        # self.body_bag_macro.run_threaded()
        #self.marionette_hands_macro.run_threaded()

        self.bloody_hands_macro = BloodyHandsMacro(self.bloody_hands)
        #self.bloody_hands_macro.run_threaded()

        self.shanked_guy_macro = ShankedGuyMacro(self.shanked_guy)
        #self.shanked_guy_macro.run_threaded()



    def _xbox_controller_listener(self, sensor, state_id, datum):


        #TESTING CODE

        if state_id == "a_button":
            if datum:

                self.stair_mouth.set_motor(-.5)

            else:
                self.stair_mouth.set_motor(0)
                
                
        if state_id == "b_button":
            if datum:
                
                self.door_body.set_motor(-.3)

            else:
                self.door_body.set_motor(0)


        if state_id == "x_button":
            if datum:

                self.marionette_hands_macro.enabled = True
                print("mc enabled")
               


        if state_id == "y_button":
            if datum:
                
                self.marionette_hands_macro.enabled = False
                print("mc disabled")


        if state_id == "r_shoulder":
            if datum:
                self.stair_mouth.actuate()

        if state_id == "l_shoulder":
            if datum:
                self.stair_mouth.retract()


        if state_id == "r_y_axis":
            if datum:

                self.spider.set_motor(-datum)
                print("spider")

        if state_id == "l_y_axis":
            if datum:
                if abs(datum) > .05:
                    self.marionette_hands.set_all(datum)


        # if state_id == "a_button":
        #     if datum:
        #         self.bats_macro.enabled = True
                

        # if state_id == "b_button":
        #     if datum:
        #         self.bats_macro.enabled = False

        # if state_id == "x_button":
        #     if datum:
        #         self.door_body_macro.enabled = True

        # if state_id == "y_button":
        #     if datum:
        #         self.door_body_macro.enabled = False

        # if state_id == "l_shoulder":
        #     if datum:
        #         self.stair_mouth_macro.enabled = True

        # if state_id == "r_shoulder":
        #     if datum:
        #         self.stair_mouth_macro.enabled = False

        if state_id == "l_trigger":
            if datum:
                self.rocking_chair_macro.enabled = True

        if state_id == "r_trigger":
            if datum:
                self.rocking_chair_macro.enabled = False

        if state_id == "back_button":
            if datum:
                self.bloody_hands_macro.enabled = True

        if state_id == "start_button":
            if datum:
                self.bloody_hands_macro.enabled = False

        if state_id == "trigger_pos":
            if datum:
                self.shanked_guy_macro.enabled = True
        if state_id == "keypad_pos":
            if datum:
                self.shanked_guy_macro.enabled = False

    def _driver_joystick_listener(self, sensor, state_id, datum):
        if state_id == "button6":
            if datum:
                print("homer")
                self.door_body.actuate()
                #self.leaning_out_macro.enabled = True

        if state_id == "button7":
            if datum:
                print("homer")
                self.door_body.retract()
                #self.leaning_out_macro.enabled = False

        if state_id == "button4":
            if datum:
                self.bats.actuate()
                #self.spike_mat_macro.enabled = True

        if state_id == "button5":
            if datum:
                self.bats.retract()
                #self.spike_mat_macro.enabled = False

        # if state_id == "button6":
        #     if datum:
        #         self.cat_macro.enabled = True
        
        # if state_id == "button7":
        #     if datum:
        #         self.cat_macro.enabled = False

        # if state_id == "button100":
        #     if datum:
        #         self.elmo_macro.run_threaded()

        if state_id == "trigger":
            if datum:
                self.marionette_hands_macro.enabled = True

        if state_id == "button11":
            if datum:
                self.marionette_hands_macro.enabled = False



    def _universal_abort_listener(self, sensor, state_id, datum):
        if state_id == 'button8':
            if datum:
                pass