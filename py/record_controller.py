import threading
import time
from collections import OrderedDict
from grt.core import GRTMacro
try:
    import wpilib
except ImportError:
    from pyfrc import wpilib

class RecordMacro(GRTMacro):

    def __init__(self, obj_list, timeout=None):
        super().__init__(timeout)
        self.obj_list = obj_list #list of objects to record
        #self.running = False
        self.instructions = OrderedDict() #dictionary of instructions to save
        self.enabled = False
        """
        This ridiculous for loop sets up a dictionary containing the objects passed in, and their output values.
        It may be easier to replace it with a 2D list.
        """
        for i in range(len(self.obj_list)):
            self.instructions["{0}, {1}".format(self.obj_list[i].getDeviceID() , type(self.obj_list[i]))] = [self.obj_list[i].get()]
        self.run_threaded()


    def engage(self):
        """
        Called in a higher level controller.
        Starts recording in a separate thread.
        """
        #self.running = True
        self.thread = threading.Thread(target=self.run_record)
        self.thread.start()

    def disengage(self):
        """
        Signals recording thread to stop.
        """
        #self.running = False

    def start_record(self):
        self.instructions = OrderedDict()
        for i in range(len(self.obj_list)):
            self.instructions["{0}, {1}".format(self.obj_list[i].getDeviceID() , type(self.obj_list[i]))] = [self.obj_list[i].get()]
        self.enabled = True

    def stop_record(self):
        self.enabled = False
        print(self.instructions)
        self.save("/home/lvuser/py/instructions.py")
        return self.instructions

    def macro_periodic(self):
        """
        Appends the output values of all the objects passed into __init__
        to the instructions dictionary. Sample rate is currently hard-coded.
        """
        #while self.running:
        #print("Operating")
        if self.enabled:
            i = 0
            tinit = time.time()
            for key in self.instructions:
                self.instructions[key].append(self.obj_list[i].get())
                #print(self.obj_list[i].Get())
                i += 1
            #wpilib.Wait(.1)
            time.sleep(.1 - (time.time() - tinit))
    def save(self, file_name):
        with open(file_name, 'a') as f:
            f.write(str(self.instructions) + "\n") 

class PlaybackMacro(GRTMacro):

    def __init__(self, instructions, talon_arr_obj, revert_controller=None, timeout=None):
        super().__init__(timeout)
        self.instructions = instructions #instructions to output
        self.talon_arr_obj = talon_arr_obj #talons to output instructions to
        self.revert_controller = revert_controller #drive controller to revert control to when finished
        
        #self.running = False
        self.enabled = False
        self.i = 0
        #parsing the dictionary into talon and solenoid components.
        self.parse()
        
        #self.run_threaded(no_initialize=True)
        #self.playback()
    def load(self, file_name):
        #assumes we have a python file (*.py)
        with open(file_name, 'r') as f:
            for line in f:
                self.instructions = eval(line.replace("\n", ""))
                #print(line)
        #self.instructions = instructions

    def parse(self):
        self.talon_arr = [] #lists that the dictionary will be parsed into
        self.solenoid_arr = []
        for key in self.instructions:
            i = int(key.split(',')[0])
            print(i)
            if "Talon" in key or "Macro" in key:
                self.talon_arr.append(self.instructions[key])
                #print(self.instructions[key])
                print(self.talon_arr)
            if "Solenoid" in key:
                self.solenoid_arr[i] = self.instructions[key]

    def engage(self):
        """
        Called in a higher level controller.
        Starts playback in a separate thread.
        """
        self.running = True
        self.thread = threading.Thread(target=self.run_playback)
        self.thread.start()

    def start_playback(self, instructions=None):
        #self.enabled = True
        if instructions:
            self.instructions = instructions
        self.parse()
        self.run_threaded()

    def stop_playback(self):
        self.terminate()

    def macro_initialize(self):
        """
        To be called only to use this LINEARLY in auto.
        """
        #pass
        #self.enabled = True
        print("Began playback")
        #self.process.join(timeout = 2)
        #print("Ended join")
        #self.terminate()

    def macro_stop(self):
        """
        Signals playback thread to stop.
        Also zeros all motor outputs.
        """
        #self.running = False
        self.enabled = False
        for talon in self.talon_arr_obj:
            if str(type(talon)) == "<class 'wpilib.cantalon.CANTalon'>":
                talon.set(0)

        #self.revert_controller.engage()

    def macro_periodic(self):
        """
        Iterates through the provided instruction dictionary.
        Disengages itself when finished.
        """
        #for i in range(len(self.talon_arr[0])):
        print("Enabled")
        tinit = time.time()
        try:
            print(str(range(len(self.talon_arr[0]))))
            for j in range(len(self.talon_arr)):   ###IMPORTANT NOTE!!! 
            #THIS WAS CHANGED FROM len(self.talon_arr) to len(self.talon_arr_obj)
            #IT SHOULD STILL WORK, but be sure to change it back at some point.
                self.talon_arr_obj[j].set(self.talon_arr[j][self.i])
                print(self.talon_arr[j][self.i])
                print("J: " + str(j))
                print(self.i)
            self.i += 1
            #wpilib.Wait(.1)
            time.sleep(.1 - (time.time() - tinit))
        except IndexError:
            self.enabled = False
            self.i = 0
            self.macro_stop()
            self.terminate()
            #self.disengage()
