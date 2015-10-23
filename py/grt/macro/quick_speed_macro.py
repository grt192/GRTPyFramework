from grt.core import GRTMacro
import time
class QuickSpeedMacro(GRTMacro):
	def __init__(self, dt, timeout=None):
		super().__init__(timeout)
		self.dt = dt

	def macro_initialize(self):
		self.dt.set_dt_output(1, 1)
		time.sleep(.5)
		self.dt.set_dt_output(0, 0)
		self.terminate()