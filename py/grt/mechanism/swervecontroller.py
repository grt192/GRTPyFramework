import math
from ctre import CANTalon
from collections import OrderedDict


class SwerveController:

	def __init__(self, joystick, xbox_controller, swerve_module):

		self.swerve_module = swerve_module

		self.joystick = joystick
		self.xbox_controller = xbox_controller

		self.ackerman_power = .7
		self.strafe_power = 1
		
		try:
			self.joystick.add_listener(self._joylistener)
		except AttributeError:
			pass
		self.xbox_controller.add_listener(self._xbox_controller_listener)

	def _joylistener(self, sensor, state_id, datum):
		pass
			

	def _xbox_controller_listener(self, sensor, state_id, datum):
		if state_id == 'a_button':
			if datum:
				self.swerve_module.zero(.25)

		if state_id == 'b_button':
			if datum:
				self.swerve_module.zero(.4)

		if state_id == 'start_button':
			if datum:
				if self.strafe_power == 1:
					#print("switching strafe to slow")
					self.strafe_power = .4
				elif self.strafe_power == .4:
					#print("swithing strafe to fast")
					self.strafe_power = 1

		if state_id == 'back_button':
			if datum:
				if self.ackerman_power == .7:
					#print("switching ackerman to fast")
					self.ackerman_power = 1
				elif self.ackerman_power == 1:
					#print("switching ackerman to slow")
					self.ackerman_power = .7

		#RIGHT JOYSTICK FOR STRAFING

		if state_id in ('r_y_axis', 'r_x_axis'):
			
			x = self.xbox_controller.r_x_axis
			y = self.xbox_controller.r_y_axis

			if abs(x) > .2 or abs(y) > .2:

				self.swerve_module.set_strafing(True)
				#print("SWITCHED TO STRAFING")

				angle = math.atan2(x,-y)
				power = math.sqrt(x ** 2 + y ** 2)

				self.swerve_module.strafe(angle, power, self.strafe_power)

			else:
				self.swerve_module.set_power(0)
				self.swerve_module.set_strafing(False)
				#print("SWITCHED TO ACKERMAN")

		if state_id in ('l_y_axis', 'l_x_axis'):

			x = self.xbox_controller.l_x_axis
			y = self.xbox_controller.l_y_axis

			if (abs(x) > .2 or abs(y) > .2) and not self.swerve_module.get_strafing():

				joy_angle = math.atan2(x, -y)

				#DETERMINE POWER: size of vector based on joystick x and y

				power = (math.sqrt(x**2 + y**2))/(math.sqrt(2))
				
				self.swerve_module.ackerman_turn(joy_angle, power, self.ackerman_power)

			else:
				self.swerve_module.set_power(0)
				







