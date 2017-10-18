 

 class BigGhost:
 	def __init__(self, actuator):
        self.actuator = actuator

    def extend(self):
        self.actuator.set(True);

    def retract(self):
        self.actuator.set(False);