from record_controller import RecordController, PlaybackController
import sys
from collections import OrderedDict
class TeleopController:

    def __init__(self, driver_stick, drive_controller, talon_arr, sp, hid_sp):
        """
        Self. conversion of inputs.
        """
        self.driver_stick = driver_stick
        self.drive_controller = drive_controller
        self.talon_arr = talon_arr
        self.sp = sp
        self.hid_sp = hid_sp

        """
        Temporary instructions to test playback controller.
        """
        self.instructions = OrderedDict([("1, <class 'grt.sensors.talon.Talon'>", [0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 0.17142857142857137, 0.17142857142857137, 0.17142857142857137, 0.17142857142857137, 0.17142857142857137]), ("2, <class 'grt.sensors.talon.Talon'>", [0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, 0.2571428571428571, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -0.6285714285714286, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, -1.1714285714285715, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 0.1428571428571429, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 1.2571428571428571, 0.17142857142857137, 0.17142857142857137, 0.17142857142857137, 0.17142857142857137, 0.17142857142857137])])
        
        """
        Declaration of playback and record controllers.
        Should be moved to config.
        """
        self.record_controller = RecordController([talon_arr[0], talon_arr[1]])
        self.playback_controller = PlaybackController(self.instructions, self.talon_arr, revert_controller=self.drive_controller)
        """
        Irritating boolean used to screen out joystick input while playing
        back a set of instructions.
        """
        self.playback = False

        """
        Engages the drive controller at initialize time to cut down on lag later on.
        """
        self.drive_controller.engage()
        #self.mech_controller.engage()

        """
        Adds its own _joylistener method as a listener in order to take in 
        joystick input.
        """
        self.driver_stick.add_listener(self._joylistener)

    def poll(self):
        self.sp.poll()
        self.hid_sp.poll()
        

    def _joylistener(self, sensor, state_id, datum):

        """
        This button will allow for faster reboots by triggering an 
        exception to force robotpy to reload the code.
        """

        if state_id == "button10":
            if datum:
                raise NameError('Rebooting')

        """
        These buttons engage and disengage the recording controller.
        Because the recording controller does not take over any outputs,
        no other conditions are necessary.
        """

        if state_id == "button9":
            if datum:
                self.record_controller.engage()
        if state_id == "button8":
            if datum:
                self.record_controller.disengage()
                del self.playback_controller
                self.playback_controller = PlaybackController(self.record_controller.instructions, self.talon_arr, revert_controller = self.drive_controller)
                print(self.record_controller.instructions)



        """
        These buttons engage and disengage the playback controller.
        They have extra conditions in their if statements to prevent 
        extra button presses from causing trouble.
        """

        if state_id == "button7":
            if datum and not self.playback: #prevents extra presses from causing issues
                    self.drive_controller.disengage()
                    self.playback_controller.engage()
                    self.playback = True
        if state_id == "button6":
            if datum and self.playback: #same as above
                self.playback_controller.disengage()
                self.drive_controller.engage()
                self.playback = False



"""
Junk test code.
if self.driver_stick.j.GetRawButton(10):
                #raise NameError('Rebooting')
                self.recording = True
                #self.playback = True
      
        if self.playback:
            self.playback_controller.playback()
        elif self.recording:
            self.drive_controller.update()
            self.record_controller.record()
            #self.drive_controller.update_and_record()
        else:
            #self.mech_controller.update()
            self.drive_controller.update()

        if self.record_controller.finished:
            self.recording = False
            self.record_controller.finished = False
            print(self.record_controller.instructions)
            sys.exit(0)
"""
