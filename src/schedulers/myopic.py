"""
File: myopic.py

This file will hold the implementation for a myopic scheduling algorithm. This algorithm will
schedule m-number of tasks across n processors.

Assumptions:
Offline scheduling algorithm so all task information is known apriori
"""

from simso.core import Job
from simso.core.Processor import Processor
from simso.core import Scheduler
from typing import Tuple

NUM_PROCS = 2

class myopic_scheduler (Scheduler):

	def __init__(self, task_list: list, window: int, w_value: int, max_backtracks: int) -> None:
		self.task_list = task_list
		self.task_order = list()
		self.proc_list = [list() for x in range(NUM_PROCS)]
		self.w_value = w_value
		self.window = window
		self.max_backtracks = max_backtracks
		self.done = False
		self.failed = False
		self.proc_avail_list = [[0] for x in self.proc_list]

	def init(self) -> None:
		pass

	def on_activate(self, job: Job) -> None:
		pass

	def on_terminated(self, job: Job) -> None:
		pass 

	def schedule(self, cpu: Processor) -> Tuple:
		pass
	
	def create_schedule(self):
		self.task_list.sort(key=lambda x: x.absolute_deadline)
		self.create_schedule_helper(self.task_list)
		
	def feasibility_function(self, job: Job) -> bool:
		return max(job.start_date, min([x[-1] for x in self.proc_avail_list])) <= job.absolute_deadline
		
	def heuristic_function(self, job: Job, w_value: int) -> int:
		EST = max(job.start_date, min([x[-1] for x in self.proc_avail_list]))
		h = job.absolute_deadline + w_value * EST
		return h

	def create_schedule_helper(self, jobs: list(Job)):
		if self.max_backtracks < 0:
			self.failed = True
			return

		if self.done or not jobs:
			self.done = True
			return

		sub_jobs = jobs[0:self.window]
		feasability = [self.feasability_function(job) for job in sub_jobs]

		if not feasability and jobs:
			self.max_backtracks -= 1
			return

		heuristics = [
			(self.heuristic_function(
				sub_jobs[job],
				self.w_value
			), job) for job in range(sub_jobs) if feasability[job]
		]

		if heuristics:
			heuristics.sort(key=lambda x: x[0])
			next_avail_proc = min([proc for proc in self.proc_avail_list], key=lambda x: x[-1])

			for job in heuristics:
				j = jobs.pop(job)
				self.create_schedule_helper(jobs)

				if self.done:
					return

				jobs.append(j)
				jobs.sort(key=lambda x: x.absolute_deadline)
		else:
			self.max_backtracks -= 1
			return jobs
