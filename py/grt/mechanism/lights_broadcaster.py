"""
Describes the interface between the lights
controller running on the laptop and the robot.
"""
__author__ = "Trevor Nielsen"

class LightsBroadcaster(Object):
    """
    Listens to various variables on the robot and pushes
    updates to network tables.
    """

    def __init__(self, networkTable):
        self.networkTable = networkTable

    def _valueListener(self, sensor, state_id, datum):
        
