import threading
import time
from collections import OrderedDict
from pyfrc import wpilib
#from grt.sensors.ticker import Ticker

class RecordController:

	def __init__(self, obj_list, time_duration):
		self.obj_list = obj_list
		#self.ticker = Ticker(1)
		self.time_initial = time.time()
		#self.tick_duration = 1
		self.time_duration = time_duration
		self.finished = False
		self.instructions = OrderedDict()
		for i in range(len(self.obj_list)):
			self.instructions["{0}, {1}".format(self.obj_list[i].GetChannel() , type(self.obj_list[i]))] = [self.obj_list[i].Get()]

	def record(self):
		
		#self.ticker.poll()
		self.thread = threading.Thread(target=self.run_record)
		self.thread.start()
		
		#print(self.instructions)
		#print(time.time())

	def run_record(self):
		#self.last_time = time.time()
		while (time.time() - self.time_initial) < self.time_duration:
			#if (time.time() - self.last_time) > self.tick_duration:
			for key in self.instructions:
				i = 0
				self.instructions[key].append(self.obj_list[i].Get())
				i += 1
				#self.last_time = time.time()
			time.sleep(3000)
		self.finished = True

class PlaybackController:

	def __init__(self, instructions, talon_arr_obj):
		self.instructions = instructions
		self.talon_arr_obj = talon_arr_obj
		self.talon_arr = []
		self.solenoid_arr = []
		self.has_started = False
		for key in self.instructions:
			i = int(key.split(',')[0])
			print(i)
			if "Talon" in key:
				self.talon_arr.append(self.instructions[key])
				#print(self.instructions[key])
				print(self.talon_arr)
			if "Solenoid" in key:
				self.solenoid_arr[i] = self.instructions[key]

	def playback(self):
		if not self.has_started:
			self.thread = threading.Thread(target=self.run_playback)
			self.thread.start()
		self.has_started = True

	def run_playback(self):
		for i in range(len(self.talon_arr[0])):
			print(str(range(len(self.talon_arr[0]))))
			for j in range(len(self.talon_arr)):
				self.talon_arr_obj[j].Set(self.talon_arr[j][i])
				print(self.talon_arr[j][i])
				print("J: " + str(j))
				print(i)
			wpilib.Wait(.1)
