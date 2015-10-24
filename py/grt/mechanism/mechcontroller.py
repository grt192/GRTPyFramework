class MechController:
    def __init__(self, elmo, headpunch, staircase, headlessmonkey, record_macro, driver_joystick, xbox_controller):
        self.elmo = elmo
        self.headpunch = headpunch
        self.staircase = staircase
        self.headlessmonkey = headlessmonkey
        self.record_macro = record_macro
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id == 'r_y_axis':
            if datum:
                if abs(datum) > .05:
                    self.elmo.start_motor(datum)
                else:
                    self.elmo.stop_elmo()
       
        if state_id == "x_button":
            if datum:
                #self.no_limit_switches = False
                self.headpunch.actuate()

        if state_id == "y_button":
            if datum:
                #self.no_limit_switches = True
                self.headpunch.retract()

        if state_id == "r_shoulder":
            self.staircase.staircase_up()

        if state_id == "l_shoulder":
            self.staircase.staircase_down()

        if state_id == "l_y_axis":
            if datum:
                if abs(datum) > .05:
                    self.headpunch.motor_start(datum)
                else:
                    self.headpunch.motorstop()



       

        """                    
        if state_id == "l_shoulder":
            if datum:
                self.two_motor_pickup.operate(.5)
                
            else:
                self.two_motor_pickup.stop()

        if state_id == "r_shoulder":
            if datum:
                self.two_motor_pickup.operate(.5)
            else:
                self.two_motor_pickup.stop()
        """



    def _driver_joystick_listener(self, sensor, state_id, datum):
        if state_id == "button2":
            if datum:
                self.headlessmonkey.actuate_1()

        if state_id == "button3":
            if datum:
                self.headlessmonkey.retract_1()

        if state_id == "button4":
            if datum:
                self.headlessmonkey.actuate_2()

        if state_id == "button5":
            if datum:
                self.headlessmonkey.retract_2()
        

        """
        if state_id == 'button10':
            if datum:
                self.elevator.abort()

        #Springloaded button 9
        if state_id == 'button9':
            if datum:
                pass
            else:
                self.elevator.spring()
        """

    def _universal_abort_listener(self, sensor, state_id, datum):
        if state_id == 'button8':
            if datum:
                self.elevator.kill_all_macros()



