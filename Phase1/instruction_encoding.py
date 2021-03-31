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

	extracted_fields["opc_code"] = bin_instruction[25:]
	extracted_fields["rs1"] = bin_instruction[12:17]
	extracted_fields["rs2"] = bin_instruction[7:12]
	extracted_fields["funct3"] = bin_instruction[17:20]
	imm1 = bin_instruction[21:25]
	imm2 = bin_instruction[1:7]
	imm3 = bin_instruction[20]
	imm4 = bin_instruction[0]
	imm = imm4 + imm3 + imm2 + imm1
	imm = format(int(imm,2)*2,'0>32b')
	extracted_fields["imm"] = imm
	
	return extracted_fields 


def extract_UJ_type(bin_instruction) :
# remember to muliply by 2 as immediate is omitted
	extracted_fields={
		"opc_code":None,
		"imm" : None,
		"funct3" : None,
		"funct7" : None,
		"rs1" : None,
		"rs2" : None,
		"rd" : None,
	}
	extracted_fields["opc_code"] = bin_instruction[25:]
	extracted_fields["rd"] = bin_instruction[20:25]
	imm19_12 = bin_instruction[12:20][::-1]
	imm11 = bin_instruction[11:12]
	imm10_1 = bin_instruction[1:11][::-1]
	imm_20 = bin_instruction[0:1]
	imm = imm10_1+imm11+imm19_12+imm_20
	imm = format(int(imm,2)*2,'0>32b')
	extracted_fields["imm"] = imm
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



#print(extract_UJ_type())
