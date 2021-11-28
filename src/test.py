

import sys
import simsogui

from SimBuilder import SimBuilder

TASK_DIR = 'cpre558-final-project/task_files'
SRC_DIR = 'cpre558-final-project/src'
CONF_DIR = 'cpre558-final-project/graphic_config'


def main(argv) -> None:
	"""
	Function: main

	This function acts as an entry point into our application. It shouldn't be called directly,
	rather it should only be envoked by the if block below

	:param argv: List of commandline arguments
	:type argv: list 
	"""

	if len(argv) == 1:
		return

	sim = SimBuilder(argv[1])
	sim.run_model()

	model = sim.model

	for log in model.logs:
		print(log)


if __name__ == '__main__':
	main(sys.argv)
	simsogui.run_gui()
