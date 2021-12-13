"""
File Job.py

This file will contain the implementation for a Job class. This will act as a mock for a job
which would run on a processor.

Creation Date: 12/12/21
Last Modified: 12/12/21
Version: 1.0
"""


class Job:
	"""
	Class: Job

	This class mocks a task which would run on a processor. It contains all the necessary
	information to describe a job.
	"""

	def __init__(self, name: str, arrive_t: int, wce_t: int, deadline: int) -> None:
		"""
		Function: __init__

		This function is the constructor for the Job class. It will initialize the member
		variables

		:param name: Name of the job
		:type name: str
		:param arrive_t: Time the task arrives at the processor
		:type arrive_t: int
		:param wce_t: Worst case execution time, here also the exact execution time
		:type wce_t: int
		:param deadline: Time at which the task expires
		:type deadline: int
		"""
		self.name = name
		self.arrival_t = arrive_t
		self.wce_t = wce_t
		self.deadline = deadline
