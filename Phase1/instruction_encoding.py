#This file has the capability to give the extracted bits from a given machine instruction
#The final extracted bits will be read into decimal values as a dictionary given below
#The variable istruction is a string of the 32 bit binary instruction

# ASSUMING INSTRUCTION OF TYPE 0x0 0x11111111
instruction="0x0 0x11111111"
def extract_R_type(instruction) :

	extracted_fields = {"opc_code" : None,
						"imm" : None,
						"funct3" : None,
						"funct7" : None,
						"rs1" : None,
						"rs2" : None,
						"rd" : None}

	# Extracting the main part of the instruction and converting from hex to binary
	bin_instruction = format(int(instruction.split()[1], 16), '0>32b')

	extracted_fields['opc_code'] = bin_instruction[25:]
	extracted_fields['rd'] = bin_instruction[20:25]
	extracted_fields['funct3'] = bin_instruction[17:20]
	extracted_fields['rs1'] = bin_instruction[12:17]
	extracted_fields['rs2'] = bin_instruction[7:12]
	extracted_fields['funct7'] = bin_instruction[:7]

	return extracted_fields ;


def extract_I_type(instruction) :

	#same as r type instruction
	extracted_fields = {"opc_code" : None, "imm" : None, "funct3" : None, "funct7" : None, "rs1" : None, "rs2" : None, "rd" : None}

	bin_instruction = format(int(instruction.split()[1], 16), '0>32b')

	extracted_fields['opc_code'] = bin_instruction[25:]
	extracted_fields['rd'] = bin_instruction[20:25]
	extracted_fields['funct3'] = bin_instruction[17:20]
	extracted_fields['rs1'] = bin_instruction[12:17]
	extracted_fields['imm'] = bin_instruction[:12]

	return extracted_fields 


def extract_S_type(instruction) :

	extracted_fields = {"opc_code" : None,
						"imm" : None,
						"funct3" : None,
						"funct7" : None,
						"rs1" : None,
						"rs2" : None,
						"rd" : None}

	# Extracting the main part of the instruction and converting from hex to binary
	bin_instruction = format(int(instruction.split()[1], 16), '0>32b')

	extracted_fields['opc_code'] = bin_instruction[25:]
	extracted_fields['imm'] = bin_instruction[:7] + bin_instruction[20:25]
	extracted_fields['funct3'] = bin_instruction[17:20]
	extracted_fields['rs1'] = bin_instruction[12:17]
	extracted_fields['rs2'] = bin_instruction[7:12]

	return extracted_fields ;


def extract_SB_type(instruction) :

	extracted_fields = {"opc_code" : None, "imm" : None, "funct3" : None, "funct7" : None, "rs1" : None, "rs2" : None, "rd" : None}

	return extracted_fields ;


def extract_UJ_type(instruction) :

	extracted_fields = {"opc_code" : None, "imm" : None, "funct3" : None, "funct7" : None, "rs1" : None, "rs2" : None, "rd" : None}

	return extracted_fields ;


def extract_U_type(instruction) :

	extracted_fields = {"opc_code" : None,
						"imm" : None,
						"funct3" : None,
						"funct7" : None,
						"rs1" : None,
						"rs2" : None,
						"rd" : None}

	# Extracting the main part of the instruction and converting from hex to binary
	bin_instruction = format(int(instruction.split()[1], 16), '0>32b')

	extracted_fields['opc_code'] = bin_instruction[25:]
	extracted_fields['rd'] = bin_instruction[20:25]
	extracted_fields['imm'] = bin_instruction[:20]

	return extracted_fields ;

#extract_I_type(instruction)