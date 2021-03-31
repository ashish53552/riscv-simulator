from five_stage_execution import *
from instruction_encoding import *
from execute_instruction import *

#Function to identify the type of instruction
def identify_instruction_and_run(instruction_dict) :

	opc_code = instruction_dict['opc_code']
	funct3 = instruction_dict['funct3']
	funct7 = instruction_dict['funct7']

	if opc_code == '0110011' :
		if funct3 == '000' and funct7 == '0000000' :
			run_add(instruction_dict)
			return



# Functions to directly run the Instruction

# R Type
def run_add() :

	pass 


# R Type
def run_and() :

	pass 


# R Type
def run_or() :

	pass 


# R Type
def run_sll() :

	pass 


# R Type
def run_slt() :

	pass 


# R Type
def run_sra() :

	pass 


# R Type
def run_srl() :

	pass 


# R Type
def run_sub() :

	pass 


# R Type
def run_xor() :

	pass 


# R Type
def run_mul() :

	pass 


# R Type
def run_div() :

	pass 


# R Type
def run_rem() :

	pass 


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