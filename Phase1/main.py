#instructions_machine_code array will have all the .mc file instructions
instrutions_machine_code = []
input_file = open("./test/input.mc","r")

for line in input_file:
    instrutions_machine_code.append(line)
#currentInstruction dictionary holds values for the instruction currently getting executed
current_instruction = {
    "opcode":"",
    "funct3":"",
    "funct7":"",
    "imm":"",
    "rs1":"",
    "rs2":"",
    "rd":"",
}


