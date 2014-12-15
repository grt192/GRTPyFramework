__author__ = "Calvin Huang"

try:
    from wpilib import Joystick
except ImportError:
    from pyfrc.wpilib import Joystick
from grt.core import Sensor
from collections import OrderedDict

BUTTON_TABLE = OrderedDict([('trigger' , 0), ('button2' , 0), ('button3' , 0),
                ('button4' , 0), ('button5' , 0), ('button6' , 0),
                ('button7' , 0), ('button8' , 0), ('button9' , 0),
                ('button10' , 0), ('button11' , 0), ('x_axis' , 0), ('y_axis' , 0)])


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
        
        """for key in BUTTON_TABLE:
            i = 1
            BUTTON_TABLE[key] = JoystickButton(self.j, i)
            i+=1"""

    def poll(self):
        #for i, state_id in enumerate(BUTTON_TABLE, 1):
         #   self.update_state(state_id,
          #                    self.j.GetRawButton(i))
            # button index is offset by 1 due to wpilib 1-indexing
        for i in range(1,11):
            BUTTON_TABLE[i-1] = self.j.GetRawButton(i)
        BUTTON_TABLE[11] = self.j.GetX()
        BUTTON_TABLE[12] = self.j.GetY()
        self.x_axis = self.j.GetX()
        self.y_axis = self.j.GetY()
        self.magnitude = self.j.GetMagnitude()
        self.direction = self.j.GetDirectionDegrees()

    def get_button(self, number):
        return self.j.GetRawButton(number)
    def get_trigger(self):
        return self.j.GetRawButton(1)
    def get_x(self):
        return self.j.GetX()
    def get_y(self):
        return self.j.GetY()
