__author__ = "Calvin Huang"

try:
    from wpilib import Joystick
except ImportError:
    from pyfrc.wpilib import Joystick
from grt.core import Sensor

BUTTON_TABLE = ['trigger', 'button2', 'button3',
                'button4', 'button5', 'button6',
                'button7', 'button8', 'button9',
                'button10', 'button11']


class TwistJoystick(Sensor):
    """
    Sensor wrapper for the Attack 3 Joystick.

    Has boolean attributes for buttons: trigger, button2-9
    and double x_axis, y_axis for joystick position
    """

    x_axis = y_axis = twist_axis = 0
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
                              self.j.GetRawButton(i))
            # button index is offset by 1 due to wpilib 1-indexing

        self.x_axis = self.j.GetX()
        self.y_axis = self.j.GetY()
        self.magnitude = self.j.GetMagnitude()
        self.direction = self.j.GetDirectionDegrees()
        self.twist_axis = self.j.GetZ()
