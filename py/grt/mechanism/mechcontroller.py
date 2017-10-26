#import time
class MechController:

    def __init__(self,stairmonster, driver_joystick, xbox_controller): # mechanisms belong in arguments
        # define mechanisms here
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)
        self.stairmonster=stairmonster

    def _xbox_controller_listener(self, sensor, state_id, datum):
        #if(datum):
        #    self.apple_mech.close_curtain()
        #    time.sleep(1)
        #    self.apple_mech.rotate()
        #    self.apple_mech.open_curtain()
        if(state_id=="a_button"):
            if(datum):
                self.stairmonster.open_stair()
                self.stairmonster.pop()
                self.stairmonster.close_stair()

    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass