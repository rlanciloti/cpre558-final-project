"""
File: test.py

This file will act as the entry point for our project while testing. More detail to come 
as the project is expanded.

Creation Date: 11/27/21
Last Modified: 11/27/21
Version: 1.1
"""

import sys
import os
import json
import simsogui
from simso.core import Model
from simso.configuration import Configuration

from schedulers.EDF_mono import EDF_mono
from SimBuilder import SimBuilder

TASK_DIR = 'cpre558-final-project/task_files'
SRC_DIR = 'cpre558-final-project/src'
CONF_DIR = 'cpre558-final-project/graphic_config'

def main(argv):
	"""
	Function: main

	This function acts as an entry point into our application. It shouldn't be called directly,
	rather it should only be envoked by the if block below

	:param argv: List of commandline arguments
	:type argv: list
	"""

	if len(argv) == 1:
		return

	#sim = SimBuilder(f"{CONF_DIR}/parsing_test.xml")
	sim = SimBuilder(argv[1])
	sim.run_model()

	model = sim.model

	for log in model.logs:
		print(log)


if __name__ == '__main__':
	main(sys.argv)
	simsogui.run_gui()