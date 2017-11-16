from ctre import CANTalon
import math
import time

class Swerve():
	def __init__(self, drive1, drive2, drive3, drive4, rotate1, rotate2, rotate3, rotate4):
		self.drive1 = drive1
		self.drive2 = drive2
		self.drive3 = drive3
		self.drive4 = drive4
		self.rotate1 = rotate1
		self.rotate2 = rotate2
		self.rotate3 = rotate3
		self.rotate4 = rotate4

		self.strafing = False

		self.HEIGHT = 24
		self.WIDTH = 16

        #MAX ANGLE FOR OUTSIDE WHEEL
		self.theta_1 = math.atan2(self.HEIGHT, self.WIDTH)

        #MAX ANGLE FOR INSIDE WHEEL
		self.theta_2 = math.pi - self.theta_1

		self.TICKS_PER_REV = 4096*72/22 #I THINK SO! old:4096*50/24

	def strafe(self, joy_angle, power, scale_down):

		joy_angle = -joy_angle

		turn_motors = (self.rotate1, self.rotate2, self.rotate3, self.rotate4)
		power_motors = (self.drive1, self.drive2, self.drive3, self.drive4)

        #Loops through each of the 4 motors.
		for i in range(4):


            #Convert encoder position to a real-world angle by doing dimensional analysis
            #and modular arithmetic (mod 2pi).

			real = (turn_motors[i].getEncPosition() * ((2*math.pi)/self.TICKS_PER_REV)) % (2*math.pi) 


            #Set each power motor to the scaled down speed.
			power_motors[i].set(power*scale_down)

            #You are currently past the angle you want to go to. 

			if real > joy_angle:


                #If the difference is greater than pi, you will end up going to the joy angle plus 2pi.
                #2pi - real is distance to 0, and then you add the joy angle to get to where you want to go.
                #Dimensional analysis at the end.
				if (real-joy_angle) > math.pi:

					adjustment_factor = ((2*math.pi - real) + joy_angle) * self.TICKS_PER_REV/(2*math.pi)

					position = turn_motors[i].getEncPosition() + adjustment_factor
                    
					turn_motors[i].set(position)

                #Goes from real to joy angle. The difference is made negative so that you can say + adjustment
                #factor instead of - to keep it consistent.
				else:
                    
					adjustment_factor = (- (real - joy_angle)) * self.TICKS_PER_REV/(2*math.pi)

					position = turn_motors[i].getEncPosition() + adjustment_factor
                    
					turn_motors[i].set(position)

            #Your angle (real) is smaller than the angle you want to go to.

			else:

                #If the difference is greater than pi, you end up going to the joy angle minus 2pi.
                #This is very similar to the case above where the difference is greater than 2pi,
                #but it is backwards.

				if (joy_angle-real) > math.pi:
                    
					adjustment_factor = (- real - (2*math.pi - joy_angle)) * self.TICKS_PER_REV/(2*math.pi)

					position = turn_motors[i].getEncPosition() + adjustment_factor
                    
					turn_motors[i].set(position)

                #This is the simplest case. Adjustment factor is difference between joy angle and real,
                #and you add the adjustment factor to your current position.

				else:
                    
					adjustment_factor = (joy_angle - real) * self.TICKS_PER_REV/(2*math.pi)

					position = turn_motors[i].getEncPosition() + adjustment_factor
                    
					turn_motors[i].set(position)

	def set_strafing(self, boolean):
		self.strafing = boolean

	def get_strafing(self):
		return self.strafing

	def set_power(self, power):
		self.drive1.set(power)
		self.drive2.set(power)
		self.drive3.set(power)
		self.drive4.set(power)



