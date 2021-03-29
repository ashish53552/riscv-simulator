import memory_file
import iag_file
import instruction_encoding

# Five Stage Execution Procedure for Running an Instruction

# Here in Fetch, the PC and IR are Hexadecimal Strings of the Program Counter and Instruction Respectively
def fetch(PC, IR) :

	if PC is None :
		PC = str(hex(0)) 
	else :
		iag_output_dict = iag_file.iag(PC, None, None, 1, 0)
		PC = iag_output_dict["PC"]

	IR = memory_file.memory[PC]

	return (PC, IR)


# In Decode, the Instruction is a Hexadecimal String
def decode(instruction) :

	bin_instruction = format(int(split_instruction[1],16), '0>32b')
	op_code = bun_instruction[25:]

	if(op_code == '0110011'):
		return instruction_encoding.extract_R_type(instruction)

	elif(op_code == '0010011' or op_code == '0000011' or op_code == '1100111') :
		return instruction_encoding.extract_I_type(instruction)

	elif(op_code == '0100011') :
		return instruction_encoding.extract_S_type(instruction)

	elif(op_code == '1100011') :
		return instruction_encoding.extract_SB_type(instruction)

	elif(op_code == '1101111') :
		return instruction_encoding.extract_UJ_type(instruction)

	elif(op_code == '0010111' or op_code == '0110111') :
		return instruction_encoding.extract_U_type(instruction)

	else :
		print("Invalid Instruction")
		return None


def excute(value1, value2, op) :

	pass 


def memory_access(MAR, MDR) :

	pass


def write_back(register_num,value) :

	pass