from collections import OrderedDict
from auxilliary_functions import *

#memory is a dictionary with key=location in hex-string and value=data in hex-string
memory = OrderedDict()

text_pointer = "0x00000000"
data_pointer = "0x10000000"
stack_pointer = "0x7FFFFFF0"

cache_size = None, cache_block_size = None, blocks_per_set = None, block_placement_type = None

#instruction_cache = {}
#data_cache = {}

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
    if location in memory.keys():
        value = ""
        for i in reversed(range(no_of_byte)):
            value = memory[location] + value
            location = "0x" + format((int(location, 16) + 1), "0>8x").upper()

        value = "0x"+format(value, "0>8")
        return value
    # print("Error")
    return "0x00000000"



def get_text_memory_file():
    #print("Text Memory\n")
    Inst_Mem = OrderedDict()
    for mem, val in memory.items():
        if int(mem,16) < int("0x10000000",16):
            #print(mem, ":", val)
            Inst_Mem[mem] = val
        else:
            break
    #print('\n')
    return Inst_Mem

def get_data_memory_file():
    #print("Data Memory\n")
    data_p = "0x10000000"
    Data_Mem = OrderedDict()
    Stack_Mem = OrderedDict()
    while data_p in memory.keys():
        #print(data_p, ":",memory[data_p])
        Data_Mem[data_p] = memory[data_p]
        data_p = "0x" + format((int(data_p, 16) + 1), "0>8x").upper()

    #print("\nStack Memory\n")
    st_p = "0x" + format((int("0x7FFFFFF0", 16) - 4), "0>8x").upper()
    while st_p in memory.keys():
        #print(st_p, ":", memory[st_p])
        Stack_Mem[st_p] = memory[st_p]
        st_p = "0x" + format((int(st_p, 16) - 1), "0>8x").upper()
        
    return Data_Mem, Stack_Mem



# Functions to make the instruction and data caches
# Both cache_size and cache_block_size are specified in bytes

def make_instruction_cache(cache_size, cache_block_size, blocks_per_set, block_placement_type) :

    instruction_cache = []          # 1D (for direct mapped) & 2D (for set & fully associative) list storing the data
    instruction_tag_array = []      # 1D (for direct mapped) & 2D (for set & fully associative) list storing the tags of each block
    block_validity = []             # 1D (for direct mapped) & 2D (for set & fully associative) list indicating whether that block has stored any data or not
    block_status = []               # 1D (for direct mapped) & 2D (for set & fully associative) list storing status (as per LRU policy)of each block in a set

    if block_placement_type = 'set_associative' or  block_placement_type = 'fully_associative':
        if block_placement_type = 'fully_associative' :
            blocks_per_set = cache_size//cache_block_size
        for i in range(cache_size/(cache_block_size*blocks_per_set)) :
            instruction_cache.append([])
            instruction_tag_array.append([])
            block_validity.append([])
            block_status.append([])
            status_initializer = 0
            for j in range(blocks_per_set) :
                instruction_cache[i].append('00'*cache_block_size)
                instruction_tag_array[i].append('0x' + '0'*8)
                block_validity[i].append('invalid')
                block_status[i].append(status_initializer)
                status_initializer += 1

    elif block_placement_type = 'direct_mapped' :
        for i in range(cache_size/cache_block_size) :
            instruction_cache.append('00'*cache_block_size)
            instruction_tag_array.append('0x' + '0'*8)
            block_validity[i].append('invalid')

    return instruction_cache, instruction_tag_array, block_validity, block_status



def make_data_cache(cache_size, cache_block_size, blocks_per_set, block_placement_type) :

    data_cache = []                 # 1D (for direct mapped) & 2D (for set & fully associative) list storing the data
    data_tag_array = []             # 1D (for direct mapped) & 2D (for set & fully associative) list storing the tags of each block
    block_validity = []             # 1D (for direct mapped) & 2D (for set & fully associative) list indicating whether that block has stored any data or not
    block_status = []               # 1D (for direct mapped) & 2D (for set & fully associative) list storing status (as per LRU policy)of each block in a set

    if block_placement_type = 'set_associative' or  block_placement_type = 'fully_associative':
        if block_placement_type = 'fully_associative' :
            blocks_per_set = cache_size//cache_block_size
        for i in range(cache_size/(cache_block_size*blocks_per_set)) :
            data_cache.append([])
            data_tag_array.append([])
            block_validity.append([])
            block_status.append([])
            status_initializer = 0
            for j in range(blocks_per_set) :
                data_cache[i].append('00'*cache_block_size)
                data_tag_array[i].append('0x' + '0'*8)
                block_validity[i].append('invalid')
                block_status[i].append(status_initializer)
                status_initializer += 1

    elif block_placement_type = 'direct_mapped' :
        for i in range(cache_size/cache_block_size) :
            data_cache.append('00'*cache_block_size)
            data_tag_array.append('0x' + '0'*8)
            block_validity[i].append('invalid')

    return data_cache, data_tag_array, block_validity, block_status


instruction_cache = {}
data = make_instruction_cache(cache_size, cache_block_size, blocks_per_set, block_placement_type)
instruction_cache['cache'] = data[0]
instruction_cache['tag_array'] = data[1]
instruction_cache['block_status'] = data[2]
instruction_cache['block_validity'] = data[3]


data_cache = {}
data = make_instruction_cache(cache_size, cache_block_size, blocks_per_set, block_placement_type)
data_cache['cache'] = data[0]
data_cache['tag_array'] = data[1]
data_cache['block_status'] = data[2]
data_cache['block_validity'] = data[3]



def get_tag_index_offest(read_address,cache_block_size,num_blocks,blocks_per_set,block_placement_type) :

    block_size_bits = cache_block_size*8
    address_int = int(read_address,16)
    tag = bounding_hex(block_size_bits*(address_int//block_size_bits))
    if block_placement_type = 'direct_mapped' :
        index = None
    else :
        index = (address_int//block_size_bits)%(num_blocks//blocks_per_set)
    offset = (int(read_address,16)-int(tag,16))//8                          # Offest is read in the number of bytes
    return tag, index, offset


def read_block_from_memory(tag_address,cache_block_size) :

    block_of_data = get_data_from_memory(tag_address,cache_block_size)
    return block_of_data


# Reads from the caches following LRU Policy

def read_from_instruction_cache(read_address, index, offest, num_bytes, cache_size, cache_block_size, blocks_per_set, block_placement_type)

    final_data = None

    if block_placement_type = 'set_associative' or block_placament_type = 'fully_associative' :

        if block_placement_type = 'fully_associative' :
            blocks_per_set = cache_size//cache_block_size
            index = 0

        match_found = False
        way_number = 0

        for i in range(blocks_per_set) :
            if instruction_cache['tag_array'][index][i] == read_address and instruction_cache['block_validity'][index][i] != 'invalid' :
                match_found = True
                way_number = i
                break

        if match_found == True :
            final_data = '0x' + instruction_cache['cache'][index][way_number][offest:offset+num_bytes*2]
            initial_status = instruction_cache['block_status'][index][way_number]
            for i in range(blocks_per_set) :
                if instruction_cache['block_status'][index][i] > initial_status :
                    instruction_cache['block_status'][index][i] -= 1
            instruction_cache['block_status'][index][way_number] = blocks_per_set - 1
            return final_data
        else :
            final_data = get_data_from_memory(bounding_hex(int(read_address,16)+offest), num_bytes)
            block_of_data = read_block_from_memory(read_address,cache_block_size)
            for i in range(blocks_per_set) :
                if instruction_cache['block_status'][index][i] == 0 :
                    instruction_cache['block_validity'][index][i] = 'valid'
                    instruction_cache['tag_array'][index][i] = read_address
                    instruction_cache['cache'][index][i] = block_of_data
                    way_number = i
                    break
            for i in range(blocks_per_set) :
                if i == way_number :
                    continue
                instruction_cache['block_status'][index][i] -= 1
            instruction_cache['block_status'][index][way_number] = block_index - 1
            return final_data

    else :

        num_blocks = cache_size//cache_block_size
        match_found = False

        if instruction_cache['tag_array'][index] == read_address and instruction_cache['block_validity'][index] != 'invalid' :
            match_found = True
            break

        if match_found == True :
            final_data = '0x' + instruction_cache['cache'][index][offest:offset+num_bytes*2]
            return final_data
        else :
            final_data = get_data_from_memory(bounding_hex(int(read_address,16)+offest), num_bytes)
            block_of_data = read_block_from_memory(read_address,cache_block_size)
            instruction_cache['tag_array'][index] = read_address
            instruction_cache['cache'][index] = block_of_data
            instruction_cache['block_validity'][index] = 'valid'
            return final_data





def read_from_data_cache(read_address, index, offest, num_bytes, cache_size, cache_block_size, blocks_per_set, block_placement_type)

    final_data = None

    if block_placement_type = 'set_associative' or block_placament_type = 'fully_associative' :

        if block_placement_type = 'fully_associative' :
            blocks_per_set = cache_size//cache_block_size
            index = 0

        match_found = False
        way_number = 0

        for i in range(blocks_per_set) :
            if data_cache['tag_array'][index][i] == read_address and data_cache['block_validity'][index][i] != 'invalid' :
                match_found = True
                way_number = i
                break

        if match_found == True :
            final_data = '0x' + data_cache['cache'][index][way_number][offest:offset+num_bytes*2]
            initial_status = data_cache['block_status'][index][way_number]
            for i in range(blocks_per_set) :
                if data_cache['block_status'][index][i] > initial_status :
                    data_cache['block_status'][index][i] -= 1
            data_cache['block_status'][index][way_number] = blocks_per_set - 1
            return final_data
        else :
            final_data = get_data_from_memory(bounding_hex(int(read_address,16)+offest), num_bytes)
            block_of_data = read_block_from_memory(read_address,cache_block_size)
            for i in range(blocks_per_set) :
                if data_cache['block_status'][index][i] == 0 :
                    data_cache['block_validity'][index][i] = 'valid'
                    data_cache['tag_array'][index][i] = read_address
                    data_cache['cache'][index][i] = block_of_data
                    way_number = i
                    break
            for i in range(blocks_per_set) :
                if i == way_number :
                    continue
                data_cache['block_status'][index][i] -= 1
            data_cache['block_status'][index][way_number] = block_index - 1
            return final_data

    else :

        num_blocks = cache_size//cache_block_size
        match_found = False

        if data_cache['tag_array'][index] == read_address and data_cache['block_validity'][index] != 'invalid' :
            match_found = True
            break

        if match_found == True :
            final_data = '0x' + data_cache['cache'][index][offest:offset+num_bytes*2]
            return final_data
        else :
            final_data = get_data_from_memory(bounding_hex(int(read_address,16)+offest), num_bytes)
            block_of_data = read_block_from_memory(read_address,cache_block_size)
            data_cache['tag_array'][index] = read_address
            data_cache['cache'][index] = block_of_data
            data_cache['block_validity'][index] = 'valid'
            return final_data



def write_to_instruction_cache(read_address, index, offest, num_bytes, new_data, cache_size, cache_block_size, blocks_per_set, block_placement_type) :

    if block_placement_type = 'set_associative' or block_placament_type = 'fully_associative' :

        if block_placement_type = 'fully_associative' :
            blocks_per_set = cache_size//cache_block_size
            index = 0

        match_found = False
        way_number = 0

        for i in range(blocks_per_set) :
            if instruction_cache['tag_array'][index][i] == read_address and instruction_cache['block_validity'][index][i] != 'invalid' :
                match_found = True
                way_number = i
                break

        if match_found == True :
            initial_status = instruction_cache['block_status'][index][way_number]
            for i in range(blocks_per_set) :
                if instruction_cache['block_status'][index][i] > initial_status :
                    instruction_cache['block_status'][index][i] -= 1
            instruction_cache['block_status'][index][way_number] = blocks_per_set - 1
            instruction_cache['cache'][index][way_number][offest:offset+num_bytes*2] = new_data[-(num_bytes*2):]
            add_data_to_memory(new_data[-(num_bytes*2):],bounding_hex(int(read_address,16)+offest),num_bytes)
        else :
            add_data_to_memory(new_data[-(num_bytes*2):],bounding_hex(int(read_address,16)+offest),num_bytes)
            block_of_data = read_block_from_memory(read_address,cache_block_size)
            for i in range(blocks_per_set) :
                if instruction_cache['block_status'][index][i] == 0 :
                    instruction_cache['block_validity'][index][i] = 'valid'
                    instruction_cache['tag_array'][index][i] = read_address
                    instruction_cache['cache'][index][i] = block_of_data
                    way_number = i
                    break
            for i in range(blocks_per_set) :
                if i == way_number :
                    continue
                instrcution_cache['block_status'][index][i] -= 1
            instruction_cache['block_status'][index][way_number] = block_index - 1

    else :

        num_blocks = cache_size//cache_block_size
        match_found = False

        if instruction_cache['tag_array'][index] == read_address and instruction_cache['block_validity'][index] != 'invalid' :
            match_found = True
            break

        if match_found == True :
            instruction_cache['cache'][index][offest:offset+num_bytes*2] = new_data[-(num_bytes*2):]
            add_data_to_memory(new_data[-(num_bytes*2):],bounding_hex(int(read_address,16)+offest),num_bytes)
        else :
            add_data_to_memory(new_data[-(num_bytes*2):],bounding_hex(int(read_address,16)+offest),num_bytes)
            block_of_data = read_block_from_memory(read_address,cache_block_size)
            instruction_cache['tag_array'][index] = read_address
            instruction_cache['cache'][index] = block_of_data
            inctruction_cache['block_validity'][index] = 'valid'




def write_to_data_cache(read_address, index, offest, num_bytes, new_data, cache_size, cache_block_size, blocks_per_set, block_placement_type) :

    if block_placement_type = 'set_associative' or block_placament_type = 'fully_associative' :

        if block_placement_type = 'fully_associative' :
            blocks_per_set = cache_size//cache_block_size
            index = 0

        match_found = False
        way_number = 0

        for i in range(blocks_per_set) :
            if data_cache['tag_array'][index][i] == read_address and data_cache['block_validity'][index][i] != 'invalid' :
                match_found = True
                way_number = i
                break

        if match_found == True :
            initial_status = data_cache['block_status'][index][way_number]
            for i in range(blocks_per_set) :
                if data_cache['block_status'][index][i] > initial_status :
                    data_cache['block_status'][index][i] -= 1
            data_cache['block_status'][index][way_number] = blocks_per_set - 1
            data_cache['cache'][index][way_number][offest:offset+num_bytes*2] = new_data[-(num_bytes*2):]
            add_data_to_memory(new_data[-(num_bytes*2):],bounding_hex(int(read_address,16)+offest),num_bytes)
        else :
            add_data_to_memory(new_data[-(num_bytes*2):],bounding_hex(int(read_address,16)+offest),num_bytes)
            block_of_data = read_block_from_memory(read_address,cache_block_size)
            for i in range(blocks_per_set) :
                if data_cache['block_status'][index][i] == 0 :
                    data_cache['block_validity'][index][i] = 'valid'
                    data_cache['tag_array'][index][i] = read_address
                    data_cache['cache'][index][i] = block_of_data
                    way_number = i
                    break
            for i in range(blocks_per_set) :
                if i == way_number :
                    continue
                data_cache['block_status'][index][i] -= 1
            data_cache['block_status'][index][way_number] = block_index - 1

    else :

        num_blocks = cache_size//cache_block_size
        match_found = False

        if data_cache['tag_array'][index] == read_address and data_cache['block_validity'][index] != 'invalid' :
            match_found = True
            break

        if match_found == True :
            data_cache['cache'][index][offest:offset+num_bytes*2] = new_data[-(num_bytes*2):]
            add_data_to_memory(new_data[-(num_bytes*2):],bounding_hex(int(read_address,16)+offest),num_bytes)
        else :
            add_data_to_memory(new_data[-(num_bytes*2):],bounding_hex(int(read_address,16)+offest),num_bytes)
            block_of_data = read_block_from_memory(read_address,cache_block_size)
            data_cache['tag_array'][index] = read_address
            data_cache['cache'][index] = block_of_data
            data_cache['block_validity'][index] = 'valid'


def read_data_from_memory(actual_address, num_bytes, cache_type) :

    num_blocks = cache_size//cache_block_size
    tag, index, offest = get_tag_index_offest(actual_address, cache_block_size, num_blocks, blocks_per_set, block_placement_type)
    if cache_type == 'instruction_cache' :
        return read_from_instruction_cache(tag, index, offest, num_bytes, cache_size, cache_block_size, blocks_per_set, block_placement_type)
    else :
        return read_from_data_cache(tag, index, offest, num_bytes, cache_size, cache_block_size, blocks_per_set, block_placement_type)


def write_data_from_memory(new_data, actual_address, num_bytes, cache_type) :

    num_blocks = cache_size//cache_block_size
    tag, index, offest = get_tag_index_offest(actual_address, cache_block_size, num_blocks, blocks_per_set, block_placement_type)
    if cache_type == 'instruction_cache' :
        return write_to_instruction_cache(tag, index, offest, num_bytes, new_data, cache_size, cache_block_size, blocks_per_set, block_placement_type)
    else :
        return write_to_data_cache(tag, index, offest, num_bytes, new_data, cache_size, cache_block_size, blocks_per_set, block_placement_type)







