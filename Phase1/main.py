from collections import OrderedDict
from five_stage_execution import *
from instruction_encoding import *
from execute_instruction import *
from memory_file import *
from register_file import *
import sys
import json
import re

input_file=sys.argv[1]

data=json.loads(input_file)
code=data['code']
code=code.split("\n") #this will contain the list of instructions

inp=data['inp']
inp=inp.replace("\n","")
inp=inp.replace("\r","")
inp=list(inp.split()) #this file contains the data inputs


PC = None
IR = None
branch = False

# Storing each instruction in the text memory
for line in code:
    # print(str(line).split()[1])
    instr = str(line).split()[1]
    add_text_to_memory(instr)

# # To mark the end of the instructions
# add_text_to_memory("0x00000000")

# # Adding Data to memory (Assuming 4 byte input)
# #print("Enter the number of elements to be added in the Data Memory :")
#num = int(inp[0])

if len(inp) > 0:
    list_of_values = inp
    for x in list_of_values:
        data = bounding_hex(int(x))
        # print(data)
        add_data_before(data)

# # get_data_memory_file()
# # cnt = 0
# # Fetching the instruction from the text memory, decoding it and performing the respective tasks
while True:

    # global PC, IR, branch
    # print(PC)
    # print(get_register_file())
    PC, IR = fetch(PC, IR, branch)
    # print("PC", PC)
    # get_memory_file()
    if IR == "0x00000000":
        break
    instruction_dict = decode(IR)
    # print(instruction_dict)
    PC, branch = identify_instruction_and_run(instruction_dict, PC)
    # get_register_file()
    # get_data_memory_file()
    # if PC == "0x00000118":
    #     input("Continue")
    # cnt += 1
    # print("cnt", cnt)

registers = get_register_file()
Inst_Mem = get_text_memory_file()
Data_Mem, Stack_Mem = get_data_memory_file()

finalResult=OrderedDict()
finalResult['registers']=registers
finalResult['Inst_Mem']=Inst_Mem
finalResult['Data_Mem']=Data_Mem
finalResult['Stack_Mem']=Stack_Mem


print(json.dumps(str(finalResult)))

sys.stdout.flush()
