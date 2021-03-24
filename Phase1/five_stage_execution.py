import memory_file
import iag_file

# Five Stage Execution Procedure for Running an Instruction

def fetch(PC, IR) :

	if PC is not None :
		PC = PC + 4
	else :
		PC = memory_file.starting_instruction

	IR = memory_file.memory[str(PC)]

	return (PC, IR)


def decode(instruction) :

	pass


def excute(value1, value2, op) :

	pass 


def memory_access(MAR, MDR) :

	pass


def write_back(register_num,value) :

	pass