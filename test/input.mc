0x0	0x00500293	addi x5 x0 5	addi x5, x0, 5
0x4	0x00100313	addi x6 x0 1	addi x6, x0, 1
0x8	0x00029663	beq x5 x0 12	beq x5, x0, nxt
0xc	0x00330313	addi x6 x6 3	addi x6, x6, 3
0x10 0x00000463	beq x0 x0 8	beq x0, x0, END
0x14 0xFFF30313	addi x6 x6 -1	addi x6, x6, -1