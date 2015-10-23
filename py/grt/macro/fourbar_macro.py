from collections import OrderedDict
from grt.core import GRTMacro

class FourBarMacro(GRTMacro):
    """
    Drive Macro; drives forwards a certain distance while
    maintaining orientation
    """
    leftSF = 1
    rightSF = -1
    distance = None
    previously_on_target = False

    def __init__(self, fourbar, distance=0, timeout=None, index_id=200):
        """
        Pass drivetrain, distance to travel (ft), and timeout (secs)
        """
        super().__init__(timeout)
        self.fourbar= fourbar
        self.distance = distance
        self.fourbar_encoder = fourbar.fourbar_encoder
        #self.STATE_DICT = {'level0_release' : 0, 'level0' : 0, 'level0.5_release' : 0, 'level0.5' : 7, 'level1_release' : 12, 'level1' : 17, 'level2_release' : 27, 'level2' : 33, 'level3_release' : 42, 'level3' : 50}
        self.STATE_DICT = OrderedDict()
        #self.STATE_DICT['full_down'] = 55
        self.STATE_DICT['down'] = 50
        self.STATE_DICT['up'] = 0
        #self.STATE_DICT['full_up'] = -5




        self.setpoint = distance
        self.zero = self.fourbar_encoder.e.getDistance()
        self.current_state = 'up'
        self.enabled = False
        self.at_top = False
        self.at_bottom = False
        self.index_id = index_id
        self.ERROR = 0
        self.counter = 0 #counter of attempted pickups
        self.prev_pressed = False #for counter
        #self.run_threaded()
        

    def macro_initialize(self):
        self.initial_distance = self.fourbar_encoder.e.getDistance()
        print("Initialized")

    def macro_periodic(self):
        """
        self.initial_distance = self.fourbar_encoder.e.getDistance()
        print(self.initial_distance)
        if(self.setpoint>self.initial_distance):
            while(self.traveled_distance() < self.setpoint * .8):
                print("travel: %f" % self.traveled_distance())
                self.fourbar.elevate_speed(.6)
                if not self.running:
                    print("Clearing close")
                    return
            while(self.traveled_distance() < self.setpoint):
                print("half power travel: %f" % self.traveled_distance())
                self.fourbar.elevate_speed(.3)
            self.fourbar.stop()
        elif(self.setpoint<self.initial_distance):
            while(self.traveled_distance() > self.setpoint * .8):
                print("travel: %f" % self.traveled_distance())
                self.fourbar.elevate_speed(-.6)
            while(self.traveled_distance() > self.setpoint):
                print("half power travel: %f" % self.traveled_distance())
                self.fourbar.elevate_speed(-.3)
            self.fourbar.stop()
        print("Cleared close")
        self.terminate()
        """
        #print("Polling")
        #print(self.initial_distance)
        #print(self.zero)

        #Move initial distance logic to a special if statement
        # that gets called only once when the macro is first enabled.
        # self.initialize() calls will be useless for these macros.
        #print(self.fourbar_encoder.distance)
        if self.enabled:
            self.ERROR = self.setpoint - self.fourbar_encoder.distance
            #If the setpoint is above the current distance.
            #print("Bottom switch: ", self.fourbar.bottom_switch.get())
            #print("Bottom limit switch: ", self.fourbar.bottom_limit_switch.get())
            #print("Encoder distance: ", self.fourbar_encoder.distance)
            #if not (self.fourbar.top_switch.get() and self.fourbar.bottom_switch.get()):
             #   self.macro_stop()
            if self.ERROR >= 0: # and self.fourbar.top_switch.get():
                #print("Started")
                #if self.ERROR < self.setpoint * .8:
                #    self.fourbar.elevate_speed(.6zse                #elif self.fourbar_encoder.distance < self.setpoint:
                #    self.fourbar.elevate_speed(.3)
                if self.ERROR > 3:
                    self.fourbar.elevate_speed(.8)
                if self.ERROR > 2 and abs(self.ERROR) <= 3:
                    self.fourbar.elevate_speed(.2)
                elif self.ERROR <= 2 and self.ERROR > .5:
                    self.fourbar.elevate_speed(.1)
                if self.ERROR <= .5:
                    #self.ERROR = 0
                    #print("Stopped +")
                    self.macro_stop()
            elif self.ERROR < 0:
                #print("Started")
                #if self.ERROR < self.setpoint * .8:
                #    self.fourbar.elevate_speed(.6)
                #elif self.fourbar_encoder.distance < self.setpoint:
                #    self.fourbar.elevate_speed(.3)
                if abs(self.ERROR) > 3:
                    self.fourbar.elevate_speed(-.8)
                if abs(self.ERROR) > 2 and abs(self.ERROR) <= 3:
                    self.fourbar.elevate_speed(-.2)
                elif abs(self.ERROR) <= 2 and abs(self.ERROR) > .5:
                    self.fourbar.elevate_speed(-.1)
                if abs(self.ERROR) <= .5:
                    #self.ERROR = 0
                    #print("Stopped -")
                    self.macro_stop()
            else:
                print("Stopping")
                #self.counter += 1
                #print(self.counter)
                self.macro_stop()

        """else:
            if not self.fourbar.bottom_switch.get() and self.fourbar.bottom_limit_switch.get() and self.fourbar.fourbar_motor.get() < 0:
                print("Slowly descending")
                #if self.fourbar.fourbar_motor.get() < 0:
                self.fourbar.elevate_speed(-.1)
            if not self.fourbar.bottom_limit_switch.get():
                if self.fourbar.fourbar_motor.get() < 0:
                    print("Stopping")
                    self.macro_stop()"""

            
        
        


            
            #if not self.fourbar.bottom_limit_switch.get():
            #    self.macro_stop()
            #else:
            #    self.macro_stop()

            #if not self.fourbar.top_switch.get():
             #   self.macro_stop()
              #  self.at_top = True
            #if not self.fourbar.bottom_switch.get():
             #   self.macro_stop()
              #  self.at_bottom = True




    def macro_stop(self):
        self.fourbar.stop()

    def re_zero(self):
        #We want to be able to do other things on the robot while the re-zeroing is occurring.
        temp_thread = threading.Thread(target=self.run_re_zero)
        temp_thread.start()

    def run_re_zero(self):
        tinit = time.time()
        tdif = time.time() - tinit
        while self.fourbar.bottom_limit_switch.get() and tdif < 5:
            self.enabled = False #Prevents the macro from fighting the re-zero.
            self.fourbar.elevate_speed_safe(-.2)
            tdif = time.time() - tinit
            time.sleep(.2)
        self.enabled = True
        self.fourbar_encoder.reset()
        self.setpoint = 0
        self.current_state = "level0"
        self.lift_to("level0")
        if self.fourbar.bottom_limit_switch.get():
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
            return self.fourbar_encoder.distance
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

        #return self.current_state, self.fourbar_encoder.distance, self.setpoint, self.ERROR
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
        self.setpoint = self.STATE_DICT[state] #-self.STATE_DICT[state] + self.fourbar_encoder.distance #self.STATE_DICT[self.current_state]
        self.current_state = state
        #self.terminate()
        #print("Open threads: ", threading.active_count())
        print(self.setpoint)
        print("Encoder distance: ", self.fourbar_encoder.distance)
        #self.run_threaded()
        #thread = threading.Thread(target=self.initialize)
        #thread.Start()
        #self.initialize()
        

    def traveled_distance(self):
        return abs(self.fourbar_encoder.distance - self.initial_distance)
        #return self.fourbar_encoder.distance

    """
    def run_fourbar_macro(self):
        if(self.setpoint>0):
            while(self.traveled_distance() < self.setpoint * .8):
                print("travel: %f" % self.traveled_distance())
                self.fourbar.elevate_speed(.6)
            while(self.traveled_distance() < self.setpoint):
                print("half power travel: %f" % self.traveled_distance())
                self.fourbar.elevate_speed(.3)
            self.fourbar.stop()
        elif(self.setpoint<0):
            while(self.traveled_distance() > self.setpoint * .8):
                print("travel: %f" % self.traveled_distance())
                self.fourbar.elevate_speed(-.6)
            while(self.traveled_distance() > self.setpoint):
                print("half power travel: %f" % self.traveled_distance())
                self.fourbar.elevate_speed(-.3)
            self.fourbar.stop()
        self.kill()
    """
   