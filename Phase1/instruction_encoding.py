#This file has the capability to give the extracted bits from a given machine instruction
#The final extracted bits will be read into decimal values as a dictionary given below
#The variable istruction is a string of the 32 bit binary instruction


def extract_R_type(instruction) :

	extracted_fields = {"opc_code" : None, "imm" : None, "funct3" : None, "funct7" : None, "rs1" : None, "rs2" : None, "rd" : None}

	return extracted_fields ;


def extract_I_type(instruction) :

	extracted_fields = {"opc_code" : None, "imm" : None, "funct3" : None, "funct7" : None, "rs1" : None, "rs2" : None, "rd" : None}

	return extracted_fields ;


def extract_S_type(instruction) :

	extracted_fields = {"opc_code" : None, "imm" : None, "funct3" : None, "funct7" : None, "rs1" : None, "rs2" : None, "rd" : None}

	return extracted_fields ;


def extract_SB_type(instruction) :

	extracted_fields = {"opc_code" : None, "imm" : None, "funct3" : None, "funct7" : None, "rs1" : None, "rs2" : None, "rd" : None}

	return extracted_fields ;


def extract_UJ_type(instruction) :

	extracted_fields = {"opc_code" : None, "imm" : None, "funct3" : None, "funct7" : None, "rs1" : None, "rs2" : None, "rd" : None}

	return extracted_fields ;


def extract_U_type(instruction) :

	extracted_fields = {"opc_code" : None, "imm" : None, "funct3" : None, "funct7" : None, "rs1" : None, "rs2" : None, "rd" : None}

	return extracted_fields ;