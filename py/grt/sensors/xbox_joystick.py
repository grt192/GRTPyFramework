__author__ = "Calvin Huang"

from wpilib import Joystick
from grt.core import Sensor

BUTTON_TABLE = ['a_button', 'b_button', 'x_button', 'y_button',
                'l_shoulder', 'r_shoulder', 'back_button',
                'start_button']


class XboxJoystick(Sensor):
    """
    Sensor wrapper for the Xbox Controller.

    Has boolean attributes for buttons: a/b/x/y/back/start_button,
    l/r_shoulder
    Attributes l/r_x/y_axis for thumbstick positions
    trigger_pos and keypad_pos for trigger and keypad position
    """

    l_x_axis = l_y_axis = r_x_axis = r_y_axis = 0
    trigger_pos = keypad_pos = 0
    a_button = b_button = x_button = y_button = False
    l_shoulder = r_shoulder = back_button = start_button = False

    def __init__(self, port):
        """
        Initializes the joystick with some USB port.
        """
        super().__init__()
        self.j = Joystick(port)

    def poll(self):
        for i, state_id in enumerate(BUTTON_TABLE):
            self.update_state(state_id,
                              self.j.GetRawButton(i + 1))
            # button index is offset by 1 due to wpilib 1-indexing

        self.l_x_axis = self.j.GetX()
        self.l_y_axis = self.j.GetY()
        self.r_x_axis = self.j.GetRawAxis(4)
        self.r_y_axis = self.j.GetRawAxis(5)
        self.trigger_pos = self.j.GetZ()
        self.keypad_pos = self.j.GetRawAxis(6)
