class MechController:
  
    def __init__(self, driver_joystick, xbox_controller, pickup, manual_shooter): # mechanisms belong in arguments
         # define mechanisms here
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
 
        self.pickup = pickup
        self.manual_shooter = manual_shooter
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)
 
    def _xbox_controller_listener(self, sensor, state_id, datum):
        pass
 
        if state_id == "l_y_axis":
            if datum:
                self.pickup.angle_change(datum)
 
        if state_id == "a_button": 
            if datum:
                self.pickup.roll(1.0)
            else:
                self.pickup.stop()
 
        if state_id == "b_button":
            if datum:
                self.pickup.roll(-1.0)
            else:
                self.pickup.stop()
 
 
        if state_id == "r_x_axis":
            if datum:
                self.manual_shooter.turn(datum*-.3)
        if state_id == "x_button":
            if datum:
                self.manual_shooter.shooter_up()

        if state_id == "y_button":
            if datum:
                self.manual_shooter.shooter_down()

    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass
