class Hand:
	def __init__(self, p1):
		self.p1 = p1
		
	def out(self):
		self.p1.set(True)
		
	def back(self):
		self.p1.set(False)
