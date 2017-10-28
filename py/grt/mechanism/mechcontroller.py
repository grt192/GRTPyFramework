class MechController:

    def __init__(self, apple_mech, spider, cat_mech, driver_joystick, xbox_controller): # mechanisms belong in arguments
        # define mechanisms here
        self.apple_mech = apple_mech
        self.spider = spider
        self.cat_mech = cat_mech
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id = 'a_button'
            if datum:
                self.apple_mech.close_curtains()
                time.sleep(.5)
                self.apple_mech.rotate()
                time.sleep(.5)
                self.apple_mech.open_curtains()
                time.sleep(.5)
        if state_id = 'b_button'
            if datum:
                self.spider.lower()
                time.sleep(5)
                self.spider.raise_()
                time.sleep(5)
        if datum:
            self.cat_mech.turn()
        else:
            self.cat_mech.stop_turning()

    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass
