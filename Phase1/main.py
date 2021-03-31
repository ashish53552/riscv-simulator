from collections import OrderedDict
from five_stage_execution import *
from instruction_encoding import *
from execute_instruction import *
from memory_file import *
from register_file import *

#instructions_machine_code array will have all the .mc file instructions
input_file = open("./test/input.mc","r")

PC = None, IR = None

# Storing each instruction in the text memory
for line in input_file:
    instr = line.split()[1]
    add_text_to_memory(instr)

# To mark the end of the instructions
add_text_to_memory(str(hex(0)))

# Fetching the instruction from the text memory, decoding it and performing the respective tasks
while True:
    PC, IR = fetch(PC, IR)
    if IR == str(hex(0)):
        break
        
    instruction_dict = decode(IR)
    instruction = identify_instruction_and_run(instruction_dict)





