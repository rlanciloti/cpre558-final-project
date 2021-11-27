"""
File: SimBuilder.py

This file will hold the class 'SimBuilder' which will construct a simulator from a python
dictionary. This dictionary will be the result of a parsed xml config file.

Creation Date: 11/27/2021
Last Modified: 11/27/2021
Version: 1.0
"""
import xmltodict
from simso.configuration import Configuration
from simso.core import Model

class SimBuilder:
	def __init__(self, conf_file: str):
		with open(conf_file, "r") as f:
			self._conf_dict = xmltodict.parse(f.read())['simulation']

		self._setup_config()
		self._setup_tasks()
		self.config.check_all()

		self.model = Model(self.config)

	def _setup_config(self):
		cd = self._conf_dict
		cd_sched = cd['sched']
		cd_proc = cd['processors']['processor']

		self.config = Configuration()
		self.config.cycles_per_ms = float(cd['@cycles_per_ms'])
		self.config.duration = float(cd['@duration'])
		self.config.etm = cd['@etm']
		self.config.scheduler_info.overhead = int(cd_sched['@overhead'])
		self.config.scheduler_info.overhead_activate = int(cd_sched['@overhead_activate'])
		self.config.scheduler_info.overhead_terminate = int(cd_sched['@overhead_terminate'])
		self.config.scheduler_info.filename = cd_sched.get('@className')
		self.config.scheduler_info.clas = cd_sched['@class']
		
		if isinstance(cd_proc, dict):
			self.config.add_processor(
				name = cd_proc["@name"],
				identifier= int(cd_proc["@id"]),
				cl_overhead = int(cd_proc["@cl_overhead"]),
				cs_overhead = int(cd_proc["@cs_overhead"]),
				speed = float(cd_proc["@speed"])
			)
		elif isinstance(cd_proc, list):
			for proc in cd_proc:
				self.config.add_processor(
					name = proc["@name"],
					identifier = int(proc["@id"]),
					cl_overhead = int(proc["@cl_overhead"]),
					cs_overhead = int(proc["@cs_overhead"]),
					speed = float(proc["@speed"])
				)

	def _setup_tasks(self):
		td = self._conf_dict['tasks']['task']
		
		if isinstance(td, dict):
			self.config.add_task(
				name = td['@name'],
				identifier = int(td['@id']),
				task_type = td['@task_type'],
				abort_on_miss = td['@abort_on_miss'],
				period = float(td["@period"]),
				activation_date = int(td['@activationDate']),
				list_activation_dates = td['@list_activation_dates'],
				deadline = float(td['@deadline']),
				base_cpi =float( td['@base_cpi']),
				mix = float(td['@mix']),
				wcet = float(td['@WCET']),
				acet = int(td['@ACET']),
				preemption_cost = int(td['@preemption_cost']),
				et_stddev = float(td['@et_stddev']) 
			)
		elif isinstance(td, list):
			for task in td:
				self.config.add_task(
					name = task['@name'],
					identifier = int(task['@id']),
					task_type = task['@task_type'],
					abort_on_miss = task['@abort_on_miss'],
					period = float(task["@period"]),
					activation_date = int(task['@activationDate']),
					list_activation_dates = task['@list_activation_dates'],
					deadline = float(task['@deadline']),
					base_cpi =float( task['@base_cpi']),
					mix = float(task['@mix']),
					wcet = float(task['@WCET']),
					acet = int(task['@ACET']),
					preemption_cost = int(task['@preemption_cost']),
					et_stddev = float(task['@et_stddev']) 
				)
	
	def run_model(self):
		self.model.run_model()
			