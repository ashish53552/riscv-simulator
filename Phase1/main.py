from instruction_encoding import *

#instructions_machine_code array will have all the .mc file instructions
instructions_machine_code = []

input_file = open("./test/input.mc","r")

for line in input_file:
    instructions_machine_code.append(line)

#total instructions in .mc file
no_of_instructions = len(instructions_machine_code)


for instruction in instructions_machine_code:

    split_instruction = instruction.split()     #split into instruction number and actual instruction (see .mc file to understand)
    bin_instruction = format(int(split_instruction[1],16), '0>32b')     #bin_instruction is string with instruction in 32bit binary form

    current_instruction_opcode = bin_instruction[0:7] #opcode extracted
    extracted_fields = {}
    if current_instruction_opcode=='0110011':         #R-format
        extracted_fields = extract_R_type(instruction) 

    elif current_instruction_opcode=='0000011':         #I-format
        extracted_fields = extract_I_type(instruction)
    
    elif current_instruction_opcode=='0100011':        #S-format
        extracted_fields = extract_S_type(instruction)
    
    elif current_instruction_opcode=='1101111':        #UJ format
        extracted_fields = extract_UJ_type(instruction)
    
    elif current_instruction_opcode=='1100011':        #SB format
        extracted_fields = extract_SB_type(instruction)

    elif current_instruction_opcode=='0010111':        #U format
        extracted_fields = extract_U_type(instruction)

    else:
        print("INVALID OPCODE\n")





