from collections import OrderedDict

memory = OrderedDict()

text_pointer = "0x00000000"
data_pointer = "0x10000000"
stack_pointer = "0x7FFFFFF0"

def add_text_to_memory(instruction):
    global text_pointer
    memory[text_pointer] = instruction[-2:]
    text_pointer = "0x" + format((int(text_pointer, 16) + 1), "0>8x").upper()  # incrementing the text pointer
    memory[text_pointer] = instruction[-4:-2]
    text_pointer = "0x" + format((int(text_pointer, 16) + 1), "0>8x").upper()  # incrementing the text pointer
    memory[text_pointer] = instruction[-6:-4]
    text_pointer = "0x" + format((int(text_pointer, 16) + 1), "0>8x").upper()  # incrementing the text pointer
    memory[text_pointer] = instruction[-8:-6]
    text_pointer = "0x" + format((int(text_pointer, 16) + 1), "0>8x").upper()  # incrementing the text pointer

def add_data_to_memory(data, no_of_byte):
    global data_pointer
    # For storing Single Byte Data like in sb
    if no_of_byte == 1:
        memory[data_pointer] = data[-2:]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1), "0>8x").upper() #incrementing the data pointer

    # For storing Half Word Data like in sh
    elif no_of_byte == 2:
        memory[data_pointer] = data[-2:]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1), "0>8x").upper()  # incrementing the data pointer
        memory[data_pointer] = data[-4:-2]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1), "0>8x").upper()  # incrementing the data pointer

    # For storing Word Data like in sw
    elif no_of_byte == 4:
        memory[data_pointer] = data[-2:]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1), "0>8x").upper()  # incrementing the data pointer
        memory[data_pointer] = data[-4:-2]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1), "0>8x").upper()  # incrementing the data pointer
        memory[data_pointer] = data[-6:-4]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1), "0>8x").upper()  # incrementing the data pointer
        memory[data_pointer] = data[-8:-6]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1), "0>8x").upper()  # incrementing the data pointer

# Assuming stack will only store word of 32 bits
def add_data_to_stack(data, location, no_of_byte):
    if no_of_byte == 1:
        memory[location] = data[-2:]

    # For storing Half Word Data like in sh
    elif no_of_byte == 2:
        memory[location] = data[-2:]
        location = "0x" + format((int(location, 16) + 1), "0>8x").upper()  # incrementing the location by one for next byte
        memory[location] = data[-4:-2]

    # For storing Word Data like in sw
    elif no_of_byte == 4:
        memory[location] = data[-2:]
        location = "0x" + format((int(location, 16) + 1), "0>8x").upper()  # incrementing the location by one for next byte
        memory[location] = data[-4:-2]
        location = "0x" + format((int(location, 16) + 1), "0>8x").upper()  # incrementing the location by one for next byte
        memory[location] = data[-6:-4]
        location = "0x" + format((int(location, 16) + 1), "0>8x").upper()  # incrementing the location by one for next byte
        memory[location] = data[-8:-6]

# Getting values for a given memory location and the number of bytes, can be used for lw, lh, lb
def get_data_from_memory(location, no_of_byte):
    value = ""
    for i in reversed(range(no_of_byte)):
        value = memory[location]+value
        location = "0x" + format((int(location, 16) + 1), "0>8x").upper()

    value = "0x"+format(value, "0>8")
    return value
