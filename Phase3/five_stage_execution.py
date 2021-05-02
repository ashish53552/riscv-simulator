import memory_file
import register_file
from iag_file import *
import instruction_encoding


# Auxillary Functions for Dealing with 2's Complement for Negative Numbers

# Returning a hexadecimal in uppercase format
def make_hex_uppercase(hex_num):
    return '0x' + (hex_num.upper())[2:]


# Padding a hexadecimal to its total_bits where hex_num is a hexadecimal_string with '0x' in the beginning
def pad_hexa(hex_num, total_half_bytes):
    return '0x' + hex_num[2:].zfill(total_half_bytes)


# For Instructions like I : total_bits = 12, & for UJ : total_bits = 20
def twos_complement(val, total_bits):
    val = val - (1 << total_bits)
    return val


# Both value1 and value2 are Hexadecimal Strings, converted to signed decimal integers
def get_neg_values(value1, value2, total_bits1, total_bits2):
    value1 = pad_hexa(value1, int(total_bits1 / 4))
    value2 = pad_hexa(value2, int(total_bits2 / 4))
    # print("Ans", value1, value2)

    bin_value1 = format(int(value1, 16), '0>' + str(total_bits1)+ 'b')
    if (bin_value1[0] == '1'):
        value1 = twos_complement(int(value1, 16), total_bits1)
    else:
        value1 = int(value1, 16)

    bin_value2 = format(int(value2, 16), '0>' + str(total_bits2)+ 'b')
    if (bin_value2[0] == '1'):
        value2 = twos_complement(int(value2, 16), total_bits2)
    else:
        value2 = int(value2, 16)

    return value1, value2


# Taking an integer value, and converting it to a hexadecimal string with a bound on the number of bits
# If the number of bits is exceeding a certain range, then extra MSB side bits (from carry) are taken out
def bounding_hex(num, total_bits=32):
    formatting_string = '0>' + str(total_bits) + 'b'

    if num > 2 ** (total_bits - 1) - 1:
        num = int('0' + bin(num)[-(total_bits - 2):], 2)
    elif num < -1 * (2 ** (total_bits - 1)):
        num = int('1' + bin(int(hex(-1 * twos_complement(-1 * num, total_bits)), 16))[-(total_bits - 2):], 2)

    if num < 0:
        bin_num = format(int(hex(-1 * twos_complement(-1 * num, total_bits)), 16), formatting_string)
        hex_num = hex(int(bin_num, 2))
    else:
        hex_num = hex(num)

    return pad_hexa(make_hex_uppercase(hex_num), int(total_bits / 4))


# Five Stage Execution Procedure for Running an Instruction


# Here in Fetch, the PC and IR are Hexadecimal Strings of the Program Counter and Instruction Respectively
def fetch(PC, IR, branch):
    if PC is None:
        PC = "0x00000000"
    else:
        iag_output_dict = None
        if branch == False:
            iag_output_dict = iag(PC, None, None, 1, 0)
        else:
            iag_output_dict = iag(PC, None, "0x00000000", 1, 1)
        PC = iag_output_dict["PC"]

    IR = memory_file.read_data_from_memory(PC, 4, 'instruction_cache')

    return (PC, IR)


# In Decode, the instruction is a Hexadecimal String of format 0x0 0x123123112
def decode(instruction):
    split_instruction = instruction.split()
    bin_instruction = format(int(split_instruction[0], 16), '0>32b')
    # print(bin_instruction)
    op_code = bin_instruction[25:]
    # print(op_code)

    if (op_code == '0110011'):
        return instruction_encoding.extract_R_type(bin_instruction)

    elif (op_code == '0010011' or op_code == '0000011' or op_code == '1100111'):
        return instruction_encoding.extract_I_type(bin_instruction)

    elif (op_code == '0100011'):
        return instruction_encoding.extract_S_type(bin_instruction)

    elif (op_code == '1100011'):
        return instruction_encoding.extract_SB_type(bin_instruction)

    elif (op_code == '1101111'):
        return instruction_encoding.extract_UJ_type(bin_instruction)

    elif (op_code == '0010111' or op_code == '0110111'):
        return instruction_encoding.extract_U_type(bin_instruction)

    else:
        print("Invalid Instruction")
        return None


# Execute Step Performs the Function of the ALU directly on hexadecimal values
def execute(value1, value2, total_bits1, total_bits2, op):
    # print("execute", value1, value2)
    value1, value2 = get_neg_values(value1, value2, total_bits1, total_bits2)
    # print("execute", value1, value2)

    if op == 'addition':
        return bounding_hex(value1 + value2)

    elif op == 'subtract':
        return bounding_hex(value1 - value2)

    elif op == 'multiply':
        return bounding_hex(value1 * value2)

    elif op == 'divide':
        return bounding_hex(value1 // value2)

    elif op == 'remainder':
        return bounding_hex(value1 % value2)

    elif op == 'and_bitwise':
        return bounding_hex(value1 & value2)

    elif op == 'or_bitwise':
        return bounding_hex(value1 | value2)

    elif op == 'xor_bitwise':
        return bounding_hex(value1 ^ value2)

    elif op == 'shift_left_logical':
        return bounding_hex(value1 << value2)

    elif op == 'shift_right_logical':
        return bounding_hex(value1 >> value2)

    elif op == 'shift_right_arithmetic':
        return bounding_hex(value1 >> value2 + (2 ** (value2) - 1) * (2 ** (total_bits1 - value2)))

    elif op == 'check_if_equal':
        if (value1 == value2):
            return True
        else:
            return False

    elif op == 'check_if_less_than':
        if (value1 < value2):
            return True
        else:
            return False

    elif op == 'check_if_greater_than_equal_to':
        if (value1 >= value2):
            return True
        else:
            return False


def memory_access(MAR, MDR, num_bytes):
    if MAR != None and MDR != None:
        # print("MAR", MAR, "MDR", MDR)
        MAR = pad_hexa(make_hex_uppercase(MAR), 8)
        MDR = pad_hexa(make_hex_uppercase(MDR), 8)
        # memory_file.add_data_to_memory(MDR, MAR, num_bytes)
        memory_file.write_data_from_memory(MDR, MAR, num_bytes, 'data_cache')
        return None

    elif MAR != None and MDR == None:
        pad_hexa(make_hex_uppercase(MAR), 8)
        # MDR = memory_file.get_data_from_memory(MAR, num_bytes)
        MDR = memory_file.read_data_from_memory(MAR, num_bytes, 'data_cache')
        return MDR


def write_back(register_num, value):
    # register_num = 'x' + str(register_num)
    register_file.update_register_val(register_num, value)














