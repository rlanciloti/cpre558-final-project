"""
File: main.py

This file will act as the entry point for our project. It will take an xml config file as
an argument, as well as a flag to run a graphics pipeline. It will then run the simulation
as specified by the config file.

Creation Date: 11/27/2021
Last Modified: 11/27/2021
Version: 1.0
"""

import simsogui

def main(argv):
	if len(argv) == 1:
		return 
		
	pass

if __name__ == '__main__':
	main()
	simsogui.run_gui()
