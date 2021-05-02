from pipeline_stage_functions import *
import memory_file, register_file

# The Buffers to hold on to values in between pipeline stages
# {'fetch_decode' : None, 'decode_execute' : None, 'execute_memory' : None, 'memory_writeback' : None}

buffers, pcs_in_order = {}, []
num_instructions, num_data_transfer, num_alu, num_control = 0, 0, 0, 0
num_stalls, num_data_hazards, num_control_hazards, num_branch_mispredictions = 0, 0, 0, 0
num_stalls_data, num_stalls_control = 0, 0
fetch = True
lst_hazard = ""

# Function to enable data forwarding
# Modes can either be 'M_M', 'M_E', 'E_E', 'M_D', 'E_D'
# from_ins & to_ins range from 0 to 4 (both included) (with from_ins < to_ins)
def data_forward(mode, from_ins, to_ins, to_reg) :

	if mode == 'M_E' :
		buffers[pcs_in_order[to_ins]]['decode_execute'][to_reg] = buffers[pcs_in_order[from_ins]]['memory_writeback']['value']
	elif mode == 'E_E' :
		buffers[pcs_in_order[to_ins]]['decode_execute'][to_reg] = buffers[pcs_in_order[from_ins]]['execute_memory']['value']


# return type is (hazard_present, in_instruction_no, forwarding_from_instr_1, forwarding_from_instr_2, the value to be forwarded)
def check_data_hazard(PC):
	# global buffers
	if pcs_in_order[0] == PC:
		return False, -1, -1, -1, -1
	elif pcs_in_order[1] == PC:
		if buffers[pcs_in_order[1]]['decode_execute']['rs1'] != '00000' and buffers[pcs_in_order[1]]['decode_execute']['rs1'] and buffers[pcs_in_order[0]]['decode_execute']['rd'] == buffers[pcs_in_order[1]]['decode_execute']['rs1']:
			return True, 1, 0, -1, 'rs1'
		elif buffers[pcs_in_order[1]]['decode_execute']['rs2'] != '00000' and buffers[pcs_in_order[1]]['decode_execute']['rs2'] and buffers[pcs_in_order[0]]['decode_execute']['rd'] == buffers[pcs_in_order[1]]['decode_execute']['rs2']:
			return True, 1, 0, -1, 'rs2'
	else:
		i = 0
		for i in range(1, len(pcs_in_order)):
			if pcs_in_order[i] == PC:
				break
		if buffers[pcs_in_order[i]]['decode_execute']['rs1'] == None and buffers[pcs_in_order[i]]['decode_execute']['rs2'] == None:
			return False, -1, -1, -1, -1
		elif buffers[pcs_in_order[i]]['decode_execute']['rs1'] == '00000' and buffers[pcs_in_order[i]]['decode_execute']['rs2'] == '00000':
			return False, -1, -1, -1, -1
		elif buffers[pcs_in_order[i - 1]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs1'] and buffers[pcs_in_order[i - 2]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs2']:
			return True, i, i - 1, i - 2, 'rs1rs2'
		elif buffers[pcs_in_order[i - 2]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs1'] and buffers[pcs_in_order[i - 1]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs2']:
			return True, i, i - 1, i - 2, 'rs2rs1'
		elif buffers[pcs_in_order[i]]['decode_execute']['rs1'] != '00000' and buffers[pcs_in_order[i]]['decode_execute']['rs1'] and buffers[pcs_in_order[i-1]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs1']:
			return True, i, i-1, -1, 'rs1'
		elif buffers[pcs_in_order[i]]['decode_execute']['rs2'] != '00000' and buffers[pcs_in_order[i]]['decode_execute']['rs2'] and buffers[pcs_in_order[i-1]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs2']:
			return True, i, i-1, -1, 'rs2'
		elif buffers[pcs_in_order[i]]['decode_execute']['rs1'] != '00000' and buffers[pcs_in_order[i]]['decode_execute']['rs1'] and buffers[pcs_in_order[i-2]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs1']:
			return True, i, i-2, -1, 'rs1'
		elif buffers[pcs_in_order[i]]['decode_execute']['rs2'] != '00000' and buffers[pcs_in_order[i]]['decode_execute']['rs2'] and buffers[pcs_in_order[i-2]]['decode_execute']['rd'] == buffers[pcs_in_order[i]]['decode_execute']['rs2']:
			return True, i, i-2, -1, 'rs2'
	return False, -1, -1, -1, -1


def input_for_execute(PC, control_signals):
	if control_signals['mux_alu'] == 'register_&_register' and control_signals['is_control_instruction'] == False:
		return (PC, buffers[PC]['decode_execute']['rs1_val'], buffers[PC]['decode_execute']['rs2_val'], None, 32, 32, control_signals['alu_op'], control_signals)
	
	elif control_signals['mux_alu'] == 'register_&_immediate' and control_signals['is_control_instruction'] == False:
		return (PC, buffers[PC]['decode_execute']['rs1_val'], buffers[PC]['decode_execute']['imm'],None, 32, 12, control_signals['alu_op'], control_signals)

	elif control_signals['mux_alu'] == 'register_&_register_&_immediate':
		return (PC, buffers[PC]['decode_execute']['rs1_val'], buffers[PC]['decode_execute']['imm'],None, 32, 12, control_signals['alu_op'], control_signals)
		
	elif control_signals['mux_alu'] == 'pc_&_imm':
		return (PC, PC, buffers[PC]['decode_execute']['imm'],None, 32, 32, control_signals['alu_op'], control_signals)
		
	elif control_signals['mux_alu'] == 'only_imm':
		return (PC, buffers[PC]['decode_execute']['imm'], hex(12), None, 20, 12, control_signals['alu_op'], control_signals)

	elif control_signals['is_control_instruction'] == True:
		if control_signals['mux_writeback'] == 'PC':
			return (PC, PC, buffers[PC]['decode_execute']['imm'], None, 32, 20, control_signals['alu_op'], control_signals)
		else:
			return (PC, buffers[PC]['decode_execute']['rs1_val'], buffers[PC]['decode_execute']['rs2_val'], buffers[PC]['decode_execute']['imm'], 32, 12, control_signals['alu_op'], control_signals)



def input_for_memory(PC, control_signals):
	if control_signals['mux_memory'] == 'MAR_&_MDR':
		return (PC, buffers[PC]['execute_memory']['value'], buffers[PC]['decode_execute']['rs2_val'], control_signals['memory_size'], control_signals)

	elif control_signals['mux_memory'] == 'MAR':
		return (PC, buffers[PC]['execute_memory']['value'], None, control_signals['memory_size'], control_signals)

	return (PC, None, None, None, control_signals)

# info_per_stage is in format
# [('f' , (pc, prev_branch, branch_inst))
# ('d' , instruction, pc)
# ('e' , (pc, value1, value2, total_bits1, total_bits2, op, control_signals))
# ('m' , (pc, MAR, MDR, num_bytes, control_signals))
# ('w' , (pc, register_num, value, control_signals))
# All these will be stored in a list (of size 5), with each index representing an instruction & each new list representing a new cycle

def execute_pipeline(info_per_stage, forwarding=True, req_PC = None) :

	global buffers
	global pcs_in_order
	global num_instructions
	global num_data_transfer
	global num_alu
	global num_control
	global num_stalls_data
	global num_stalls_control
	global num_stalls
	global num_data_hazards
	global num_control_hazards
	global num_branch_mispredictions
	global fetch
	global lst_hazard
	info_nxt_stage = []
	stall = False
	flush = False

	inst_details = {}
	cycle_details = {}

	_PC, branch_inst, dest_PC = None, False, None

	for i in range(len(info_per_stage)):
		
		if info_per_stage[i][0] == 'f':
			_PC, IR, branch_inst, dest_PC = pipeline_fetch(info_per_stage[i][1])
			if memory_file.read_data_from_memory(_PC, 4, 'instruction_cache') == '0x00000000':
				fetch = False
				continue
			pcs_in_order.append(_PC)
			buffers[_PC] = {'fetch_decode' : IR, 'decode_execute' : None, 'execute_memory' : None, 'memory_writeback' : None}
			if _PC == req_PC:
				inst_details[_PC+"_fetch_decode"] = buffers[_PC]['fetch_decode']
			cycle_details[_PC+"_fetch_decode"] = buffers[_PC]['fetch_decode']
			info_nxt_stage.append(('d', (IR, _PC)))



		elif info_per_stage[i][0] == 'd' :
			PC, control_signals, instruction_dict = pipeline_decode(info_per_stage[i][1])

			rs1_val, rs2_val = None, None
			if instruction_dict['rs1']:
				rs1_val = register_file.get_register_val("x" + str(int(instruction_dict['rs1'], 2)))
			if instruction_dict['rs2']:
				rs2_val = register_file.get_register_val("x" + str(int(instruction_dict['rs2'], 2)))
			buffers[PC]['decode_execute'] = {'rs1': instruction_dict['rs1'], 'rs2': instruction_dict['rs2'],
											 'rd': instruction_dict['rd'], 'rs1_val': rs1_val, 'rs2_val': rs2_val,
											 'imm': instruction_dict['imm'], 'type': control_signals['mux_memory']}

			if PC == req_PC:
				inst_details[PC+"_decode_execute"] = {'opc_code': instruction_dict['opc_code'],'funct3': instruction_dict['funct3'],'funct7': instruction_dict['funct7'],
														 'rs1': instruction_dict['rs1'], 'rs2': instruction_dict['rs2'], 'rd': instruction_dict['rd'],
														 'imm': instruction_dict['imm']}
			cycle_details[PC+"_decode_execute"] = {'opc_code': instruction_dict['opc_code'],'funct3': instruction_dict['funct3'],'funct7': instruction_dict['funct7'],
														 'rs1': instruction_dict['rs1'], 'rs2': instruction_dict['rs2'], 'rd': instruction_dict['rd'],
														 'imm': instruction_dict['imm'] }

			ch, to_inst, from_inst1, from_inst2, to_reg = check_data_hazard(PC)
			if ch and control_signals['is_control_instruction'] and lst_hazard != pcs_in_order[from_inst1] + pcs_in_order[to_inst]:
				lst_hazard = pcs_in_order[from_inst1] + pcs_in_order[to_inst]
				num_control_hazards+=1
			elif ch and lst_hazard != pcs_in_order[from_inst1] + pcs_in_order[to_inst]:
				lst_hazard = pcs_in_order[from_inst1] + pcs_in_order[to_inst]
				num_data_hazards+=1

			# print("Debug: ", PC, to_inst, from_inst1, from_inst2, to_reg)
			if ch == False:
					# print("YES")
					if control_signals['is_control_instruction']:
						new_pc = handle_branches(PC, control_signals, instruction_dict, [rs1_val, rs2_val])
						# print("NEW_PC : ", new_pc)
						lst_pc = info_per_stage[i + 1][1][0]
						if not check_in_bat(PC):
							lst_pc = alu(PC, '0x00000004', 32, 32, 'addition')
						if lst_pc != new_pc:
							flush = True
							info_nxt_stage.append(('e', input_for_execute(PC, control_signals)))
							if fetch:
								info_nxt_stage.append(('f', (new_pc, True)))
							break

			else:
				if forwarding:
					if from_inst1 != -1:
						if buffers[pcs_in_order[from_inst1]]['decode_execute']['type'] == 'MAR' and buffers[pcs_in_order[from_inst1]]['memory_writeback']:
							data_forward('M_E', from_inst1, to_inst, to_reg[:3]+'_val')
						elif buffers[pcs_in_order[from_inst1]]['decode_execute']['type'] != 'MAR' and buffers[pcs_in_order[from_inst1]]['execute_memory']:
							data_forward('E_E', from_inst1, to_inst, to_reg[:3]+'_val')
							# print("BOOM")
						else:
							if not control_signals['is_control_instruction']:
								num_stalls_data+=1
							stall = True

						if len(to_reg) > 3:
							to_reg = to_reg[3:]


					if from_inst2 != -1 and not stall:
						if buffers[pcs_in_order[from_inst2]]['decode_execute']['type'] == 'MAR' and buffers[pcs_in_order[from_inst2]]['memory_writeback']:
							data_forward('M_E', from_inst2, to_inst, to_reg[:3]+'_val')
						elif buffers[pcs_in_order[from_inst2]]['decode_execute']['type'] != 'MAR' and buffers[pcs_in_order[from_inst2]]['execute_memory']:
							data_forward('E_E', from_inst2, to_inst, to_reg[:3]+'_val')
						else:
							if not control_signals['is_control_instruction']:
								num_stalls_data+=1
							stall = True

					
					if control_signals['is_control_instruction'] and not stall:
						new_pc = handle_branches(PC, control_signals, instruction_dict, [buffers[PC]['decode_execute']['rs1_val'], buffers[PC]['decode_execute']['rs2_val']])
						lst_pc = info_per_stage[i + 1][1][0]
						if not check_in_bat(PC):
							lst_pc = alu(PC, '0x00000004', 32, 32, 'addition')
						# print("NEW_PC : ", new_pc)
						if lst_pc != new_pc:
							flush = True
							info_nxt_stage.append(('e', input_for_execute(PC, control_signals)))
							if fetch:
								info_nxt_stage.append(('f', (new_pc, True)))
							break

				else:
					if not control_signals['is_control_instruction']:
						num_stalls_data += 1
					stall = True

			if stall:
				info_nxt_stage.append(('d', info_per_stage[i][1]))
				if fetch:
					if branch_inst and dest_PC:
						info_nxt_stage.append(('f', (dest_PC, branch_inst)))
					else:
						info_nxt_stage.append(('f', (PC, branch_inst)))
				break

			else:
				info_nxt_stage.append(('e', input_for_execute(PC, control_signals)))




		elif info_per_stage[i][0] == 'e':
			PC, value, control_signals = pipeline_execute(info_per_stage[i][1])
			if control_signals['is_control_instruction'] == True and control_signals['mux_writeback'] == 'PC':
				buffers[PC]['execute_memory'] = {'value': value['nxt_pc']}
			else:
				buffers[PC]['execute_memory'] = {'value': value}

			# if not branch_prediction and control_signals['is_control_instruction'] == True:
			# 	if info_per_stage[i+1][1][0] != value['nxt_pc']:
			# 				flush = True
			# 				if pcs_in_order[-1] == info_per_stage[i+1][1][0]:
			# 					pcs_in_order = pcs_in_order[:-1]
			# 				info_nxt_stage.append(('m', input_for_memory(PC, control_signals)))
			# 				if fetch:
			# 					info_nxt_stage.append(('f', (value['nxt_pc'], prev_branch, True)))
			# 				break
			# else:
			if PC == req_PC:
				inst_details[PC+"_execute_memory"] = buffers[PC]['execute_memory']
			cycle_details[PC+"_execute_memory"] = buffers[PC]['execute_memory']
			info_nxt_stage.append(('m', input_for_memory(PC, control_signals)))



		elif info_per_stage[i][0] == 'm':
			PC, value, control_signals = pipeline_memory_access(info_per_stage[i][1])

			if value and control_signals['mux_writeback']:
				buffers[PC]['memory_writeback'] = {'value': value}
			elif control_signals['mux_writeback'] == None:
				buffers[PC]['memory_writeback'] = {'value': None}
			else:
				buffers[PC]['memory_writeback'] = {'value': buffers[PC]['execute_memory']['value']}

			rd = None
			if buffers[PC]['decode_execute']['rd']:
				rd = "x" + str(int(buffers[PC]['decode_execute']['rd'], 2))

			if PC == req_PC:
				inst_details[PC+"_memory_writeback"] = buffers[PC]['memory_writeback']
			cycle_details[PC+"_memory_writeback"] = buffers[PC]['memory_writeback']
			info_nxt_stage.append(('w', (PC, rd, buffers[PC]['memory_writeback']['value'], control_signals)))



		elif info_per_stage[i][0] == 'w':
			PC, control_signals = pipeline_write_back(info_per_stage[i][1])
			num_instructions+=1
			if control_signals['is_control_instruction']:
				num_control += 1
			elif control_signals['mux_writeback'] == 'alu':
				num_alu += 1
			elif control_signals['mux_writeback'] == 'MDR' or control_signals['mux_writeback'] == None:
				num_data_transfer += 1

			pcs_in_order = pcs_in_order[1:]
			# del buffers[PC]
			
	if not stall and not flush and fetch:
		if branch_inst:
			info_nxt_stage.append(('f', (dest_PC, True)))
		else:
			# print("YO")
			info_nxt_stage.append(('f', (_PC, branch_inst)))

	# print("Data Hazards", len(data_hazard), "control_hazard", control_hazard)
	if stall:
		num_stalls+=1
	if flush:
		num_branch_mispredictions+=1

	return info_nxt_stage, cycle_details, inst_details

def print_required_values():
	global pcs_in_order
	global num_instructions
	global num_data_transfer
	global num_alu
	global num_control
	global num_stalls_data
	global num_stalls_control
	global num_stalls
	global num_data_hazards
	global num_control_hazards
	global num_branch_mispredictions
	stats = {}
	num_stalls_control = num_stalls - num_stalls_data
	# print("num_instructions, num_data_transfer, num_alu, num_control : ", num_instructions, num_data_transfer, num_alu, num_control)
	# print("num_stalls, num_data_hazards, num_control_hazards, num_branch_mispredictions : ", num_stalls, num_data_hazards, num_control_hazards, num_branch_mispredictions)
	# print("num_stalls_data, num_stalls_control: ", num_stalls_data, num_stalls_control)

	stats['num_instructions'] = num_instructions
	stats['num_data_transfer'] = num_data_transfer
	stats['num_alu'], stats['num_control'] = num_alu, num_control
	stats['num_stalls'], stats['num_data_hazards'], stats['num_control_hazards'], stats['num_branch_mispredictions'] = num_stalls, num_data_hazards, num_control_hazards, num_branch_mispredictions
	stats['num_stalls_data'],stats['num_stalls_control'] = num_stalls_data, num_stalls_control
	
	return stats

