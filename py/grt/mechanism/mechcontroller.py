
                 self.manual_shooter.turn(datum*.3)
        if state_id == "x_button":
            if datum:
                self.manual_shooter.spin_flywheel(1.0)
                self.pickup.zero()
        if state_id == "y_button":
            if datum:
                self.pickup.go_to_zero()
                self.manual_shooter.spin_flywheel(0)

    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass