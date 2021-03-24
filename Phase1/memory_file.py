# This file contains the basic memory implementation variable

memory_addresses = [str(hex(i)) for i in range(4294967295)]
memory_values = [0 for i in range(4294967295)] #Decimal for 0xFFFFFFFF

memory = zip(memory_addresses,memory_values)

text_segment = memory[:268435456]
data_segment = memory[268435456:]
heap_segment = memory[268468200:]
