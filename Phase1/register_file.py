# Default Register File

from collections import OrderedDict

#registers is a dictionary with key=register number in string and value=data in hex-string
registers = OrderedDict()

for i in range(32):
  registers["x"+str(i)] = "0x00000000"

registers["x2"] = "0x7FFFFFF0"
registers["x3"] = "0x10000000"


def get_register_val(register_num):
	return registers[register_num]


def update_register_val(register_num, value):

	if register_num != 'x0' :
		registers[register_num] = value
























