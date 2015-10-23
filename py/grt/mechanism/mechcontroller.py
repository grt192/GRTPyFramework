class MechController:
    def __init__(self, elevator, fourbar, two_motor_pickup, bin_steal_mech, driver_joystick, xbox_controller):
        self.elevator = elevator
        self.fourbar = fourbar
        self.two_motor_pickup = two_motor_pickup
        self.bin_steal_mech = bin_steal_mech
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)
        self.trigger_count = 0
        self.button9_count = 0
        self.last_height = 0
        self.manual_control = False
        self.fourbar_automatic_control = False
        self.step_offset = False
        self.no_limit_switches = True
        self.num_trigger_presses = 0

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if self.manual_control:
            if state_id == 'r_y_axis':
                if datum:
                    if abs(datum) > .05:
                        self.elevator.elevate_speed_safe(datum)
                    else:
                        self.elevator.stop()
        if state_id == 'l_y_axis':
            if datum:
                if abs(datum) > .1:
                    self.fourbar.fourbar_macro.enabled = False
                    self.fourbar.elevate_speed(-datum)
                else:
                    if self.fourbar_automatic_control:
                        self.fourbar.fourbar_macro.setpoint = self.fourbar.fourbar_encoder.distance
                        self.fourbar.fourbar_macro.enabled = True
                    self.fourbar.stop()
        if state_id == "back_button": #Makes it hard to accidentally press this.
            if datum:
                self.elevator.lift_macro.enabled = False
                self.manual_control = True
        if state_id == "start_button":
            if datum:
                self.elevator.lift_macro.enabled = True
                self.manual_control = False

        if state_id == "x_button":
            if datum:
                #self.no_limit_switches = False
                self.bin_steal_mech.extend()
        if state_id == "y_button":
            if datum:
                #self.no_limit_switches = True
                self.bin_steal_mech.retract()
        if state_id == "r_shoulder":
            self.elevator.raise_full_step()
        if state_id == "l_shoulder":
            self.elevator.lower_full_step()

        if state_id == "a_button_2":
            if datum:
                if self.step_offset:
                    self.step_offset = False
                    self.elevator.lift_macro.STATE_DICT['level0_release'] = 0
                    self.elevator.lift_macro.STATE_DICT['level0'] = 0
                    self.elevator.lift_macro.STATE_DICT['level0.5_release'] = 0
                    self.elevator.lift_macro.STATE_DICT['level0.5'] = 7
                    self.elevator.lift_macro.STATE_DICT['level1_release'] = 13
                    self.elevator.lift_macro.STATE_DICT['level1'] = 22
                    self.elevator.lift_macro.STATE_DICT['level2_release'] = 25
                    self.elevator.lift_macro.STATE_DICT['level2'] = 35
                    self.elevator.lift_macro.STATE_DICT['level3_release'] = 36
                    self.elevator.lift_macro.STATE_DICT['level3'] = 48
                    self.elevator.lift_macro.STATE_DICT['level4_release'] = 49.5
                    self.elevator.lift_macro.STATE_DICT['level4'] = 54.5
                else:
                    self.step_offset = True
                    self.elevator.lift_macro.STATE_DICT['level0_release'] = 0
                    self.elevator.lift_macro.STATE_DICT['level0'] = 0
                    self.elevator.lift_macro.STATE_DICT['level0.5_release'] = 0
                    self.elevator.lift_macro.STATE_DICT['level0.5'] = 7
                    self.elevator.lift_macro.STATE_DICT['level1_release'] = 13
                    self.elevator.lift_macro.STATE_DICT['level1'] = 22
                    self.elevator.lift_macro.STATE_DICT['level2_release'] = 25
                    self.elevator.lift_macro.STATE_DICT['level2'] = 35
                    self.elevator.lift_macro.STATE_DICT['level3_release'] = 36
                    self.elevator.lift_macro.STATE_DICT['level3'] = 48
                    self.elevator.lift_macro.STATE_DICT['level4_release'] = 49.5
                    self.elevator.lift_macro.STATE_DICT['level4'] = 54.5

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
        if state_id == "z_axis_2":
            height = datum
            if abs(height - self.last_height) > .3:
                 #self.driver_joystick.j.getZ()
                if height >= -1 and height < -3/5:
                    self.elevator.set_state('level0')
                    print("Level 0!")
                elif height > -3/5 and height < -1/5:
                    print("Level 0.5!")
                    self.elevator.set_state('level0.5')
                elif height > -1/5 and height < 1/5:
                    self.elevator.set_state('level1')
                elif height > 1/5 and height < 3/5:
                    self.elevator.set_state('level2')
                elif height > 3/5 and height <= 1:
                    self.elevator.set_state('level3')
                else:
                    print('Unknown range set!')
                self.last_height = height

        if state_id == 'trigger':
            if datum:
                #if self.trigger_count == 1:
                #    self.trigger_count = 0
                #    self.elevator.release()
                #if self.trigger_count == 0:
                #    self.elevator.set_state('level3')
                #    self.trigger_count += 1
                if self.elevator.lift_macro.current_state == "level0" or self.elevator.lift_macro.current_state == "level0_release" or self.elevator.lift_macro.current_state == "level0.5_release":
                    #self.elevator.set_state('level1')
                    if self.no_limit_switches:
                        self.elevator.set_state('level1')
                    else:
                        self.elevator.align_macro.enabled = True
                    print("Springing")
                    self.num_trigger_presses = 0
                else:
                    if not self.num_trigger_presses == 1:
                        self.elevator.align_macro.enabled = False
                        self.elevator.align_macro.dt.set_lf_scale_factors(1, 1)
                        self.elevator.lower_half_step()
                        self.num_trigger_presses += 1
                    else:
                        self.elevator.set_state('level0')
                        self.num_trigger_presses = 0
                print(self.elevator.lift_macro.current_state)
            else:
                self.elevator.align_macro.enabled = False
                self.elevator.release_macro.enabled = False
                self.elevator.align_macro.has_touched = False
                self.elevator.align_macro.backed_up = False
                self.elevator.align_macro.dt.set_lf_scale_factors(1, 1)
            
            #if datum:
            #    self.elevator.set_state('level3')
            #else:
            #   self.elevator.set_state('level0')
        if state_id == "button57":
            if datum:
                self.elevator.pickup()
            else:
                self.elevator.align_macro.enabled = False
        if state_id == "button60":
            if datum:
                self.elevator.toggle_step()

        if state_id == "button6":
            if datum:
                if self.elevator.lift_macro.current_state == "level0" or self.elevator.lift_macro.current_state == "level0_release" or self.elevator.lift_macro.current_state == "level0.5_release":
                    self.num_trigger_presses = 0
                self.elevator.raise_full_step()
                print(self.elevator.lift_macro.current_state)

        if state_id == "button7":
            if datum:
                self.elevator.lower_full_step()
                print(self.elevator.lift_macro.current_state)


        if state_id == "button3":
            if datum:
                if self.fourbar_automatic_control:
                    self.fourbar.fourbar_macro.enabled = True
                    self.fourbar.set_state("up")
                else:
                    self.fourbar.fourbar_macro.enabled = False
                    self.fourbar.elevate()
            else:
                self.fourbar.stop()
        if state_id == "button2":
            if datum:
                if self.fourbar_automatic_control:
                    self.fourbar.fourbar_macro.enabled = True
                    self.fourbar.set_state("down")
                else:
                    self.fourbar.fourbar_macro.enabled = False
                    self.fourbar.lower()
            else:
                self.fourbar.stop()

        if state_id == "button4":
            if datum:
                print("Re-zeroing!")
                self.elevator.lift_macro.re_zero()
        if state_id == "button5":
            if datum:
                print("Aligning")
                self.elevator.pickup()
            else:
                self.elevator.align_macro.enabled = False
        

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



