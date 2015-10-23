from grt.core import GRTMacro
import time
class TwoStealMacro(GRTMacro):
	def __init__(self, bin_steal_mech, timeout=None):
		super().__init__(timeout)
		self.bin_steal_mech = bin_steal_mech

	def macro_initialize(self):
		self.bin_steal_mech.extend()
		time.sleep(.3)
		self.terminate()