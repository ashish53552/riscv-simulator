from pipeline_stage_functions import *
from iag import *

# The Buffers to hold on to values in between pipeline stages
# {'fetch_decode' : None, 'decode_execute' : None, 'execute_memory' : None, 'memory_writeback' : None}
global buffers = {}
global pcs_in_order = []

# Function to enable data forwarding
# Modes can either be 'M_M', 'M_E', 'E_E', 'M_D', 'E_D'
# from_ins & to_ins range from 0 to 4 (both included) (with from_ins < to_ins)
def data_forward(mode, from_ins, to_ins, to_reg) :

	global buffers
	if mode = 'M_M' :
		buffers[pcs_in_order[to_ins]]['memory_writeback'][] = buffers[pcs_in_order[from_ins]]['memory_writeback']
	elif mode = 'M_E' :
		buffers[pcs_in_order[to_ins]]['decode_execute'] = buffers[pcs_in_order[from_ins]]['memory_writeback']
	elif mode = 'E_E' :
		buffers[pcs_in_order[to_ins]]['decode_execute'][to_reg] = buffers[pcs_in_order[from_ins]]['execute_memory']['rd_val']
	elif mode = 'M_D' :
		buffers[pcs_in_order[to_ins]]['fetch_decode'] = buffers[pcs_in_order[from_ins]]['memory_writeback']
	elif mode = 'E_D' :
		buffers[pcs_in_order[to_ins]]['fetch_decode'] = buffers[pcs_in_order[from_ins]]['execute_memory']


# return type is (hazard_present, in_instruction_no, forwarding_from_instr_1, forwarding_from_instr_2, the value to be forwarded)
def check_data_hazard(PC):
	# global buffers
	if pcs_in_order[0] == PC:
		return False, -1, -1, -1, -1
	elif pcs_in_order[1] == PC:
		if buffers[pcs_in_order[0]]['decode_execute']['rd'] == buffers[pcs_in_order[1]]['decode_execute']['rs1']:
			return True, 1, 0, -1, 'rs1'
		elif buffers[pcs_in_order[0]]['decode_execute']['rd'] == buffers[pcs_in_order[1]]['decode_execute']['rs2']:
			return True, 1, 0, -1, 'rs2'
	else:
		for i in range(1, len(pcs_in_order)):
			if pcs_in_order[i] == PC:
				break
		if buffers[pcs_in_order[i-1]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs1']:
			return True, i, i-1, -1, 'rs1'
		elif buffers[pcs_in_order[i-1]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs2']:
			return True, i, i-1, -1, 'rs2'
		elif buffers[pcs_in_order[i-2]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs1'] and buffers[pcs_in_order[i-2]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs2']:
			return True, i, i-1, i-2
		elif buffers[pcs_in_order[i-2]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs1']:
			return True, i, i-2, -1, 'rs1'
		elif buffers[pcs_in_order[i-2]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs2']:
			return i, i-2, -1, 'rs2'
	return False, -1, -1, -1, -1


def flush_pipeline() :

	pass


# info_per_stage is in format
# [('f' , (pc, prev_branch))
# ('d' , instruction, pc)
# ('e' , (pc, value1, value2, total_bits1, total_bits2, op, branch))
# ('m' , (pc, MAR, MDR, num_bytes, branch))
# ('w' , (pc, register_num, value, branch)
# All these will be stored in a list (of size 5), with each index representing an instruction & each new list representing a new cycle
def execute_pipeline(info_per_stage) :

	global buffers, registers_to_be_written_back

	info_nxt_stage = []
	stall = False
	for i in range(len(info_per_stage)):
		if info_per_stage[i][0] == 'f' :
			_PC, IR = pipeline_fetch(info_per_stage[i][1])
			pcs_in_order.append(_PC)
			buffers[PC] = {'fetch_decode' : IR, 'decode_execute' : None, 'execute_memory' : None, 'memory_writeback' : None}
			info_nxt_stage.append(('d', (_PC, IR)))

		elif info_per_stage[i][0] == 'd' :
			PC, control_signal, instruction_dict = pipeline_decode(info_per_stage[i][1])
			ch, to_inst, from_inst1, from_inst2, to_reg = check_data_hazard(PC)

			if ch == False:
				if instruction_dict['rs1']:
					rs1_val = register_file.get_register_val("x" + str(int(instruction_dict['rs1'], 2)))
				if instruction_dict['rs2']:
					rs2_val = register_file.get_register_val("x" + str(int(instruction_dict['rs2'], 2)))
				buffers[PC]['decode_execute'] = {'rs1': instruction_dict['rs1'], 'rs2': instruction_dict['rs2'],'rd': instruction_dict['rd'], 'rs1_val': rs1_val, 'rs2_val': rs2_val, 'imm': instruction_dict['imm']}

				# Update this based on Control Signals
				info_nxt_stage.append(('e', ()))
			else:
				if forwarding:
					if from_inst1 != -1:
						if buffers[pcs_in_order[from_ins1]]['execute_memory']:
							data_forward('M_M', from_ins1, to_ins, to_reg+'_val')
						else:
							stall = True
					if from_inst2 != -1:
						if buffers[pcs_in_order[from_ins2]]['execute_memory']:
							data_forward('M_M', from_ins2, to_ins, to_reg + '_val')
						else:
							stall = True
				else:
					stall = True

				if stall:
					info_nxt_stage.append(('d', info_per_stage[i][1]))
					info_nxt_stage.append(('f', (PC, prev_branch)))
					break


		elif info_per_stage[i][0] == 'e':
			pipeline_execute(info_per_stage[i][1])
			info_nxt_stage.append(('m', ()))

		elif info_per_stage[i][0] == 'm':
			pipeline_memory_access(info_per_stage[i][1])

		elif info_per_stage[i][0] == 'w':
			pipeline_write_back(info_per_stage[i][1])
			pcs_in_order.remove(PC)
			
	if not stall:
		info_nxt_stage.append(('f', (_PC, prev_branch)))

	return info_nxt_stage




