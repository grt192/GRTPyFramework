from grt.macro.hh_macros import *

class MechController:
    def __init__(self, opener, ramp, driver_joystick, xbox_controller):
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        self.opener = opener
        self.ramp = ramp
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id == "a_button":
            if datum:
                self.opener.extend()
        if state_id == "x_button":
            if datum:
                self.opener.retract()
        if state_id == "b_button":
            if datum:
                self.opener.go_to_drawers()
        if state_id == "r_y_axis":
            if datum > 0.05:
                self.opener.open_drawers(datum)
        if state_id == "y_button"
            if datum:
                self.ramp.arm_out
        if state_id == "l_shoulder"
            if datum:
                self.ramp.flap_down
        if state_id == "r_shoulder"
            if datum:
                self.ramp.ramp_tilt

    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass

    def _universal_abort_listener(self, sensor, state_id, datum):
        if state_id == 'button8':
            if datum:
                pass