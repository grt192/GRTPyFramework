from record_controller import PlaybackMacro

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

        self.elmo_instructions = []
        self.headpunch_instructions = []
        self.staircase_instructions = []
        self.headless_instructions = []

        self.elmo_macro = PlaybackMacro(self.elmo_instructions, [self.elmo.motor])
        self.headpunch_macro = PlaybackMacro(self.headpunch_instructions, [self.headpunch.motor, self.headpunch.pneumatic])
        self.staircase_macro = PlaybackMacro(self.staircase_instructions, [self.staircase.pneumatic])
        self.headless_macro = PlaybackMacro(self.headless_instructions, [self.headlessmonkey.pneumatic_1, self.headlessmonkey.pneumatic_2])


    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id == 'l_y_axis':
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

        if state_id == "r_y_axis":
            if datum:
                if abs(datum) > .05:
                    self.headpunch.motor_start(datum)
                else:
                    self.headpunch.motor_stop()



       

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
        if state_id == "button6":
            if datum:
                self.record_macro.start_record()
        if state_id == "button7":
            if datum:
                self.headless_instructions = self.record_macro.stop_record()
        if state_id == "button8":
            if datum:
                self.elmo_macro.start_playback(self.elmo_instructions)
                self.headpunch_macro.start_playback(self.headless_instructions)
                self.staircase_macro.start_playback()
                self.headless_macro.start_playback()
        if state_id == "button9":
            if datum:
                self.elmo_macro.stop_playback()
                self.headpunch_macro.stop_playback()
                self.staircase_macro.stop_playback()
                self.headless_macro.stop_playback()
        

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



