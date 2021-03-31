from five_stage_execution import *
from instruction_encoding import *
from execute_instruction import *

#Function to identify the type of instruction
def identify_instruction_and_run(instruction_dict,PC) :

	opc_code = instruction_dict['opc_code']
	funct3 = instruction_dict['funct3']
	funct7 = instruction_dict['funct7']

	if opc_code == '0110011' :
		if funct3 == '000' and funct7 == '0000000' :
			run_add(instruction_dict)
			return PC



# Functions to directly run the Instruction

# R Type
def run_add(instruction_dict) :

	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'addition')

	write_back(rd,output)



# R Type
def run_and() :
	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'and_bitwise')

	write_back(rd,output)



# R Type
def run_or() :
	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'or_bitwise')

	write_back(rd,output)
 


# R Type
def run_sll() :
	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'shift_left_logical')

	write_back(rd,output) 


# R Type
def run_slt() :
	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'check_if_less than')

	write_back(rd,output)


# R Type
def run_sra() :
	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'shift_right_arithmetic')

	write_back(rd,output)



# R Type
def run_srl() :
	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'shift_right_logical')

	write_back(rd,output)
	


# R Type
def run_sub() :
	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'subtract')

	write_back(rd,output)


# R Type
def run_xor() :
	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'xor_bitwise')

	write_back(rd,output)


# R Type
def run_mul() :
	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'multiply')

	write_back(rd,output)
	pass 


# R Type
def run_div() :
	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'divide')

	write_back(rd,output)


# R Type
def run_rem() :
	rs1 = int(instruction_dict['rs1'],2)
	val_rs1 = hex(get_register_val(rs1))

	rs2 = int(instruction_dict['rs2'],2)
	val_rs2 = hex(get_register_val(rs2))

	rd = int(instruction_dict['rd'],2)

	output = execute(val_rs1, val_rs2, 32, 32, 'remainder')

	write_back(rd,output)


# I Type
def run_addi() :

	pass 


# I Type
def run_andi() :

	pass 


# I Type
def run_ori() :

	pass 


# I Type
def run_lw() :

	pass 


# I Type
def run_lh() :

	pass 


# I Type
def run_lb() :

	pass 


# I Type
def jalr() :

	pass 


# S Type
def run_sw() :

	pass 


# S Type
def run_sh() :

	pass 


# S Type
def run_sb() :

	pass 


# SB Type
def run_beq() :

	pass 


# SB Type
def run_bne() :

	pass 


# SB Type
def run_bge() :

	pass 


# SB Type
def run_blt() :

	pass 


# UJ Type
def run_jal() :

	pass 


# U Type
def run_auipc() :

	pass 


# U Type
def run_lui() :

	pass 









