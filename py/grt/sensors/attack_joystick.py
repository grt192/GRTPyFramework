__author__ = "Calvin Huang"

from wpilib import Joystick
from grt.core import Sensor

BUTTON_TABLE = ['trigger', 'button2', 'button3',
                'button4', 'button5', 'button6',
                'button7', 'button8', 'button9',
                'button10', 'button11']


class Attack3Joystick(Sensor):
    """
    Sensor wrapper for the Attack 3 Joystick.

    Has boolean attributes for buttons: trigger, button2-9
    and double x_axis, y_axis for joystick position
    """

    x_axis = y_axis = 0
    trigger = button2 = button3 = \
        button4 = button5 = button6 = \
        button7 = button8 = button9 = \
        button10 = button11 = False

    def __init__(self, port):
        """
        Initializes the joystick with some USB port.
        """
        super().__init__()
        self.j = Joystick(port)

    def poll(self):
        for i, state_id in enumerate(BUTTON_TABLE, 1):
            self.update_state(state_id,
                              self.j.getRawButton(i))

        self.x_axis = self.j.getX()
        self.y_axis = self.j.getY()
