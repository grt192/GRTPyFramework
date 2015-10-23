from grt.macro.assistance_macros import *
import wpilib

class Elevator:
    def __init__(self, elevator_motor, elevator_encoder, left_switch=None, right_switch=None, dt=None, winch_servo=None, top_switch=None, bottom_switch=None, bottom_limit_switch=None):
        self.elevator_motor = elevator_motor
        self.elevator_encoder = elevator_encoder
        self.winch_servo = winch_servo
        self.left_switch = left_switch
        self.right_switch = right_switch
        self.top_switch = top_switch
        self.bottom_switch = bottom_switch
        self.running_macros = []
        self.bottom_limit_switch = bottom_limit_switch
        #The elevator passes itself to the macros so that they can take over its functions.
        self.release_macro = ReleaseMacro(self, dt)
        self.align_macro = AlignMacro(self, dt)
        self.lift_macro = ElevatorMacro(self)

        #self.temp_talon = wpilib.Talon(9)

    def elevate(self):
        if self.winch_servo:
            self.release_winch()
        self.elevator_motor.set(1)

    def toggle_step(self):
        pass

    def lower(self):
        if self.winch_servo:
            self.release_winch()
        self.elevator_motor.set(-1)

    def stop(self):
        if self.winch_servo:
            self.engage_winch()

        self.elevator_motor.set(0)
        #self.temp_talon.set(0)

    def elevate_speed(self, power):
        self.elevator_motor.set(-power)
        #self.temp_talon.set(power)

    def lower_half_step(self):
        current_index = list(self.lift_macro.STATE_DICT.keys()).index(self.lift_macro.current_state)
        print(current_index)
        if not current_index == 0:
            self.lift_macro.current_state = list(self.lift_macro.STATE_DICT.keys())[current_index - 1]
            self.lift_macro.setpoint = list(self.lift_macro.STATE_DICT.values())[current_index - 1]
    def lower_full_step(self):
        if "release" in self.lift_macro.current_state:
            self.step_logic(-3)
        else:
            self.step_logic(-2)
    def raise_full_step(self):
        if "release" in self.lift_macro.current_state:
            self.step_logic(1)
        else:
            self.step_logic(2)

    def step_logic(self, steps):
        current_index = list(self.lift_macro.STATE_DICT.keys()).index(self.lift_macro.current_state)
        adjusted_index = current_index + steps
        print(current_index)
        if adjusted_index >= 0: #Prevents wrap-around
            try:
                self.lift_macro.current_state = list(self.lift_macro.STATE_DICT.keys())[adjusted_index]
                self.lift_macro.setpoint = list(self.lift_macro.STATE_DICT.values())[adjusted_index]
            except IndexError:
                pass


    def elevate_speed_safe(self, power):
        if not self.bottom_switch.get() and self.bottom_limit_switch.get() and power < 0:
            print("Slowly descending")
            #self.elevate_speed(.1 * power)
            self.elevate_speed(power * .1)
        elif not self.bottom_limit_switch.get() and power < 0:
            print("Stopping")
            self.lift_macro.macro_stop()
        else:
            self.elevate_speed(power)

    def engage_winch(self):
        self.winch_servo.setAngle(45)

    def release_winch(self):
        self.winch_servo.setAngle(0)

    def release(self):
        self.release_macro.release()
    def abort_release(self):
        self.release_macro.abort()
    def pickup(self):
        self.align_macro.align()
    def spring(self):
        self.wait_for_pickup()
        self.set_state('level4')
    def wait_for_pickup(self):
        self.align_macro.wait_for_align()

    def set_state(self, state):
        self.lift_macro.lift_to(state)

    def disable_all_macros(self):
        for macro in self.running_macros:
            if macro.enabled:
                macro.enabled = False

    def emergency_stop_all_macros(self):
        for macro in self.running_macros:
            macro.terminate()
            if macro.enabled:
                macro.enabled = False

    def emergency_restart_all_macros(self):
        self.kill_all_macros()
        for macro in self.running_macros:
            macro.run_threaded()
        #macro.thread.stop()

