__author__ = 'dhruv'

from wpilib import Joystick
from grt.core import SensorPoller, Sensor

class DriverStation(Sensor):
    """ Allows us to treat the Driver Station as a single sensor.

    It adds all the listeners of the joysticks to itself, and has inside it a sensor
    poller which polls the joysticks.
    """
    BUTTON_TABLE = []
    def __init__(self, joysticks):
        """ Initializes DS with a list of GRT joysticks """
        super().__init__()
        self.joysticks = joysticks
        self.joystick_poller = SensorPoller(self.joysticks)
        for i, joystick in enumerate(self.joysticks):
            self.BUTTON_TABLE.extend(["joy%s" % i + x for x in joystick.BUTTONTABLE])
            for listener in joystick.listeners:
                self.add_listener(listener)

    def poll(self):
        super().poll()
        self.joystick_poller.poll()
        self.state = dict((sensor, vars(sensor)) for sensor in self.joysticks)