from five_stage_execution import *
from instruction_encoding import *
from collections import OrderedDict

#instructions_machine_code array will have all the .mc file instructions
instructions_machine_code = []

input_file = open("./test/input.mc","r")

for line in input_file:
    instructions_machine_code.append(line)

#total instructions in .mc file
no_of_instructions = len(instructions_machine_code)


for instruction in instructions_machine_code:
    decode(instruction)





