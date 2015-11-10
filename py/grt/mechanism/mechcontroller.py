from grt.macro import *

class MechController:
    def __init__(driver_joystick, xbox_controller):
       
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

       

    def _xbox_controller_listener(self, sensor, state_id, datum):

        

    def _driver_joystick_listener(self, sensor, state_id, datum):
        

        

    def _universal_abort_listener(self, sensor, state_id, datum):
        if state_id == 'button8':
            if datum:
                pass


