import threading
import time
from collections import OrderedDict
try:
	import wpilib
except ImportError:
	from pyfrc import wpilib

class RecordController:

	def __init__(self, obj_list):
		self.obj_list = obj_list #list of objects to record
		self.running = False
		self.instructions = OrderedDict() #dictionary of instructions to save
		"""
		This ridiculous for loop sets up a dictionary containing the objects passed in, and their output values.
		It may be easier to replace it with a 2D list.
		"""
		for i in range(len(self.obj_list)):
			self.instructions["{0}, {1}".format(self.obj_list[i].GetChannel() , type(self.obj_list[i]))] = [self.obj_list[i].Get()]


	def engage(self):
		"""
		Called in a higher level controller.
		Starts recording in a separate thread.
		"""
		self.running = True
		self.thread = threading.Thread(target=self.run_record)
		self.thread.start()

	def disengage(self):
		"""
		Signals recording thread to stop.
		"""
		self.running = False

	def run_record(self):
		"""
		Appends the output values of all the objects passed into __init__
		to the instructions dictionary. Sample rate is currently hard-coded.
		"""
		while self.running:
			i = 0
			for key in self.instructions:
				self.instructions[key].append(self.obj_list[i].Get())
				print(self.obj_list[i].Get())
				i += 1
			wpilib.Wait(.1)

class PlaybackController:

	def __init__(self, instructions, talon_arr_obj, revert_controller):
		self.instructions = instructions #instructions to output
		self.talon_arr_obj = talon_arr_obj #talons to output instructions to
		self.revert_controller = revert_controller #drive controller to revert control to when finished
		self.talon_arr = [] #lists that the dictionary will be parsed into
		self.solenoid_arr = []
		self.running = False
		#parsing the dictionary into talon and solenoid components.
		for key in self.instructions:
			i = int(key.split(',')[0])
			print(i)
			if "Talon" in key:
				self.talon_arr.append(self.instructions[key])
				#print(self.instructions[key])
				print(self.talon_arr)
			if "Solenoid" in key:
				self.solenoid_arr[i] = self.instructions[key]

	def engage(self):
		"""
		Called in a higher level controller.
		Starts playback in a separate thread.
		"""
		self.running = True
		self.thread = threading.Thread(target=self.run_playback)
		self.thread.start()

	def disengage(self):
		"""
		Signals playback thread to stop.
		Also zeros all motor outputs.
		"""
		self.running = False
		for talon in self.talon_arr_obj:
			talon.Set(0)
		self.revert_controller.engage()

	def run_playback(self):
		"""
		Iterates through the provided instruction dictionary.
		Disengages itself when finished.
		"""
		for i in range(len(self.talon_arr[0])):
			print(str(range(len(self.talon_arr[0]))))
			for j in range(len(self.talon_arr)):
				self.talon_arr_obj[j].Set(self.talon_arr[j][i])
				print(self.talon_arr[j][i])
				print("J: " + str(j))
				print(i)
			wpilib.Wait(.1)
			if not self.running:
				break
		self.disengage()
