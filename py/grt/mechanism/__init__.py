from grt.core import Constants

constants = Constants()

'''
class Elevator:

    motor_power = .75

    def __init__(self, motor):
        self.motor = motor
        self.set_ep(self.motor_power)

    def set_ep(self, power):
        self.motor.Set(power * self.motor_power)

    def start_ep(self):
        self.motor.Set(self.motor_power)

    def stop_ep(self):
        self.motor.Set(0)

    def reverse_ep(self):
        self.motor.Set(-self.motor_power)

class Intake:

    motor_power = 1

    def __init__(self, roller):
        self.roller = roller
        self.set_ep(self.motor_power)

    def set_ep(self, power):
        self.roller.Set(power * self.motor_power)

    def start_ep(self):
        self.roller.Set(self.motor_power)

    def stop_ep(self):
        self.roller.Set(0)

    def reverse_ep(self):
        self.roller.Set(-self.motor_power)

class PneumaticRelease:

    def __init__(self, pneumatic):
        self.pneumatic = pneumatic

    def release_open(self):
        self.pneumatic.Set(1)

    def release_closed(self):
        self.pneumatic.Set(0)
'''

class Pickup:
	def __init__(self, roller, elev, actuator):
		'''
		roller: the roller motor
		elev: the elevation motor
		actuator: the penumatic
		'''
		self.roller = roller
		self.elev = elev
		self.actuator = actuator
	def roll_in(self):
		self.roller.Set(0.5)
	def roll_out(self):
		self.roller.Set(-0.5)
	def roll_stop(self):
		self.roller.Set(0)
	def extend(self):
		self.actuator.Set(True)
	def retract(self):
		self.actuator.Set(False)
	def up(self):
		self.elev.Set(1)
	def down(self):
		self.elev.Set(-1)
	def elev_stop(self):
		self.elev.Set(0)