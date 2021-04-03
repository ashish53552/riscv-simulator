from collections import OrderedDict

#memory is a dictionary with key=location in hex-string and value=data in hex-string
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

def add_data_before(data, no_of_byte=4):
    global data_pointer
    if no_of_byte == 1:
        memory[data_pointer] = data[-2:]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1), "0>8x").upper()  # incrementing the location by one for next byte

    # For storing Half Word Data like in sh
    elif no_of_byte == 2:
        memory[data_pointer] = data[-2:]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1), "0>8x").upper()  # incrementing the location by one for next byte
        memory[data_pointer] = data[-4:-2]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1),"0>8x").upper()  # incrementing the location by one for next byte

    # For storing Word Data like in sw
    elif no_of_byte == 4:
        memory[data_pointer] = data[-2:]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1), "0>8x").upper()  # incrementing the location by one for next byte
        memory[data_pointer] = data[-4:-2]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1), "0>8x").upper()  # incrementing the location by one for next byte
        memory[data_pointer] = data[-6:-4]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1), "0>8x").upper()  # incrementing the location by one for next byte
        memory[data_pointer] = data[-8:-6]
        data_pointer = "0x" + format((int(data_pointer, 16) + 1), "0>8x").upper()  # incrementing the location by one for next byte

# Adding data of given bit in a given memory location
def add_data_to_memory(data, location, no_of_byte):
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
    # if location in memory.keys():
        value = ""
        for i in reversed(range(no_of_byte)):
            value = memory[location] + value
            location = "0x" + format((int(location, 16) + 1), "0>8x").upper()

        value = "0x"+format(value, "0>8")
        return value
    # return "0x00000000"

def get_text_memory_file():
    print("MEMORY FILE")
    print("Text Memory")
    for mem, val in memory.items():
        if int(mem,16) < int(data_pointer,16):
            print(mem, ":", val)
        else:
            break

def get_data_memory_file():
    print("Data Memory")
    for mem, val in memory.items():
        if int(mem,16) >= int("0x10000000",16):
            print(mem, ":",val)













