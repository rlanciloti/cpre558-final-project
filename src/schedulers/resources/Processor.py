"""
File: Processor.py

This file contains the class definition for a Processor class. This class will act as a
mock processor which can run one job at a time.

Creation Date: 12/12/2021
Last Modified: 12/12/2021
Version: 1.0
"""

from schedulers.resources.Job import Job


class Processor:
	"""
	Class: Processor

	This class mocks a processor which will run a single job at a time
	"""

	def __init__(self, name: str) -> None:
		"""
		Function: __init__

		This function will initialize the Processor instances member variables.

		:param name: Name of the processor
		:type name: str
		"""
		self.name = name
		self.job_list = list()
		self.next_available_time = 0

	def add_job(self, job: Job) -> None:
		"""
		Function: add_job

		This function will append a given job to the processor's job queue

		:param job: The job to be scheduled
		:type job: Job
		"""

		start_time = (
			self.next_available_time if job.arrival_t < self.next_available_time
			else job.arrival_t
		)

		self.job_list.append((job, start_time))

		self.next_available_time = start_time + job.wce_t

	def pop_job(self) -> Job:
		"""
		Function: pop_job

		This function will remove the most recently added job and return it back to the calling
		function.

		:return: The most recently added job
		:rtype: Job
		"""

		j = self.job_list.pop()
		self.next_available_time -= j.wce_t
		return j

	def get_task_list(self) -> str:
		"""
		Function: get_task_list

		This function will return a string representation of the processor task list

		:return: String representation of the task list
		:rtype: str
		"""

		retval = f"{self.name}: ["

		for t in self.job_list:
			retval += f"({t[1]} | { t[0].name} | {t[0].wce_t + t[1]}), "

		retval = retval[:-2]
		retval += "]"
		return retval
