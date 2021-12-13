"""
File: test.py

This file will act as the entry point for our project while testing. More detail to come
as the project is expanded.

Creation Date: 11/27/21
Last Modified: 12/13/21
Version: 1.3
"""

import sys
from schedulers.resources.Job import Job
from schedulers.resources.Processor import Processor
from schedulers.myopic import myopic_scheduler


def main(argv: list) -> None:
	"""
	Function: main

	This function acts as an entry point into our application. It shouldn't be called directly,
	rather it should only be envoked by the if block below

	:param argv: List of commandline arguments
	:type argv: list
	"""

	tasks = [
		# Job("T1", 0, 28, 80),
		# Job("T2", 0, 24, 73),
		# Job("T3", 14, 39, 95),
		# Job("T4", 5, 25, 89),
		# Job("T5", 35, 21, 108)
		Job("T1", 0, 6, 10),
		Job("T2", 2, 7, 13),
		Job("T3", 1, 3, 16),
		Job("T4", 2, 7, 17),
		Job("T5", 3, 9, 19)
	]

	proc_list = [
		Processor("P1"),
		Processor("P2")
	]

	scheduler = myopic_scheduler(tasks, proc_list, 3, 1, 3)

	if scheduler.done:
		for proc in scheduler.proc_list:
			print(proc.get_task_list())

	else:
		print("Failed to find viable schedule")

	if len(argv) == 1:
		return


if __name__ == '__main__':
	main(sys.argv)
