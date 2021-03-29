# Default Register File

from collections import OrderedDict

registers = OrderedDict()

for i in range(32):
  registers["x"+str(i)] = "0x00000000"

registers["x2"] = "0x7FFFFFF0"
registers["x3"] = "0x10000000"


def get_register_val(register_num):
    return registers[register_num]

def update_register_val(register_num, value):
    registers[register_num] = value
























