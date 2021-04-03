0x0	0x10000537	lui x10 65536	lui x10,0x10000
0x4	0x00B00593	addi x11 x0 11	addi x11,x0,11
0x8	0x00100393	addi x7 x0 1	addi x7 x0 1
0xc	0x008000EF	jal x1 8	jal x1,bubblesort
0x10 0x06000063	beq x0 x0 96	beq x0,x0,finish
0x14 0x04758C63	beq x11 x7 88	beq x11,x7,exit
0x18 0x00100413	addi x8 x0 1	addi x8,x0,1
0x1c 0xFFC10113	addi x2 x2 -4	addi x2,x2,-4
0x20 0x00B12023	sw x11 0(x2)	sw x11,0(x2)
0x24 0xFFC10113	addi x2 x2 -4	addi x2,x2,-4
0x28 0x00112023	sw x1 0(x2)	sw x1,0(x2)
0x2c 0x00A00FB3	add x31 x0 x10	add x31,x0,x10
0x30 0x02B45263	bge x8 x11 36	bge x8,x11,ff
0x34 0x000FAF03	lw x30 0(x31)	lw x30,0(x31)
0x38 0x004FAE83	lw x29 4(x31)	lw x29,4(x31)
0x3c 0x01EED663	bge x29 x30 12	bge x29,x30,noswap
0x40 0x01DFA023	sw x29 0(x31)	sw x29,0(x31)
0x44 0x01EFA223	sw x30 4(x31)	sw x30,4(x31)
0x48 0x00140413	addi x8 x8 1	addi x8,x8,1
0x4c 0x004F8F93	addi x31 x31 4	addi x31,x31,4
0x50 0xFE1FF06F	jal x0 -32	jal x0 loop
0x54 0xFFF58593	addi x11 x11 -1	addi x11,x11,-1
0x58 0xFBDFF0EF	jal x1 -68	jal x1,bubblesort
0x5c 0x00012083	lw x1 0(x2)	lw x1,0(x2)
0x60 0x0045A583	lw x11 4(x11)	lw x11,4(x11)
0x64 0x00810113	addi x2 x2 8	addi x2,x2,8
0x68 0x00008067	jalr x0 x1 0	jalr x0, x1, 0
0x6c 0x00008067	jalr x0 x1 0	jalr x0, x1, 0