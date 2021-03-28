#instructions_machine_code array will have all the .mc file instructions
instructions_machine_code = []

input_file = open("./test/input.mc","r")

for line in input_file:
    instructions_machine_code.append(line)

#total instructions in .mc file
no_of_instructions = len(instructions_machine_code)

#current_instruction dictionary holds values for the instruction currently getting executed
current_instruction = {
    "opcode":"",
    "funct3":"",
    "funct7":"",
    "imm":"",
    "rs1":"",
    "rs2":"",
    "rd":"",
}

##Currently solving assuming only one instruction in .mc file, later adding a for loop would make the program work for .mc file with multiple instructions
for instruction in instructions_machine_code:
    #split into instruction number and actual instruction (see .mc file to understand)
    split_instruction = instruction.split()
  #  print(bin(int(split_instruction[1],16)))
    print(format(int(split_instruction[1],16), '0>32b'))
    #bin_instruction = 



