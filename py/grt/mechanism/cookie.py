class Cookie:
    
    def __init__(self, p3):
        self.p3 = p3
    
    def hand_down(self):
        self.p3.set(True)
        
    def hand_up(self):
        self.p3.set(False)