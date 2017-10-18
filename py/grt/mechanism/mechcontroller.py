import time

class MechController:

    def __init__(self, spider, cookie, driver_joystick, xbox_controller): # mechanisms belong in arguments
        # define mechanisms here
        self.spider = spider
        self.cookie = cookie
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id == 'a_button':
            if datum:
                self.apple_mech.close_curtains()
                time.sleep(.5)
                self.apple_mech.rotate()
                time.sleep(.5)
                self.apple_mech.open_curtains()
                time.sleep(.5)
        if state_id == 'b_button':
            if datum:
                self.spider.lower()
                time.sleep(5)
                self.spider.raise_()
                time.sleep(5)
        if state_id == 'x_button':
            if datum:
                self.cookie.hand_down()
                time.sleep(2)
                self.cookie.hand_up()
                time.sleep(2)

    def _driver_joystick_listener(self, sensor, state_id, datum):
        if state_id == "switch1":
            if datum:
                print("switch1")
                self.spider.lower()
                time.sleep(5)
                self.spider.raise_()
                time.sleep(5)
