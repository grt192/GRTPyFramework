__author__ = "Calvin Huang"

from wpilib import DriverStation
from grt.core import Sensor

# button/pin pair list
BUTTON_TABLE = [('button1', 1), ('button2', 3), ('button3', 5),
                ('button4', 7), ('button5', 9), ('button6', 11),
                ('button7', 13), ('button8', 15),
                ('l_toggle', 10), ('r_toggle', 12),
                ('orange_button', 14), ('green_button', 16)]

REGISTER_CLK = 2;
REGISTER_D1 = 6;
REGISTER_D2 = 8;
REGISTER_LOAD = 4;

IOBOARD = DriverStation.GetInstance().GetEnhancedIO()

class ButtonBoard(Sensor):
    '''
    Sensor wrapper for the Attack 3 Joystick.

    Has boolean attributes for buttons: trigger, button2-9
    and double x_axis, y_axis for joystick position
    '''

    def __init__(self):
        '''
        Constructs a new ButtonBoard. Only one should be instantiated.
        '''
        super().__init__()
        for name, pin in BUTTON_TABLE:
            IOBOARD.SetDigitalConfig(pin, IOBOARD.tDigitalConfig.kInputPullUp)

        for i in (REGISTER_CLK, REGISTER_D1, REGISTER_D2, REGISTER_LOAD):
            IOBOARD.SetDigitalConfig(i, IOBOARD.tDigitalConfig.kOutput)


    def poll(self):
        digstate = IOBOARD.GetDigitals()  # bit-packed button states
        for name, pin in BUTTON_TABLE:
            self.update_state(name, ((digstate >> (pin - 1)) & 1) == 0)

    # TODO LEDs
