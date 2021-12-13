"""
File: myopic.py

This file will hold the implementation for a myopic scheduling algorithm. This algorithm will
schedule m-number of tasks across n processors.

Assumptions:
Offline scheduling algorithm so all task information is known apriori
"""

from schedulers.resources.Job import Job
from schedulers.resources.Processor import Processor


class myopic_scheduler:
	"""
	Class: myopic_scheduler

	This class is a multiprocessor scheudler that will add tasks to list of available
	processors when possible.
	"""

	def __init__(
		self, task_list: list, proc_list: list, window: int, w_value: int,
		max_backtracks: int) -> None:
		"""
		Function: __init__

		This function is the constructor for a myopic scheduler

		:param task_list: List of tasks to be scheduled
		:type task_list: list
		:param proc_list: List of processors available to scheudle on
		:type proc_list: list
		:param window: Number of tasks to be considered when scheduling
		:type window: int
		:param w_value: Weigth for the heuristic function
		:type w_value: int
		:param max_backtracks: Maximum number of back tracks allowed before giving up
		:type max_backtracks: int
		"""
		self.task_list = task_list
		self.task_order = list()
		self.proc_list = proc_list
		self.w_value = w_value
		self.window = window
		self.max_backtracks = max_backtracks
		self.done = False
		self.failed = False

		self.create_schedule()

	def get_next_avail_proc(self) -> Processor:
		"""
		Function: get_next_available_proc

		This function gets the next processor which can be scheduled on.

		:return: Next free processor
		:rtype: Processor
		"""
		min_time = min([proc.next_available_time for proc in self.proc_list])
		proc_l = [
			proc for proc in self.proc_list
			if proc.next_available_time == min_time
		]

		return proc_l[0] if len(proc_l) > 0 else None

	def create_schedule(self) -> None:
		"""
		Function: create_schedule

		This function will call a recursive function which will build a scheudle as per the
		myopic scheduler rules
		"""
		self.task_list.sort(key=lambda x: x.deadline)
		self.create_schedule_helper(self.task_list)

	def feasibility_function(self, job: Job) -> bool:
		"""
		Function: feasibility_function

		This function will determine if a give task is feasible or not

		:param job: Job to be considered
		:type job: Job
		:return: True if the job is feasible
		:rtype: bool
		"""
		return max(
			job.arrival_t,
			min(
				[proc.next_available_time for proc in self.proc_list]
			)
		) <= job.deadline

	def heuristic_function(self, job: Job) -> int:
		"""
		Function: heuristic_function

		This function is used for determining which job is the best option to schedule

		:param job: Job which needs to be scheduled
		:type job: Job
		:return: The provided job's heuristic value
		:rtype: int
		"""
		EST = max(job.arrival_t, min([proc.next_available_time for proc in self.proc_list]))
		h = job.deadline + self.w_value * EST
		return h

	def create_schedule_helper(self, jobs: list) -> None:
		"""
		Function: create_schedule_helper

		This function recursively builds out a schedule as per myopic scheduler rules

		:param jobs: List of jobs to be scheduled
		:type jobs: list
		"""
		if self.max_backtracks < 0:
			self.failed = True
			return

		if self.done or not jobs:
			self.done = True
			return

		sub_jobs = jobs[0:self.window]
		feasability = [self.feasibility_function(job) for job in sub_jobs]

		if not feasability and jobs:
			self.max_backtracks -= 1
			return

		heuristics = [
			(
				self.heuristic_function(
					sub_jobs[job]
				),
				job
			) for job in range(len(sub_jobs)) if feasability[job]
		]

		if heuristics:
			heuristics.sort(key=lambda x: x[0])

			for job in heuristics:
				j = jobs.pop(job[1])
				next_avail_proc: Processor = self.get_next_avail_proc()
				assert next_avail_proc is not None

				next_avail_proc.add_job(j)
				self.create_schedule_helper(jobs)

				if self.done:
					return

				jobs.append(j)
				jobs.sort(key=lambda x: x.deadline)
		else:
			self.max_backtracks -= 1
