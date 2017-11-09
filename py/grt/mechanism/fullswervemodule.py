import time
from math import sin, cos, atan, pi

T = 5

def square(x):
	return x * x

class Wheel(object):
	def __init__(self, vx, vy):
		self.theta = None
		self.target_theta = None
		self.last_changed = None
		self.r = None
		self.target_time = None
		self.vx = vx
		self.vy = vy
	def set_target(self, theta, target_theta, r):
		self.theta = theta
		self.target_theta = target_theta
		self.last_changed = time.time()
		self.r = r
		self.target_time = time.time()
	def update(self):
		global T
		if self.last_changed is None or time.time() - self.target_time >= T:
			return (0,0)
		dt = time.time() - self.last_changed
		self.last_changed = time.time()
		dt_st = time.time() - self.target_time # dt set target
		dts = square((self.target_theta - self.theta) / T)
		stheta = (1 - dt_st / T) * self.theta + (dt_st / T) * self.target_theta # sum of theta
		ax = self.r * dts * cos(stheta)
		ay = self.r * dts * sin(stheta)
		dvx = ax * dt
		dvy = ay * dt
		self.vx += dvx
		self.vy += dvy
		return (dvx, dvy)
		
wheel = Wheel(0, 0)
wheel.set_target(0, pi / 2, 3)
x = 0
y = 0
last_done = time.time()
while True:
	dt = time.time() - last_done
	last_done = time.time()
	dvx, dvy = wheel.update()
	x += dvx * dt
	y += dvy * dt
	print(x, y)
	time.sleep(.03)



































