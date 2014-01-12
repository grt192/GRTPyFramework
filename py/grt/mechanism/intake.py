#SQUARE INTAKE MECHANISM
class Intake:
    def __init__(self, roller):
        self.roller = roller
    def start_ep(self):
        self.roller.Set(1)
    def end_ep(self):
        self.roller.Set(0)
    def reverse(self):
        self.roller.Set(-1)
