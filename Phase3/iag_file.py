# File containing the function of the Instruction Address Generator (IAG)

# pc_prev : Previous Program Counter (Input to MuxPC)
# ra : Return Address (Input to MuxPC)
# imm : Immediate Value (Input to MuxINC)
# mux_pc_cs : Control Signal to MuxPC where {0 : Take ra, 1 : Take PC}
# mux_inc_cs : Control Signal to MuxINC where {0 : Take 4, 1 : Take imm}

import five_stage_execution as fs


def iag(pc_prev, ra, imm, mux_pc_cs, mux_inc_cs):
    mux_pc_output = None
    mux_inc_output = None

    if mux_pc_cs == 0:
        mux_pc_output = ra
    else:
        mux_pc_output = pc_prev

    if mux_inc_cs == 0:
        mux_inc_output = "0x00000004"
    else:
        mux_inc_output = imm

    # print("IAG = ", mux_pc_output, mux_inc_output)

    iag_output = {"PC": fs.pad_hexa(fs.make_hex_uppercase(hex(int(mux_pc_output, 16) + int(mux_inc_output, 16))), 8),
                  "PC_temp": fs.pad_hexa(fs.make_hex_uppercase(hex(int(mux_pc_output, 16) + 4)), 8)}

    return iag_output























