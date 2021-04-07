0x0 0x00200E93 addi x29 x0 2 addi x29 x0 2
0x4 0x00100F13 addi x30 x0 1 addi x30 x0 1
0x8 0x10000197 auipc x3 65536 auipc x3 65536
0xc 0xFF818193 addi x3 x3 -8 addi x3 x3 -8
0x10 0x00000213 addi x4 x0 0 addi x4 x0 0
0x14 0x00300293 addi x5 x0 3 addi x5 x0 3
0x18 0x10000597 auipc x11 65536 auipc x11 65536
0x1c 0xFE858593 addi x11 x11 -24 addi x11 x11 -24
0x20 0x008000EF jal x1 8 jal x1 mergesort
0x24 0x10000C63 beq x0 x0 280 beq x0 x0 ff
0x28 0xFFC10113 addi x2 x2 -4 addi x2 x2 -4
0x2c 0x00412023 sw x4 0(x2) sw x4 0(x2)
0x30 0xFFC10113 addi x2 x2 -4 addi x2 x2 -4
0x34 0x00512023 sw x5 0(x2) sw x5 0(x2)
0x38 0xFFC10113 addi x2 x2 -4 addi x2 x2 -4
0x3c 0x00112023 sw x1 0(x2) sw x1 0(x2)
0x40 0x02525863 bge x4 x5 48 bge x4 x5 exit
0x44 0x004284B3 add x9 x5 x4 add x9 x5 x4
0x48 0x01E4D2B3 srl x5 x9 x30 srl x5 x9 x30
0x4c 0xFDDFF0EF jal x1 -36 jal x1 mergesort
0x50 0x00128213 addi x4 x5 1 addi x4 x5 1
0x54 0x00412283 lw x5 4(x2) lw x5 4(x2)
0x58 0xFD1FF0EF jal x1 -48 jal x1 mergesort
0x5c 0x00812C83 lw x25 8(x2) lw x25 8(x2)
0x60 0x00400D33 add x26 x0 x4 add x26 x0 x4
0x64 0x00500DB3 add x27 x0 x5 add x27 x0 x5
0x68 0x001D8D93 addi x27 x27 1 addi x27 x27 1
0x6c 0x018000EF jal x1 24 jal x1 merge
0x70 0x00012083 lw x1 0(x2) exit:lw x1 0(x2)
0x74 0x00412283 lw x5 4(x2) lw x5 4(x2)
0x78 0x00812203 lw x4 8(x2) lw x4 8(x2)
0x7c 0x00C10113 addi x2 x2 12 addi x2 x2 12
0x80 0x00008067 jalr x0 x1 0 jalr x0,x1,0
0x84 0xFFC10113 addi x2 x2 -4 addi x2 x2 -4
0x88 0x00112023 sw x1 0(x2) sw x1 0(x2)
0x8c 0x01DC9CB3 sll x25 x25 x29 sll x25 x25 x29
0x90 0x01DD1D33 sll x26 x26 x29 sll x26 x26 x29
0x94 0x01DD9DB3 sll x27 x27 x29 sll x27 x27 x29
0x98 0x00BC8CB3 add x25 x25 x11 add x25 x25 x11
0x9c 0x00BD0D33 add x26 x26 x11 add x26 x26 x11
0xa0 0x00BD8DB3 add x27 x27 x11 add x27 x27 x11
0xa4 0x01900B33 add x22 x0 x25 add x22 x0 x25
0xa8 0x000D0A93 addi x21 x26 0 addi x21 x26 0
0xac 0x035CDA63 bge x25 x21 52 mergeloop: bge x25 x21 l1
0xb0 0x05BD5463 bge x26 x27 72 bge x26 x27 l2
0xb4 0x000CAB83 lw x23 0(x25) lw x23 0(x25)
0xb8 0x000D2C03 lw x24 0(x26) lw x24 0(x26)
0xbc 0x018BCA63 blt x23 x24 20 blt x23 x24 one
0xc0 0xFFC10113 addi x2 x2 -4 addi x2 x2 -4
0xc4 0x004D0D13 addi x26 x26 4 addi x26 x26 4
0xc8 0x01812023 sw x24 0(x2) sw x24 0(x2)
0xcc 0xFE1FF06F jal x0 -32 jal x0 mergeloop
0xd0 0xFFC10113 addi x2 x2 -4 addi x2 x2 -4
0xd4 0x004C8C93 addi x25 x25 4 addi x25 x25 4
0xd8 0x01712023 sw x23 0(x2) sw x23 0(x2)
0xdc 0xFD1FF06F jal x0 -48 jal x0 mergeloop
0xe0 0x03BD5863 bge x26 x27 48 bge x26 x27 mergeexit
0xe4 0x000D2C03 lw x24 0(x26) lw x24 0(x26)
0xe8 0x004D0D13 addi x26 x26 4 addi x26 x26 4
0xec 0xFFC10113 addi x2 x2 -4 addi x2 x2 -4
0xf0 0x01812023 sw x24 0(x2) sw x24 0(x2)
0xf4 0xFEDFF06F jal x0 -20 jal x0 l1
0xf8 0x015CDC63 bge x25 x21 24 l2: bge x25 x21 mergeexit
0xfc 0x000CAB83 lw x23 0(x25) lw x23 0(x25)
0x100 0x004C8C93 addi x25 x25 4 addi x25 x25 4
0x104 0xFFC10113 addi x2 x2 -4 addi x2 x2 -4
0x108 0x01712023 sw x23 0(x2) sw x23 0(x2)
0x10c 0xFEDFF06F jal x0 -20 jal x0 l2
0x110 0x01600CB3 add x25 x0 x22 add x25 x0 x22
0x114 0xFFCD8D93 addi x27 x27 -4 addi x27 x27 -4
0x118 0x019DCC63 blt x27 x25 24 blt x27 x25 mergebye
0x11c 0x00012883 lw x17 0(x2) lw x17 0(x2)
0x120 0x011DA023 sw x17 0(x27) sw x17 0(x27)
0x124 0x00410113 addi x2 x2 4 addi x2 x2 4
0x128 0xFFCD8D93 addi x27 x27 -4 addi x27 x27 -4
0x12c 0xFEDFF06F jal x0 -20 jal x0 in_loop
0x130 0x00012083 lw x1 0(x2) lw x1 0(x2)
0x134 0x00410113 addi x2 x2 4 addi x2 x2 4
0x138 0x00008067 jalr x0 x1 0 jalr x0,x1,0