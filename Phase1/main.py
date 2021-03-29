import five_stage_execution
from collections import OrderedDict

registers = OrderedDict()
for i in range(32):
  registers["x"+str(i)] = "0x00000000"

registers["x2"] = "0x7FFFFFF0"
registers["x3"] = "0x10000000"

#instructions_machine_code array will have all the .mc file instructions
instructions_machine_code = []

input_file = open("./test/input.mc","r")

for line in input_file:
    instructions_machine_code.append(line)

#total instructions in .mc file
no_of_instructions = len(instructions_machine_code)


for instruction in instructions_machine_code:
    
    five_stage_execution.decode(instruction)





