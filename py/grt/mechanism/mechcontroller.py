import time

class MechController:

    def __init__(self, talon1, talon2, talon3, talon4, talon5, talon6, talon7, talon8, driver_joystick, xbox_controller): # mechanisms belong in arguments
        # define mechanisms here
        self.talon1 = talon1
        self.talon2 = talon2
        self.talon3 = talon3
        self.talon4 = talon4
        self.talon5 = talon5
        self.talon6 = talon6
        self.talon7 = talon7
        self.talon8 = talon8
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id == 'a_button':
            if datum:
                print("a_button")
                self.talon5.set(.5)
                time.sleep(2)
                self.talon5.set(0)
        if state_id == 'b_button':
            if datum:
                print("b_button")
                self.talon6.set(.5)
                time.sleep(2)
                self.talon6.set(0)
        if state_id == 'y_button':
            if datum:
                print("y_button")
                self.talon7.set(.5)
                time.sleep(2)
                self.talon7.set(0)
        if state_id == 'x_button':
            if datum:
                print("x_button")
                self.talon8.set(.5)
                time.sleep(2)
                self.talon8.set(0)


    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass

