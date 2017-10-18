class Giraffe:
    
    def __init__(self, p1):
        self.p1 = p1
    
    def head_down(self):
        self.p1.set(True)
        
    def head_up(self):
        self.p1.set(False)