from collections import OrderedDict
import five_stage_execution as fse
from instruction_encoding import *
from execute_instruction import *
from pipeline_stage_functions import *
from pipelined_execution import *
from auxilliary_functions import *
from memory_file import *
from register_file import *
import sys
import json
import re
import os

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
print("Enter 1 for yes 0 for no")
pipelining = int(input('Pipelining? '))
register_after_each_cycle = int(input("Registers File? "))

if pipelining:
    data_forwarding = int(input('Data_Forwarding? '))
    print_pipeline_registers = int(input('Print_Pipeline_Registers? '))
    req_inst = str(input('Print_pipeline_registers_for_inst_with_PC_in_format(0x0000000A)? (Leave Empty if not required)'))

### Input
with open('../test/factorial(of_10_in_x26).mc', 'r') as f:
    lines = f.read()
code = lines.splitlines()

# Storing each instruction in the text memory
for line in code:
    instr = str(line).split()[1]
    add_text_to_memory(instr)

# # Adding Data to memory (Assuming 4 byte input)
inp = input("Enter the number of elements to be added in the Data Memory :")

if len(inp) > 0:
    for x in inp.split():
        data = bounding_hex(int(x))
        add_data_before(data)

# To be returned to front-end as a JSON Object along with memory dictionaries
Stats = {}

if pipelining:
    info_per_stage = [('f', (None, False))]
    total_cycles, CPI = 0, 0
    all_cycle_details = {}
    req_inst_details = {}
    Registers_per_cycle = {}

    while True:
        # print(info_per_stage)
        info_per_stage, cycle_details, inst_details = execute_pipeline(info_per_stage, data_forwarding, req_inst)
        if not info_per_stage:
            break

        total_cycles += 1

        # print(buffers)
        # print("cycle done:", total_cycles, "\n")
        # print(cycle_details)

        if print_pipeline_registers:
            all_cycle_details["Cycle " + str(total_cycles)] = cycle_details
        if inst_details:
            req_inst_details["Cycle " + str(total_cycles)] = inst_details
        if register_after_each_cycle:
            Registers_per_cycle["Cycle " + str(total_cycles)] = get_register_file()

    # if print_pipeline_registers:
    #     print("Instruction Buffers per Cycle\n", all_cycle_details, "\n")
    #
    # # if inst_details:
    # # print("REQ_INST", len(req_inst))
    # print("Required Instruction Buffers\n", req_inst_details, "\n")
    #
    # print("Total Cycles", total_cycles-1)
    Stats = print_required_values()
    Stats['total_cycles'] = total_cycles - 1
    CPI = total_cycles / Stats['num_instructions']
    # print("CPI: ", CPI, "\n")
    Stats["CPI"] = CPI
    Stats['all_cycle_details'] = all_cycle_details
    Stats['req_inst_details'] = req_inst_details
    Stats['register_per_cycle'] = Registers_per_cycle


else:
    PC = None
    IR = None
    branch = False
    cycles = 0
    Registers_per_cycle = {}
    Stats['num_alu'], Stats['num_control'], Stats['num_data_transfer'] = 0, 0, 0

    while True:
        PC, IR = fse.fetch(PC, IR, branch)
        if IR == "0x00000000":
            break
        cycles += 1
        instruction_dict = decode(IR)
        PC, branch, br, data_t = identify_instruction_and_run(instruction_dict, PC)
        if data_t:
            Stats['num_data_transfer'] += 1
        elif br:
            Stats['num_control'] += 1
            # print(PC)
        else:
            Stats['num_alu'] += 1
        if register_after_each_cycle:
            Registers_per_cycle["Cycle " + str(cycles)] = get_register_file()

    Stats['total_cycles'] = 5 * cycles
    Stats['CPI'] = 5
    Stats['num_instructions'] = cycles
    Stats['register_per_cycle'] = Registers_per_cycle

registers = get_register_file()
Inst_Mem = get_text_memory_file()
Data_Mem, Stack_Mem = get_data_memory_file()

os.remove("debug_info.txt")
file_d = open("debug_info.txt", 'a')
for i in Stats.keys():
    if type(Stats[i]) == int or type(Stats[i]) == float:
        print(i, "\n", Stats[i], "\n")
    elif Stats[i]:
        # print(i,"\n")
        file_d.write("\n")
        file_d.write(i+"\n")
        for j in Stats[i]:
            # print(j, "\n", Stats[i][j], "\n")
            file_d.write(j+"\n"+str(Stats[i][j])+"\n")

def print_output(x):
    for i in x:
        print(i, " : ", x[i])
    print("\n")

print("Registers\n")
print_output(registers)
print("Instruction Memory\n")
print_output(Inst_Mem)
print("Data Memory\n")
print_output(Data_Mem)
print("Stack Memory\n")
print_output(Stack_Mem)

# finalResult=OrderedDict()
# finalResult['registers']=registers
# finalResult['Inst_Mem']=Inst_Mem
# finalResult['Data_Mem']=Data_Mem
# finalResult['Stack_Mem']=Stack_Mem


# print(json.dumps(finalResult))
# sys.stdout.flush()
