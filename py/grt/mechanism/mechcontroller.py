import time

class MechController:

    def __init__(self, apple, spider, cookie, big_ghost, giraffe, hand, stair_monster, cat_mech, driver_joystick, xbox_controller): # mechanisms belong in arguments
        # define mechanisms here
        self.apple = apple
        self.spider = spider
        self.cat_mech = cat_mech
        self.cookie = cookie
        self.giraffe = giraffe
        self.big_ghost = big_ghost
        self.hand = hand
        self.stair_monster = stair_monster
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        # if state_id == 'a_button':
        #     if datum:
        #         self.apple_mech.close_curtains()
        #         time.sleep(.5)
        #         self.apple_mech.rotate()
        #         time.sleep(.5)
        #         self.apple_mech.open_curtains()
        #         time.sleep(.5)
        # if state_id == 'b_button':
        #     if datum:
        #         self.spider.lower()
        #         time.sleep(5)
        #         self.spider.raise_()
        #         time.sleep(5)
        # if state_id == 'x_button':
        #     if datum:
        #         self.cookie.hand_down()
        #         time.sleep(2)
        #         self.cookie.hand_up()
        #         time.sleep(2)

        # if state_id == 'y_button':
        #     if datum:
        #         self.giraffe.head_down()
        #         time.sleep(5)
        #         self.giraffe.head_up()
        #         time.sleep(5)

        # if state_id == 'l_shoulder':
        #     if datum:
        #         self.big_ghost.extend()
        #         time.sleep(4)
        #         self.big_ghost.retract()
        #         time.sleep(4)

        # if state_id == 'r_shoulder':
        #     if datum:
        #         self.hand.back()
        #         time.sleep(0.5)
        #         self.hand.out()
        #         time.sleep(0.5)
        #         self.hand.back()
        #         time.sleep(0.5)
        #         self.hand.out()
        #         time.sleep(5)
        if state_id == "x_button":
            if datum:
                self.stair_monster.open_stair()

        if state_id == "y_button":
            if datum:
                self.stair_monster.close_stair()

    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass
