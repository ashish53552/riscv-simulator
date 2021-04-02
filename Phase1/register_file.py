# Default Register File

from collections import OrderedDict

#registers is a dictionary with key=register number in string and value=data in hex-string
registers = OrderedDict()

for i in range(32):
  registers["x"+str(i)] = "0x00000000"

registers["x2"] = "0x7FFFFFF0"
registers["x3"] = "0x10000000"


def get_register_val(register_num):
	# register_num = 'x' + str(register_num)
	return registers[register_num]


def update_register_val(register_num, value):

	# register_num = 'x' + str(register_num)
	if register_num != 'x0' :
		registers[register_num] = value

def get_register_file():
	print("REGISTER FILE \n")
	for register, val in registers.items():
		print(register, ":", val)
	print("\n")
























