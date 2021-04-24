from collections import OrderedDict
from pipeline_stage_functions import *
from pipelined_execution import *
from auxilliary_functions import *
from memory_file import *
from register_file import *
import sys
import json
import re

# input_file=sys.argv[1]
#
# data=json.loads(input_file)
# code=data['code']
# code=code.split("\n") #this will contain the list of instructions

# inp=data['inp']
# inp=inp.replace("\n","")
# inp=inp.replace("\r","")
# inp=list(inp.split()) #this file contains the data inputs

### Input to be taken for knobs


# pipelining = int(Input('Pipelining? '))
# data_forwarding = int(Input('Data_Forwarding? '))
# print_pipeline_registers = int(Input('Print_Pipeline_Registers? '))
# print_pipeline_registers_inst_num = int(Input('print_pipeline_registers_inst_num? '))
#
# if pipelining == 0 :
#     data_forwarding = 0
#     print_pipeline_registers = 0
#     print_pipeline_regisrers_inst_num = 0
# else :
#     if data_forwarding == 0 :
#         print_pipeline_registers = 0
#         print_pipeline_regisrers_inst_num = 0
#     else :
#         if print_pipeline_registers == 1 :
#             print_pipeline_regisrers_inst_num = 0



### Performance Measures

total_cycles, CPI = 0, 0

###
with open('../test/merge(4_inputs).mc', 'r') as f:
  lines = f.read()
code = lines.splitlines()

# PC = None
# IR = None
# branch = False
info_per_stage = [('f' , (None, False))]

# Storing each instruction in the text memory
for line in code:
    # print(str(line).split()[1])
    instr = str(line).split()[1]
    add_text_to_memory(instr)

# # To mark the end of the instructions
# add_text_to_memory("0x00000000")

# # Adding Data to memory (Assuming 4 byte input)
inp = input("Enter the number of elements to be added in the Data Memory :")
#num = int(inp[0])

if len(inp) > 0:
    # list_of_values = inp
    for x in inp.split():
        data = bounding_hex(int(x))
        # print(data)
        add_data_before(data)

# # get_data_memory_file()
# # cnt = 0
# # Fetching the instruction from the text memory, decoding it and performing the respective tasks
while True:
    print(info_per_stage)
    info_per_stage = execute_pipeline(info_per_stage)
    total_cycles+=1
    print(buffers)
    print("cycle done:", total_cycles, "\n")

    if not info_per_stage:
        break
    
tot_inst = print_required_values()
CPI = total_cycles / tot_inst
print("CPI: ", CPI)

registers = get_register_file()
Inst_Mem = get_text_memory_file()
Data_Mem, Stack_Mem = get_data_memory_file()

print(registers)
print(Inst_Mem)
print(Data_Mem)
print(Stack_Mem)

# finalResult=OrderedDict()
# finalResult['registers']=registers
# finalResult['Inst_Mem']=Inst_Mem
# finalResult['Data_Mem']=Data_Mem
# finalResult['Stack_Mem']=Stack_Mem


# print(json.dumps(finalResult))
#
# sys.stdout.flush()
