from grt.core import GRTMacro
from grt.mechanism import *
import time

class AppleMacro(GRTMacro):
	def __init__(self, apple, timeout=None):
		super().__init__(timeout=timeout)
		self.apple = apple
		self.enabled = False

	def perform(self):
		if self.enabled:
			self.apple.close_curtains()
			time.sleep(0.5)
			self.apple.rotate()
			time.sleep(.5)
			self.apple.open_curtains()
			time.sleep(5)

class BigGhostMacro(GRTMacro):
	def __init__(self, big_ghost, timeout=None):
		super().__init__(timeout=timeout)
		self.big_ghost = big_ghost
		self.enabled = False

	def perform(self):
		if self.enabled:
			self.big_ghost.extend()
			time.sleep(3)
			self.big_ghost.retract()
			time.sleep(4)

class CookieMacro(GRTMacro):
	def __init__(self, cookie, timeout=None):
		super().__init__(timeout=timeout)
		self.cookie = cookie
		self.enabled = False

	def perform(self):
		if self.enabled:
			self.cookie.hand_down()
			time.sleep(1)
			self.cookie.hand_up()
			time.sleep(3)

class GiraffeMacro(GRTMacro):
	def __init__(self, giraffe, timeout=None):
		super().__init__(timeout=timeout)
		self.giraffe = giraffe
		self.enabled = False

	def perform(self):
		if self.enabled:
			self.giraffe.head_down()
			time.sleep(3)
			self.giraffe.head_up()
			time.sleep(5)

class SpiderMacro(GRTMacro):
	def __init__(self, spider, timeout=None):
		super().__init__(timeout=timeout)
		self.spider = spider
		self.enabled = False

	def perform(self):
		if self.enabled:
			self.spider.lower()
			time.sleep(3)
			self.spider.raise_()
			time.sleep(5)
			
class HandMacro(GRTMacro):
	def __init__(self, hand, timeout=None):
		super().__init__(timeout=timeout)
		self.hand = hand
		self.enabled = False
		
	def perform(self):
		if self.enabled:
			self.hand.back()
			time.sleep(0.5)
			self.hand.out()
			time.sleep(0.5)
			self.hand.back()
			time.sleep(0.5)
			self.hand.out()
			time.sleep(5)

