from five_stage_execution import *
from iag import *



def pipeline_fetch(info) :

	PC, IR, branch = info
	pass


def pipeline_decode(info) :

	instruction = info
	pass


def pipeline_execute(info) :

	value1, value2, total_bits1, total_bits2, op = info
	pass


def pipeline_memory_access(info) :

	MAR, MDR, num_bytes = info
	pass


def pipeline_write_back(info) :

	register_num, value = info
	pass


def pipeline_stall(info) :

	pass