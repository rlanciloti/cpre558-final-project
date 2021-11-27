"""
File: edf_test.py

This file will hold code pertaining to EDF scheduling on a single core processor. This is
example code for getting familiar with SimSo framework.

Creation Date: 11/27/21
Last Modified: 11/27/21
Version: 1.0
"""

from simso.core import Scheduler

class EDF_mono(Scheduler):
	def init(self):
		self.ready_list = list()

	def on_activate(self, job):
		self.ready_list.append(job)

	def on_terminated(self, job):
		self.ready_list.remove(job)

	def schedule(self, cpu):
		if not self.ready_list: return None

		job = min(self.ready_list, key=lambda x: x.absolute_deadline)

