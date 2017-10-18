class MechController:

    def __init__(self, spider, cookie, giraffe, driver_joystick, xbox_controller): # mechanisms belong in arguments
        # define mechanisms here
        self.spider = spider
        self.cookie = cookie
        self.giraffe = giraffe
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
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
        if state_id == 'y_button':
            if datum:
                self.giraffe.head_down()
                time.sleep(5)
                self.giraffe.head_up()
                time.sleep(5)

    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass
