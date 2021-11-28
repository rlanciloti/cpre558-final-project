"""
File: EDF_Mono.py

This file will hold code pertaining to EDF scheduling on a single core processor. This is
example code for getting familiar with SimSo framework.

Creation Date: 11/27/21
Last Modified: 11/27/21
Version: 1.1
"""

from typing import Tuple
from simso.core import Job
from simso.core.Processor import Processor
from simso.core import Scheduler


class EDF_Mono(Scheduler):

	"""
	Class: EDF_mono

	This class is a sub-class of Scheduler which is a part of simso. Using this super class
	allows us to create a custom scheduler. This is an implementation of EDF for a single core
	processor.

	:param Scheduler: Super class
	:type Scheduler: class
	"""

	def init(self) -> None:
		"""
		Function: init

		This function initialized all necessary instance variables
		"""

		self.ready_list = list()

	def on_activate(self, job: Job) -> None:
		"""
		Function: on_activate

		This is an override of a super class function. This function is triggered when a task
		arrives, or is 'activated'.

		:param job: The task which arrived and trigger this function
		:type job: Job
		"""

		self.ready_list.append(job)

	def on_terminated(self, job: Job) -> None:
		"""
		Function: on_terminated

		This is an override of a super class function. This function is triggered when a task
		finishes, or is `terminated`.

		:param job: The task which finished and triggered this function
		:type job: Job
		"""

		self.ready_list.remove(job)

	def schedule(self, cpu: Processor) -> Tuple:
		"""
		Function: schedule

		This is an override of a super class function. This function is triggered when the
		processor needs to run the scheduler. Returns a tuple or a list of tuples and each
		tuple contains a job and a CPU to run the job on.

		:param cpu: Calling CPU, or the CPU which needs the scheuduler
		:type cpu: Processor
		:return: Tuple or list of tuples containing the Job and CPU to run said job
		:rtype: Tuple/List<Tule> (Job, Processor)
		"""

		if not self.ready_list:
			return None

		job = min(self.ready_list, key=lambda x: x.absolute_deadline)
		return (job, cpu)
