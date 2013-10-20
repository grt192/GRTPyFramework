__author__ = "Calvin Huang"

from wpilib import Joystick
from grt.core import Sensor

BUTTON_TABLE = ['a_button', 'b_button', 'x_button', 'y_button',
                'l_shoulder', 'r_shoulder', 'back_button',
                'start_button']

class XboxJoystick(Sensor):
    '''
    Sensor wrapper for the Xbox Controller.

    Has boolean attributes for buttons: a/b/x/y/back/start_button,
    l/r_shoulder
    Attributes l/r_x/y_axis for thumbstick positions
    trigger_pos and keypad_pos for trigger and keypad position
    '''

    def __init__(self, port):
        '''
        Initializes the joystick with some USB port.
        '''
        super().__init__()
        j = Joystick(port)

    def poll(self):
        for i, state_id in enumerate(BUTTON_TABLE):
            self.update_state(state_id,
                              j.getRawButton(i + 1))
            # button index is offset by 1 due to wpilib 1-indexing

        self.update_state('l_x_axis', j.getX())
        self.update_state('l_y_axis', j.getY())
        self.update_state('r_x_axis', j.getRawAxis(4))
        self.update_state('r_y_axis', j.getRawAxis(5))
        self.update_state('trigger_pos', j.getZ());
        self.update_state('keypad_pos', j.getRawAxis(6))
