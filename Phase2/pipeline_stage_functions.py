from five_stage_execution import *
from iag import *
from auxilliary_functions import *
import instruction_encoding


# Possible Control Signals in control_signals in the function pipeline_decode :
# 'mux_alu' : 'register_&_register', 'register_&_immediate', 'pc_&_imm' 'only_imm', None
# (None when execute stage is to be skipped for branch prediction) & 'only_imm' for auipc
# 'alu_op' : op in alu to use
# 'mux_memory' : 'MAR', 'MAR_&_MDR', None
# 'memory_size' : (number of bytes)
# 'mux_writeback' : 'alu', 'MDR', 'PC' None



def pipeline_fetch(info) :

	PC, IR, prev_branch = info

	if branch == 0 :
		if PC is None:
	        PC = "0x00000000"
	    else:
	        iag_output_dict = None
	        if branch == False:
	            iag_output_dict = iag(PC, None, None, 1, 0)
	        else:
	            iag_output_dict = iag(PC, None, "0x00000000", 1, 1)
	        PC = iag_output_dict["PC"]

	    IR = memory_file.get_data_from_memory(PC, 4)

	    return (PC, IR)
	else :
		pass


def pipeline_decode(info) :

	instruction = info
	
	split_instruction = instruction.split()
    bin_instruction = format(int(split_instruction[0], 16), '0>32b')
    op_code = bin_instruction[25:]
    instruction_dict = None

    if (op_code == '0110011'):
        instruction_dict = instruction_encoding.extract_R_type(bin_instruction)

    elif (op_code == '0010011' or op_code == '0000011' or op_code == '1100111'):
        instruction_dict = instruction_encoding.extract_I_type(bin_instruction)

    elif (op_code == '0100011'):
        instruction_dict = instruction_encoding.extract_S_type(bin_instruction)

    elif (op_code == '1100011'):
        instruction_dict = instruction_encoding.extract_SB_type(bin_instruction)

    elif (op_code == '1101111'):
        instruction_dict = instruction_encoding.extract_UJ_type(bin_instruction)

    elif (op_code == '0010111' or op_code == '0110111'):
        instruction_dict = instruction_encoding.extract_U_type(bin_instruction)

    else:
        print("Invalid Instruction")
        return None

    opc_code = instruction_dict['opc_code']
    funct3 = instruction_dict['funct3']
    funct7 = instruction_dict['funct7']

    control_signals = {'mux_alu' : None, 'mux_memory' : None, 'memory_size' = 4 'mux_writeback' : None}

    # R format
    if opc_code == '0110011':
        if funct3 == '000' and funct7 == '0000000':
        	control_signals['mux_alu'] = 'register_&_register'
        	control_signals['alu_op'] = 'addition'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

        elif funct3 == '111' and funct7 == '0000000':
            control_signals['mux_alu'] = 'register_&_register'
        	control_signals['alu_op'] = 'and_bitwise'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

        elif funct3 == '110' and funct7 == '0000000':
            Pcontrol_signals['mux_alu'] = 'register_&_register'
        	control_signals['alu_op'] = 'or_bitwise'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

        elif funct3 == '001' and funct7 == '0000000':
            control_signals['mux_alu'] = 'register_&_register'
        	control_signals['alu_op'] = 'shift_left_logical'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

        elif funct3 == '010' and funct7 == '0000000':
            control_signals['mux_alu'] = 'register&_register'
        	control_signals['alu_op'] = 'set_if_less_than'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

        elif funct3 == '101' and funct7 == '0100000':
            control_signals['mux_alu'] = 'register_&_register'
        	control_signals['alu_op'] = 'shift_right_arithmetic'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

        elif funct3 == '101' and funct7 == '0000000':
            control_signals['mux_alu'] = 'register_&_register'
        	control_signals['alu_op'] = 'shift_right_logical'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

        elif funct3 == '000' and funct7 == '0100000':
            control_signals['mux_alu'] = 'register_&_register'
        	control_signals['alu_op'] = 'subtract'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

        elif funct3 == '100' and funct7 == '0000000':
            control_signals['mux_alu'] = 'register_&_register'
        	control_signals['alu_op'] = 'xor_bitwise'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

        elif funct3 == '000' and funct7 == '0000001':
            control_signals['mux_alu'] = 'register_&_register'
        	control_signals['alu_op'] = 'multiply'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

        elif funct3 == '100' and funct7 == '0000001':
            control_signals['mux_alu'] = 'register_&_register'
        	control_signals['alu_op'] = 'divide'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

        elif funct3 == '110' and funct7 == '0000001':
            control_signals['mux_alu'] = 'register&_register'
        	control_signals['alu_op'] = 'remainder'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

    # I format
    elif opc_code == '0010011':
        if funct3 == '000':
            control_signals['mux_alu'] = 'register_&_immediate'
        	control_signals['alu_op'] = 'addition'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

        elif funct3 == '111':
            control_signals['mux_alu'] = 'register_&_immediate'
        	control_signals['alu_op'] = 'and_bitwise'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

        elif funct3 == '110':
            control_signals['mux_alu'] = 'register_&_immediate'
        	control_signals['alu_op'] = 'or_bitwise'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'alu'
            return PC, control_signals, instruction_dict

    # I format
    elif opc_code == '0000011':
        if funct3 == '000':
            control_signals['mux_alu'] = 'register_&_immediate'
        	control_signals['alu_op'] = 'addition'
        	control_signals['mux_memory'] = 'MAR'
        	control_signals['memory_size'] = 1
        	control_signals['mux_writeback'] = 'MDR'
            return PC, control_signals, instruction_dict

        elif funct3 == '001':
            control_signals['mux_alu'] = 'register_&_immediate'
        	control_signals['alu_op'] = 'addition'
        	control_signals['mux_memory'] = 'MAR'
        	control_signals['memory_size'] = 2
        	control_signals['mux_writeback'] = 'MDR'
            return PC, control_signals, instruction_dict

        elif funct3 == '010':
            control_signals['mux_alu'] = 'register_&_immediate'
        	control_signals['alu_op'] = 'addition'
        	control_signals['mux_memory'] = 'MAR'
        	control_signals['mux_writeback'] = 'MDR'
            return PC, control_signals, instruction_dict

    # I format
    elif opc_code == '1100111':
        if funct3 == '000':
            control_signals['mux_alu'] = 'pc_&_immediate'
        	control_signals['alu_op'] = 'addition'
        	control_signals['mux_memory'] = None
        	control_signals['mux_writeback'] = 'PC'
            return PC, control_signals, instruction_dict

    # S format
    elif opc_code == '0100011':
        if funct3 == '000':
            control_signals['mux_alu'] = 'register_&_immediate'
        	control_signals['alu_op'] = 'addition'
        	control_signals['mux_memory'] = 'MAR_&_MDR'
        	control_signals['memory_size'] = 1
        	control_signals['mux_writeback'] = None
            return PC, control_signals, instruction_dict

        elif funct3 == '010':
            control_signals['mux_alu'] = 'register_&_immediate'
        	control_signals['alu_op'] = 'addition'
        	control_signals['mux_memory'] = 'MAR_&_MDR'
        	control_signals['mux_writeback'] = None
            return PC, control_signals, instruction_dict

        elif funct3 == '010':
            control_signals['mux_alu'] = 'register_&_immediate'
        	control_signals['alu_op'] = 'addition'
        	control_signals['mux_memory'] = 'MAR_&_MDR'
        	control_signals['memory_size'] = 2
        	control_signals['mux_writeback'] = None
            return PC, control_signals, instruction_dict

    # SB format
    elif opc_code == '1100011':
        if funct3 == '000':
            PC, branch = run_beq(instruction_dict, PC)
            return PC, branch

        elif funct3 == '001':
            PC, branch = run_bne(instruction_dict, PC)
            return PC, branch

        elif funct3 == '100':
            PC, branch = run_blt(instruction_dict, PC)
            return PC, branch

        elif funct3 == '101':
            PC, branch = run_bge(instruction_dict, PC)
            return PC, branch

    # U format
    elif opc_code == '0010111':
    	val_imm = hex(int(instruction_dict['imm'], 2))
    	val_imm = alu(val_imm, shift_amount, 20, 12, 'shift_left_logical')
    	instruction_dict['imm'] = val_imm
        control_signals['mux_alu'] = 'pc_&_imm'
        control_signals['alu_op'] = 'addition'
        control_signals['mux_memory'] = None
        control_signals['mux_writeback'] = 'alu'
        return PC, control_signals, instruction_dict

    # U format
    elif opc_code == '0110111':
        control_signals['mux_alu'] = 'only_imm'
        control_signals['alu_op'] = 'shift_left_logical'
        control_signals['mux_memory'] = None
        control_signals['mux_writeback'] = 'alu'
        return PC, control_signals, instruction_dict

    # UJ format
    elif opc_code == '1101111':
        control_signals['mux_alu'] = 'pc_&_immediate'
        control_signals['alu_op'] = 'addition'
        control_signals['mux_memory'] = None
        control_signals['mux_writeback'] = 'PC'
        return PC, control_signals, instruction_dict




def pipeline_execute(info) :

	value1, value2, total_bits1, total_bits2, op, branch = info
	
	if branch == 1 :
		return None

	return alu(value1, value2, total_bits1, total_bits2, op)


def pipeline_memory_access(info) :

	MAR, MDR, num_bytes, branch = info

	if branch == 1 :
		return None

	if MAR != None and MDR != None:
        # print("MAR", MAR, "MDR", MDR)
        MAR = pad_hexa(make_hex_uppercase(MAR), 8)
        MDR = pad_hexa(make_hex_uppercase(MDR), 8)
        memory_file.add_data_to_memory(MDR, MAR, num_bytes)
        return None

    elif MAR != None and MDR == None:
        pad_hexa(make_hex_uppercase(MAR), 8)
        MDR = memory_file.get_data_from_memory(MAR, num_bytes)
        return MDR


def pipeline_write_back(info) :

	register_num, value, branch = info
	
	register_file.update_register_val(register_num, value)


def pipeline_stall(info) :

	pass