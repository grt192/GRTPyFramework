

class Spider:
    def __init__(self, actuator):
        self.actuator = actuator

    def lower(self):
        self.actuator.set(True);

    def raise_(self):
        self.actuator.set(False);
