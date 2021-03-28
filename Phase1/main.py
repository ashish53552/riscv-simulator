#instructions_machine_code array will have all the .mc file instructions
instructions_machine_code = []

input_file = open("./test/input.mc","r")

for line in input_file:
    instructions_machine_code.append(line)

#total instructions in .mc file
no_of_instructions = len(instructions_machine_code)



##Currently solving assuming only one instruction in .mc file, later adding a for loop would make the program work for .mc file with multiple instructions
for instruction in instructions_machine_code:

    split_instruction = instruction.split()     #split into instruction number and actual instruction (see .mc file to understand)
    bin_instruction = format(int(split_instruction[1],16), '0>32b')     #bin_instruction is string with instruction in 32bit binary form

    current_instruction_opcode = bin_instruction[0:7] #opcode extracted

    if current_instruction_opcode=='0110011':
        #R-format
        current_instruction_rd = bin_instruction[7:12]
        current_instruction_funct3 = bin_instruction[12:15]
        current_instruction_rs1 = bin_instruction[15:20]
        current_instruction_rs2 = bin_instruction[20:25]
        current_instruction_funct7 = bin_instruction[25:]

     #current_instruction dictionary holds values for the instruction currently getting executed
        current_instruction = {
            "opcode":current_instruction_opcode,
            "funct3":current_instruction_funct3,
            "funct7":current_instruction_funct7,
            "imm":"",
            "rs1":current_instruction_rs1,
            "rs2":current_instruction_rs2,
            "rd":current_instruction_rd,
        }       

    elif current_instruction_opcode=='0000011': #Note - 0010011 also is I format
        #I-format
        print()
    
    elif current_instruction_opcode=='0100011':
        #S-format
        print()
    
    elif current_instruction_opcode=='1101111':
        #UJ format
        print()
    
    elif current_instruction_opcode=='1100011':
        #SB format
        print()

    else:
        print("INVALID OPCODE\n")

    #current_instruction dictionary will be passed further




