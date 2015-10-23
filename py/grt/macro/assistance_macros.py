
from grt.core import GRTMacro
import wpilib
import threading
import time



class ReleaseMacro(GRTMacro):
    def __init__(self, elevator, dt, timeout=None):
        super().__init__(timeout)
        self.left_switch = elevator.left_switch
        self.right_switch = elevator.right_switch
        self.elevator = elevator
        self.elevator_motor = elevator.elevator_motor #change how the motor is being called!
        #ie. use the elevator's functions
        elevator.running_macros.append(self)
        self.enabled = False
        #self.run_threaded()
        self.dt = dt
    #while any switches are pressed, lower elevator
    def macro_periodic(self):
        if self.enabled:
            #if not self.l_switch.get() and not self.r_switch.get():
            #    self.dt.set_lf_scale_factors(1, 1)
            if self.l_switch.get() and self.r_switch.get():
                #if both buttons are pressed (both are False)
                self.dt.set_lf_scale_factors(1, 1)
                self.elevator.lower_half_step()
                self.dt.set_dt_output(0, 0)
                print('ALIGNED')
                #self.kill()
                self.enabled = False
                #stop the robot 

            """elif self.r_switch.get():
                #the right switch is pressed (because the left is not)
                #shut off the right side to turn into position
                self.dt.set_lf_scale_factors(1, .05)
            elif self.l_switch.get():
                #the left switch is pressed (because the right is not)
                #shut off the left side to turn into position
                self.dt.set_lf_scale_factors(.05, 1)
                #come to a stop
            """
            #else:
            #    self.dt.set_lf_scale_factors(1, 1)
            #print('ALIGNED')
    def macro_stop(self):
        self.elevator.stop()
        self.dt.set_dt_output(0)

    def release(self):
        #self.run_threaded() #forces the macro to thread
        self.enabled = True
    def abort(self):
        self.enabled = False


class AlignMacro(GRTMacro):
    '''
    Using limit switch info, automatically
    align the pickup with a tote.  
    '''

    def __init__(self, elevator, dt, timeout=None):
        super().__init__(timeout)

        self.dt = dt
        self.elevator = elevator
        self.l_switch = elevator.left_switch
        self.r_switch = elevator.right_switch
        self.aligning = False
        self.enabled = False
        self.has_touched = False
        self.backed_up = False
        self.run_threaded()

    def macro_periodic(self):
        '''
        Have the robot align itself by ramming into a box
        when it is reasonably close to it
        '''
        #ramming_power = 0.2
        #turning_power = 0.2
        #weak_turning = 0.1
        '''
        while(self.l_switch.get() and self.r_switch.get() and self.aligning ):
            #double check to make sure if this is the correct way to 
            #see if limit switches are pressed. 
            #"While neither switch is pressed" (i.e. both Gets give True)
            self.dt.set_dt_output(ramming_power, ramming_power)
    
            ##### TESTING STUFF #####
            #print('Left limit switch state: %f, Right limit switch state: %f'%(self.l_switch.get(), self.r_switch.get())
       '''
        #print("Left switch: ", self.l_switch.get())
        #print("Right switch: ", self.r_switch.get())
        self.better_align()
                #stop the robot 
            #elif self.r_switch.get():
                #the right switch is pressed (because the left is not)
                #shut off the right side to turn into position
            #    self.dt.set_lf_scale_factors(.5, -.3)
            #elif self.l_switch.get():
                #the left switch is pressed (because the right is not)
                #shut off the left side to turn into position
            #    self.dt.set_lf_scale_factors(-.3, .5)
                #come to a stop
            #else:
            #    self.dt.set_lf_scale_factors(1, 1)
            #print('ALIGNED')
    def old_align(self):
        if self.enabled:
            #if not self.l_switch.get() and not self.r_switch.get():
            #    self.dt.set_lf_scale_factors(1, 1)
            if self.l_switch.get() and self.r_switch.get():
                #if both buttons are pressed (both are False)
                #self.dt.set_lf_scale_factors(1, 1)
                self.elevator.set_state('level1')
                self.dt.set_dt_output(0, 0)
                print('ALIGNED')
                #self.kill()
                self.enabled = False

    def better_align(self):
        
        if self.enabled:
            if not self.has_touched:
                if self.l_switch.get() or self.r_switch.get():
                    self.dt.disable()
                    self.dt.set_dt_output(-.15, -.15)
                    self.has_touched = True

            elif self.has_touched:
                if self.l_switch.get() or self.r_switch.get():
                    self.dt.set_dt_output(-.15, -.15)
                else:
                    self.dt.set_dt_output(.15, .15)
                    self.has_touched = False
                    self.backed_up = True
            if self.backed_up:
                if self.l_switch.get() and self.r_switch.get():
                    self.elevator.set_state('level1')
                    time.sleep(1)
                    self.dt.set_dt_output(0, 0)
                    self.backed_up = False
                    self.has_touched = False
                    self.dt.enable()
                    self.enabled = False
                elif self.l_switch.get():
                    self.dt.set_dt_output(-.1, .2)
                elif self.r_switch.get():
                    self.dt.set_dt_output(.2, -.1)
                else:
                    self.dt.set_dt_output(.15, .15)
        else:
            self.dt.enable()

        #self.dt.set_dt_output(-.2, -.2)
        #time.sleep(.25)

    def align(self):
        #self.run_threaded()
        self.enabled = True

    def wait_for_align(self):
        #self.run_linear()
        self.process.join(timeout=2)

    
    def macro_stop(self):
        #self.aligning = False
        self.dt.set_dt_output(0, 0)

    #def wait_for_align(self):
        #Do the same thing here. NOT threaded.




#constants = Constants()
from collections import OrderedDict

class ElevatorMacro(GRTMacro):
    """
    Drive Macro; drives forwards a certain distance while
    maintaining orientation
    """
    leftSF = 1
    rightSF = -1
    distance = None
    previously_on_target = False

    def __init__(self, elevator, distance=0, timeout=None, index_id=100):
        """
        Pass drivetrain, distance to travel (ft), and timeout (secs)
        """
        super().__init__(timeout)
        self.elevator= elevator
        self.distance = distance
        self.elevator_encoder = elevator.elevator_encoder
        #self.STATE_DICT = {'level0_release' : 0, 'level0' : 0, 'level0.5_release' : 0, 'level0.5' : 7, 'level1_release' : 12, 'level1' : 17, 'level2_release' : 27, 'level2' : 33, 'level3_release' : 42, 'level3' : 50}
        self.STATE_DICT = OrderedDict()
        self.STATE_DICT['level0_release'] = 0
        self.STATE_DICT['level0'] = 0
        self.STATE_DICT['level0.5_release'] = 0
        self.STATE_DICT['level0.5'] = 7
        self.STATE_DICT['level1_release'] = 13
        self.STATE_DICT['level1'] = 22
        self.STATE_DICT['level2_release'] = 25
        self.STATE_DICT['level2'] = 35
        self.STATE_DICT['level3_release'] = 36
        self.STATE_DICT['level3'] = 48
        self.STATE_DICT['level4_release'] = 49.5
        self.STATE_DICT['level4'] = 54.5

        self.setpoint = distance
        self.zero = self.elevator_encoder.e.getDistance()
        self.current_state = 'level0'
        self.enabled = True
        self.at_top = False
        self.at_bottom = False
        self.index_id = index_id
        self.ERROR = 0
        self.counter = 0 #counter of attempted pickups
        self.prev_pressed = False #for counter
        self.run_threaded()
        

    def macro_initialize(self):
        self.initial_distance = self.elevator_encoder.e.getDistance()
        print("Initialized")

    def macro_periodic(self):
        """
        self.initial_distance = self.elevator_encoder.e.getDistance()
        print(self.initial_distance)
        if(self.setpoint>self.initial_distance):
            while(self.traveled_distance() < self.setpoint * .8):
                print("travel: %f" % self.traveled_distance())
                self.elevator.elevate_speed(.6)
                if not self.running:
                    print("Clearing close")
                    return
            while(self.traveled_distance() < self.setpoint):
                print("half power travel: %f" % self.traveled_distance())
                self.elevator.elevate_speed(.3)
            self.elevator.stop()
        elif(self.setpoint<self.initial_distance):
            while(self.traveled_distance() > self.setpoint * .8):
                print("travel: %f" % self.traveled_distance())
                self.elevator.elevate_speed(-.6)
            while(self.traveled_distance() > self.setpoint):
                print("half power travel: %f" % self.traveled_distance())
                self.elevator.elevate_speed(-.3)
            self.elevator.stop()
        print("Cleared close")
        self.terminate()
        """
        #print("Polling")
        #print(self.initial_distance)
        #print(self.zero)

        #Move initial distance logic to a special if statement
        # that gets called only once when the macro is first enabled.
        # self.initialize() calls will be useless for these macros.
        #print(self.elevator_encoder.distance)
        if self.enabled:
            self.ERROR = self.setpoint - self.elevator_encoder.distance
            #If the setpoint is above the current distance.
            print("Bottom switch: ", self.elevator.bottom_switch.get())
            print("Bottom limit switch: ", self.elevator.bottom_limit_switch.get())
            print("Encoder distance: ", self.elevator_encoder.distance)
            #if not (self.elevator.top_switch.get() and self.elevator.bottom_switch.get()):
             #   self.macro_stop()
            if self.ERROR >= 0: # and self.elevator.top_switch.get():
                #print("Started")
                #if self.ERROR < self.setpoint * .8:
                #    self.elevator.elevate_speed(.6zse                #elif self.elevator_encoder.distance < self.setpoint:
                #    self.elevator.elevate_speed(.3)
                if self.ERROR > 3:
                    self.elevator.elevate_speed(.4)
                if self.ERROR > 2 and abs(self.ERROR) <= 3:
                    self.elevator.elevate_speed(.1)
                elif self.ERROR <= 2 and self.ERROR > .5:
                    self.elevator.elevate_speed(.1)
                if self.ERROR <= .5:
                    #self.ERROR = 0
                    #print("Stopped +")
                    self.macro_stop()
            elif self.ERROR < 0 and self.elevator.bottom_switch.get():
                #print("Started")
                #if self.ERROR < self.setpoint * .8:
                #    self.elevator.elevate_speed(.6)
                #elif self.elevator_encoder.distance < self.setpoint:
                #    self.elevator.elevate_speed(.3)
                if abs(self.ERROR) > 3:
                    self.elevator.elevate_speed(-.4)
                if abs(self.ERROR) > 2 and abs(self.ERROR) <= 3:
                    self.elevator.elevate_speed(-.1)
                elif abs(self.ERROR) <= 2 and abs(self.ERROR) > .5:
                    self.elevator.elevate_speed(-.1)
                if abs(self.ERROR) <= .5:
                    #self.ERROR = 0
                    #print("Stopped -")
                    self.macro_stop()
            elif not self.elevator.bottom_switch.get() and self.elevator.bottom_limit_switch.get():
                print("Slowly descending")
                self.elevator.elevate_speed(-.2)

            else:
                print("Stopping")
                #self.counter += 1
                #print(self.counter)
                self.macro_stop()

        """else:
            if not self.elevator.bottom_switch.get() and self.elevator.bottom_limit_switch.get() and self.elevator.elevator_motor.get() < 0:
                print("Slowly descending")
                #if self.elevator.elevator_motor.get() < 0:
                self.elevator.elevate_speed(-.1)
            if not self.elevator.bottom_limit_switch.get():
                if self.elevator.elevator_motor.get() < 0:
                    print("Stopping")
                    self.macro_stop()"""

            
        if not self.elevator.bottom_limit_switch.get() and not self.prev_pressed:
            self.counter += 1
            self.prev_pressed = True
            print(self.counter)
        elif self.elevator.bottom_limit_switch.get():
            self.prev_pressed = False
        


            
            #if not self.elevator.bottom_limit_switch.get():
            #    self.macro_stop()
            #else:
            #    self.macro_stop()

            #if not self.elevator.top_switch.get():
             #   self.macro_stop()
              #  self.at_top = True
            #if not self.elevator.bottom_switch.get():
             #   self.macro_stop()
              #  self.at_bottom = True




    def macro_stop(self):
        self.elevator.stop()

    def re_zero(self):
        #We want to be able to do other things on the robot while the re-zeroing is occurring.
        temp_thread = threading.Thread(target=self.run_re_zero)
        temp_thread.start()

    def run_re_zero(self):
        tinit = time.time()
        tdif = time.time() - tinit
        while self.elevator.bottom_limit_switch.get() and tdif < 5:
            self.enabled = False #Prevents the macro from fighting the re-zero.
            self.elevator.elevate_speed_safe(-.2)
            tdif = time.time() - tinit
            time.sleep(.2)
        self.enabled = True
        self.elevator_encoder.reset()
        self.setpoint = 0
        self.current_state = "level0"
        self.lift_to("level0")
        if self.elevator.bottom_limit_switch.get():
            print("Re-zeroing has timed out! The encoder has been reset anyway, but the zero may not be correct.")
        else:
            print("Re-zeroing successfully completed.")

    def getDeviceID(self):
        #Yes, this is pretending to be a Talon.
        return self.index_id
    def get(self):
        """if self.index_id == 0:
            return self.current_state
        elif self.index_id == 1:
            return self.elevator_encoder.distance
        elif self.index_id == 2:
            return self.setpoint
        elif self.index_id == 3:
            return self.ERROR
        else:
            print("This index does not record anything.")
            return "No record"
        """
        """
        Call the following code (or something similar) on this tuple to re-parse it
        and return the value you want:

        a = [(1,2,3),(4,5,6),(7,8,9)]
        b = []
        for i in a:
            b.append(i[0])  #Replace 0 with the index you want.
        print(b)

        Yes, this means that the instructions will be an ordered dictionary of lists of tuples. :)
        """

        #return self.current_state, self.elevator_encoder.distance, self.setpoint, self.ERROR
        return self.setpoint

    def set(self, state):
        #wanted_instructions = []
        #wanted_instructions.append()
        self.setpoint = state #state[2]
        #print(state)

    def lift_to(self, state):
        #Add in self.enabled logic here!
        #These macros are always running, each in their own separate background thread, but 
        #they only do anything interesting when enabled by their specific methods.
        #They can also stop themselves easily (or be stopped by something else easily)
        #by disabling them. 
        #In an emergency, their threads can also be terminated. This method will require
        #the macro's thread to be restarted before it can be used again.
        #self.running = False
        self.initial_distance = 0
        self.setpoint = self.STATE_DICT[state] #-self.STATE_DICT[state] + self.elevator_encoder.distance #self.STATE_DICT[self.current_state]
        self.current_state = state
        #self.terminate()
        #print("Open threads: ", threading.active_count())
        print(self.setpoint)
        print("Encoder distance: ", self.elevator_encoder.distance)
        #self.run_threaded()
        #thread = threading.Thread(target=self.initialize)
        #thread.Start()
        #self.initialize()
        

    def traveled_distance(self):
        return abs(self.elevator_encoder.distance - self.initial_distance)
        #return self.elevator_encoder.distance

    """
    def run_elevator_macro(self):
        if(self.setpoint>0):
            while(self.traveled_distance() < self.setpoint * .8):
                print("travel: %f" % self.traveled_distance())
                self.elevator.elevate_speed(.6)
            while(self.traveled_distance() < self.setpoint):
                print("half power travel: %f" % self.traveled_distance())
                self.elevator.elevate_speed(.3)
            self.elevator.stop()
        elif(self.setpoint<0):
            while(self.traveled_distance() > self.setpoint * .8):
                print("travel: %f" % self.traveled_distance())
                self.elevator.elevate_speed(-.6)
            while(self.traveled_distance() > self.setpoint):
                print("half power travel: %f" % self.traveled_distance())
                self.elevator.elevate_speed(-.3)
            self.elevator.stop()
        self.kill()
    """
   