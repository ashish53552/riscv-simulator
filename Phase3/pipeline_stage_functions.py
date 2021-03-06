from auxilliary_functions import *
from branch_address_table import *
import instruction_encoding
import memory_file, register_file


# Possible Control Signals in control_signals in the function pipeline_decode :
# 'mux_alu' : 'register_&_register', 'register_&_immediate', 'pc_&_imm', 'only_imm', None
# (None when execute stage is to be skipped for branch prediction) & 'only_imm' for auipc
# 'alu_op' : op in alu to use
# 'mux_memory' : 'MAR', 'MAR_&_MDR', None
# 'memory_size' : (number of bytes)
# 'mux_writeback' : 'alu', 'MDR', 'PC' None
# 'is_control-instruction' : True/False
# 'control_instruction' : {'flush' : True/False, 'new_pc' : None}
# 'flush' : True and False


def handle_branches(PC, control_signals, instruction_dict, values):

    if check_in_bat(PC) == False:
        if control_signals['mux_writeback']=='PC' and control_signals['mux_alu'] == 'register_&_immediate':
            add_to_bat(PC, alu(values[0], instruction_dict['imm'], 32, 20, 'addition'))
        else:
            imm_bits = 12
            if control_signals['mux_writeback']=='PC':
                imm_bits = 20

            if predict_taken_or_not(instruction_dict['imm']) == 'taken':
                add_to_bat(PC, alu(PC, instruction_dict['imm'], 32, imm_bits, 'addition'))
            else:
                add_to_bat(PC, alu(PC, '0x00000004', 32, 32, 'addition'))

    if control_signals['mux_alu'] == 'register_&_register' :
        value1 = values[0]
        value2 = values[1]
        new_pc = None
        output = alu(value1, value2, 32, 32, control_signals['alu_op'])

        if output == True :
            return alu(PC, instruction_dict['imm'], 32, 12, 'addition')
        else:
            return alu(PC, "0x00000004", 32, 32, 'addition')

    else:
        prev_val = PC
        if control_signals['mux_alu'] == 'register_&_immediate':
            prev_val = values[0]
        return alu(prev_val, instruction_dict['imm'], 32, 20, 'addition')
	


def pipeline_fetch(info):

    PC, branch_inst = info
    branch_instruction = False
    dest_pc_branch = None

    if branch_inst == True:
        pass
    elif PC is None:
        PC = "0x00000000"
    else:
        PC = alu(PC, '0x00000004', 32, 32, 'addition')

    if check_in_bat(PC) == True:
        dest_pc_branch = get_bat(PC)
        branch_instruction = True

    # IR = memory_file.get_data_from_memory(PC, 4)
    IR = memory_file.read_data_from_memory(PC, 4, 'instruction_cache')
    return (PC, IR, branch_instruction, dest_pc_branch)


def pipeline_decode(info) :

    instruction, PC = info

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

    control_signals = {}
    shift_amount = hex(12)
    # R format
    if opc_code == '0110011': # add
        if funct3 == '000' and funct7 == '0000000':
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'addition'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '111' and funct7 == '0000000': # and
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'and_bitwise'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '110' and funct7 == '0000000': # or
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'or_bitwise'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '001' and funct7 == '0000000': # sll
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'shift_left_logical'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '010' and funct7 == '0000000': #slt
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'set_if_less_than'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '101' and funct7 == '0100000': #sra
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'shift_right_arithmetic'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '101' and funct7 == '0000000': # srl
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'shift_right_logical'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '000' and funct7 == '0100000': # sub
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'subtract'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '100' and funct7 == '0000000': # xor
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'xor_bitwise'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '000' and funct7 == '0000001': # mul
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'multiply'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '100' and funct7 == '0000001': # div
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'divide'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '110' and funct7 == '0000001': # rem
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'remainder'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

    # I format
    elif opc_code == '0010011':
        if funct3 == '000': # addi
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_immediate'
            control_signals['alu_op'] = 'addition'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '111': # andi
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_immediate'
            control_signals['alu_op'] = 'and_bitwise'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '110': # ori
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_immediate'
            control_signals['alu_op'] = 'or_bitwise'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'alu'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

    # I format
    elif opc_code == '0000011':
        if funct3 == '000': # lb
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_immediate'
            control_signals['alu_op'] = 'addition'
            control_signals['mux_memory'] = 'MAR'
            control_signals['memory_size'] = 1
            control_signals['mux_writeback'] = 'MDR'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '001': # lh
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_immediate'
            control_signals['alu_op'] = 'addition'
            control_signals['mux_memory'] = 'MAR'
            control_signals['memory_size'] = 2
            control_signals['mux_writeback'] = 'MDR'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '010': # lw
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_immediate'
            control_signals['alu_op'] = 'addition'
            control_signals['mux_memory'] = 'MAR'
            control_signals['memory_size'] = 4
            control_signals['mux_writeback'] = 'MDR'
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

    # I format
    elif opc_code == '1100111':
        if funct3 == '000': # jalr
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_immediate'
            control_signals['alu_op'] = 'addition'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = 'PC'
            control_signals['is_control_instruction'] = True
            return PC, control_signals, instruction_dict

    # S format
    elif opc_code == '0100011':
        if funct3 == '000': # sb
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_register_&_immediate'
            control_signals['alu_op'] = 'addition'
            control_signals['mux_memory'] = 'MAR_&_MDR'
            control_signals['memory_size'] = 1
            control_signals['mux_writeback'] = None
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '010': # sw
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_register_&_immediate'
            control_signals['alu_op'] = 'addition'
            control_signals['mux_memory'] = 'MAR_&_MDR'
            control_signals['memory_size'] = 4
            control_signals['mux_writeback'] = None
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

        elif funct3 == '001': # sh
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_register_&_immediate'
            control_signals['alu_op'] = 'addition'
            control_signals['mux_memory'] = 'MAR_&_MDR'
            control_signals['memory_size'] = 2
            control_signals['mux_writeback'] = None
            control_signals['is_control_instruction'] = False
            return PC, control_signals, instruction_dict

    # SB format
    elif opc_code == '1100011':
        if funct3 == '000': # beq
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'check_if_equal'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = None
            control_signals['is_control_instruction'] = True
            return PC, control_signals, instruction_dict

        elif funct3 == '001': # bne
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'check_if_not_equal'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = None
            control_signals['is_control_instruction'] = True
            return PC, control_signals, instruction_dict

        elif funct3 == '100': # blt
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'check_if_less_than'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = None
            control_signals['is_control_instruction'] = True
            return PC, control_signals, instruction_dict

        elif funct3 == '101': # bge
            val_imm = hex(int(instruction_dict['imm'], 2))
            instruction_dict['imm'] = val_imm
            control_signals['mux_alu'] = 'register_&_register'
            control_signals['alu_op'] = 'check_if_greater_than_equal_to'
            control_signals['mux_memory'] = None
            control_signals['mux_writeback'] = None
            control_signals['is_control_instruction'] = True
            return PC, control_signals, instruction_dict

    # U format
    elif opc_code == '0010111': # auipc
        val_imm = hex(int(instruction_dict['imm'], 2))
        val_imm = alu(val_imm, shift_amount, 20, 12, 'shift_left_logical')
        instruction_dict['imm'] = val_imm
        control_signals['mux_alu'] = 'pc_&_imm'
        control_signals['alu_op'] = 'addition'
        control_signals['mux_memory'] = None
        control_signals['mux_writeback'] = 'alu'
        control_signals['is_control_instruction'] = False
        return PC, control_signals, instruction_dict

    # U format
    elif opc_code == '0110111': # lui
        val_imm = hex(int(instruction_dict['imm'], 2))
        instruction_dict['imm'] = val_imm
        control_signals['mux_alu'] = 'only_imm'
        control_signals['alu_op'] = 'shift_left_logical'
        control_signals['mux_memory'] = None
        control_signals['mux_writeback'] = 'alu'
        control_signals['is_control_instruction'] = False
        return PC, control_signals, instruction_dict

    # UJ format
    elif opc_code == '1101111': # jal
        val_imm = hex(int(instruction_dict['imm'], 2))
        instruction_dict['imm'] = val_imm
        control_signals['mux_alu'] = None
        control_signals['alu_op'] = 'addition'
        control_signals['mux_memory'] = None
        control_signals['mux_writeback'] = 'PC'
        control_signals['is_control_instruction'] = True
        return PC, control_signals, instruction_dict



def pipeline_execute(info) :

	PC, value1, value2, imm, total_bits1, total_bits2, op, control_signals = info
	
	if control_signals['is_control_instruction'] == True and control_signals['mux_writeback'] != 'PC':
		decision = alu(value1, value2, total_bits1, total_bits1, op)
		if decision:
			branch_pc = alu(PC, imm, total_bits1, total_bits2, 'addition')
		else:
			branch_pc = alu(PC, '0x00000004', total_bits1, total_bits1, 'addition')
		return PC, branch_pc, control_signals
        
	elif control_signals['is_control_instruction'] == True and control_signals['mux_writeback'] == 'PC':
		return PC, {'nxt_pc': alu(value1, '0x00000004', total_bits1, total_bits1, op), 'branch_pc': alu(value1, value2, total_bits1, total_bits2, op)}, control_signals

	return PC, alu(value1, value2, total_bits1, total_bits2, op), control_signals


def pipeline_memory_access(info) :

    PC, MAR, MDR, num_bytes, control_signals = info

    if control_signals['is_control_instruction'] == True:
        return PC, None, control_signals

    if MAR != None and MDR != None:
        # print("MAR", MAR, "MDR", MDR)
        MAR = pad_hexa(make_hex_uppercase(MAR), 8)
        MDR = pad_hexa(make_hex_uppercase(MDR), 8)
        memory_file.write_data_to_memory(MDR, MAR, num_bytes, 'data_cache')
        # memory_file.add_data_to_memory(MDR, MAR, num_bytes)
        # print("YES")
        return PC, None, control_signals

    elif MAR != None and MDR == None:
        pad_hexa(make_hex_uppercase(MAR), 8)
        # MDR = memory_file.get_data_from_memory(MAR, num_bytes)
        MDR = memory_file.read_data_from_memory(MAR, num_bytes, 'data_cache')
        return PC, MDR, control_signals

    return PC, None, control_signals


def pipeline_write_back(info) :
    PC, register_num, value, control_signals = info

    # if control_signals['is_control_instruction'] == True and control_signals['mux_writeback'] == 'PC':
    # 	register_file.update_register_val(register_num, value['nxt_pc'])
    # print("WB", register_num, value)
    if value:
        register_file.update_register_val(register_num, value)

    return PC, control_signals
