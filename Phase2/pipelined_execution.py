from pipeline_stage_functions import *
from iag import *

# The Buffers to hold on to values in between pipeline stages
buffers = [{'fetch_decode' : None, 'decode_execute' : None, 'execute_memory' : None, 'memory_writeback' : None} for i in range(5)]

#How to know what registers are left to write back (added in decode stage and removed after write back)
registers_to_be_written_back = []

# Function to enable data forwarding
# Modes can either be 'M_M', 'M_E', 'E_E', 'M_D', 'E_D'
# from_ins & to_ins range from 0 to 4 (both included) (with from_ins < to_ins)
def data_forward(mode, from_ins, to_ins) :

	global buffers
	if mode = 'M_M' :
		buffers[to_ins]['memory_writeback'] = buffers[from_ins]['memory_writeback']
	elif mode = 'M_E' :
		buffers[to_ins]['decode_execute'] = buffers[from_ins]['memory_writeback']
	elif mode = 'E_E' :
		buffers[to_ins]['decode_execute'] = buffers[from_ins]['execute_memory']
	elif mode = 'M_D' :
		buffers[to_ins]['fetch_decode'] = buffers[from_ins]['memory_writeback']
	elif mode = 'E_D' :
		buffers[to_ins]['fetch_decode'] = buffers[from_ins]['execute_memory']


# instruction_set is basically the set of instructions in the pipeline in a particular cycle from top to bottom
# An example for instruction_set looks like ['f','d','e','m','w']
# In case of a stall, the stage (like 'f'/'w') is replaced by None
def check_data_hazard(instruction_set) :

	global buffers

	pass


def flush_pipeline() :

	pass


# info_per_stage is in the format 
# [('f' , (pc, IR, branch))
# ('d' , instruction)
# ('e' , (value1, value2, total_bits1, total_bits2, op))
# ('m' , (MAR, MDR, num_bytes))
# ('w' , (register_num, value)
# 's']   ~'s' indicates a stall
# All these will be stored in a list (of size 5), with each index representing an instruction & each new list representing a new cycle
def execute_pipeline(info_per_stage) :

	global buffers, registers_to_be_written_back

	for i in range(5):
		if info_per_stage[i][0] == 'f' :
			pipeline_fetch(info_per_stage[i][1])

		elif info_per_stage[i][0] == 'd' :
			pipeline_decode(info_per_stage[i][1])

		elif info_per_stage[i][0] == 'e' :
			pipeline_execute(info_per_stage[i][1])

		elif info_per_stage[i][0] == 'm' :
			pipeline_memory_access(info_per_stage[i][1])

		elif info_per_stage[i][0] == 'w' :
			pipeline_write_back(info_per_stage[i][1])

		elif info_per_stage[i][0] == 's' :
			pipeline_stall()




