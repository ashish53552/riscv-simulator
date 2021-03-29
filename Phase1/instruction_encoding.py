# This file has the capability to give the extracted bits from a given machine instruction.
# The final extracted bits will be read as binary strings into a dictionary extracted_fields.

# bin_instruction variable is a 32 bit binary string

def extract_R_type(bin_instruction) :

	extracted_fields={
		"opc_code":None,
		"imm" : None,
		"funct3" : None,
		"funct7" : None,
		"rs1" : None,
		"rs2" : None,
		"rd" : None,
	}

	extracted_fields['opc_code'] = bin_instruction[25:]
	extracted_fields['rd'] = bin_instruction[20:25]
	extracted_fields['funct3'] = bin_instruction[17:20]
	extracted_fields['rs1'] = bin_instruction[12:17]
	extracted_fields['rs2'] = bin_instruction[7:12]
	extracted_fields['funct7'] = bin_instruction[:7]

	return extracted_fields 


def extract_I_type(bin_instruction) :

	extracted_fields={
		"opc_code":None,
		"imm" : None,
		"funct3" : None,
		"funct7" : None,
		"rs1" : None,
		"rs2" : None,
		"rd" : None,
	}

	extracted_fields['opc_code'] = bin_instruction[25:]
	extracted_fields['rd'] = bin_instruction[20:25]
	extracted_fields['funct3'] = bin_instruction[17:20]
	extracted_fields['rs1'] = bin_instruction[12:17]
	extracted_fields['imm'] = bin_instruction[:12]

	return extracted_fields 


def extract_S_type(bin_instruction) :

	extracted_fields={
		"opc_code":None,
		"imm" : None,
		"funct3" : None,
		"funct7" : None,
		"rs1" : None,
		"rs2" : None,
		"rd" : None,
	}

	extracted_fields['opc_code'] = bin_instruction[25:]
	extracted_fields['imm'] = bin_instruction[:7] + bin_instruction[20:25]
	extracted_fields['funct3'] = bin_instruction[17:20]
	extracted_fields['rs1'] = bin_instruction[12:17]
	extracted_fields['rs2'] = bin_instruction[7:12]

	return extracted_fields 


def extract_SB_type(bin_instruction) :

	extracted_fields={
		"opc_code":None,
		"imm" : None,
		"funct3" : None,
		"funct7" : None,
		"rs1" : None,
		"rs2" : None,
		"rd" : None,
	}
	return extracted_fields 


def extract_UJ_type(bin_instruction) :

	extracted_fields={
		"opc_code":None,
		"imm" : None,
		"funct3" : None,
		"funct7" : None,
		"rs1" : None,
		"rs2" : None,
		"rd" : None,
	}
	return extracted_fields 


def extract_U_type(bin_instruction) :

	extracted_fields={
		"opc_code":None,
		"imm" : None,
		"funct3" : None,
		"funct7" : None,
		"rs1" : None,
		"rs2" : None,
		"rd" : None,
	}

	extracted_fields['opc_code'] = bin_instruction[25:]
	extracted_fields['rd'] = bin_instruction[20:25]
	extracted_fields['imm'] = bin_instruction[:20]

	return extracted_fields
