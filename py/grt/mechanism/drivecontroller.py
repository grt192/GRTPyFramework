"""
Module for various drivetrain control mechanisms.
Listens to Attack3Joysticks, not wpilib.Joysticks.
"""

from time import time

class ArcadeDriveController:
    """
    Class for controlling DT in arcade drive mode, with one or two joysticks.
    """

    def __init__(self, dt, l_joystick, r_joystick=None, f_rec=None, f_play=None, rec_test=False, freq=10):
        """
        Initialize arcade drive controller with a DT and up to two joysticks.
        f_rec is an optional file (string) that will contain recorded joystick output
        f_play is an optional file (string) that will "play" recorded output
        freq is the #times/second to record joystick input to the file
        """
        self.dt = dt
        self.l_joystick = l_joystick
        self.r_joystick = r_joystick
        self.f_rec = f_rec
        self.recording = False
        self.freq = freq
        l_joystick.add_listener(self._joylistener)
        if r_joystick:
            r_joystick.add_listener(self._joylistener)
        if rec_test:
            self.f_rec = 'test_recording.txt'
            self.f_play = self.f_rec
            open(self.f_rec, 'w').close() #empty contents of file
            

    def _joylistener(self, sensor, state_id, datum):
        if sensor in (self.l_joystick, self.r_joystick) and state_id in ('x_axis', 'y_axis'):
            power = -self.l_joystick.y_axis
            turnval = self.r_joystick.x_axis if self.r_joystick else self.l_joystick.x_axis
            # get turn value from r_joystick if it exists, else get it from l_joystick
            self.dt.set_dt_output(power - turnval,
                                  power + turnval)
            #store DT ouputs in file if recording
            if self.recording:
                if time() - self.last_time > 1.0/self.freq:
                    out.write("%f %f\n"%(power - turnval, power + turnval))
                    self.last_time = time() #this timing scheme works
                    #very similarly to how the Ticker works
        elif sensor == self.l_joystick and state_id == 'trigger':
            if datum:
                self.dt.upshift()
            else:
                self.dt.downshift()
        elif sensor == 'button1' and f_rec:
            #assume button1 starts recording
            if datum:
                out = open(f_rec, 'w') #open in the file in "write" mode
                self.recording = True
                self.last_time = time()
        elif sensor == 'button2':
            #assume button2 stops recording
            #add a failsafe to close file if 
            #even if button2 is not pressed
            if datum:
                self.recording = False
                out.close() #close the output file
        elif sensor == 'button3' and f_play:
            #assume button3 is the "play" button
            if datum:
                with open(f_play, 'r') as f:
                    for line in f:
                        a, b = map(float, line.split())
                        self.dt.set_dt_output(a, b)


class TankDriveController:
    """
    Class for controlling DT in tank drive mode with two joysticks.
    """

    def __init__(self, dt, l_joystick, r_joystick):
        """
        Initializes self with a DT and left and right joysticks.
        """
        self.dt = dt
        self.l_joystick = l_joystick
        self.r_joystick = r_joystick
        l_joystick.add_listener(self._joylistener)
        r_joystick.add_listener(self._joylistener)

    def _joylistener(self, sensor, state_id, datum):
        if sensor in (self.l_joystick, self.r_joystick) and state_id in ('x_axis', 'y_axis'):
            self.dt.set_dt_output(self.l_joystick.y_axis,
                                  self.r_joystick.y_axis)
