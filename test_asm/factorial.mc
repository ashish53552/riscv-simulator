0x0	0x00A00E93	addi x29 x0 10	addi x29 x0,10
0x4	0x00100E13	addi x28 x0 1	addi x28,x0 1
0x8	0x01D00333	add x6 x0 x29	add x6 x0 x29
0xc	0x008000EF	jal x1 8	jal x1 fact
0x10 0x02000E63	beq x0 x0 60	beq x0 x0 google
0x14 0x03C30863	beq x6 x28 48	beq x6 x28 exit
0x18 0xFFC10113	addi x2 x2 -4	addi x2,x2,-4
0x1c 0x00612023	sw x6 0(x2)	sw x6,0(x2)
0x20 0xFFC10113	addi x2 x2 -4	addi x2,x2,-4
0x24 0x00112023	sw x1 0(x2)	sw x1,0(x2)
0x28 0xFFF30313	addi x6 x6 -1	addi x6,x6,-1
0x2c 0xFE9FF0EF	jal x1 -24	jal x1 fact
0x30 0x00012083	lw x1 0(x2)	lw x1,0(x2)
0x34 0x00412303	lw x6 4(x2)	lw x6,4(x2)
0x38 0x00810113	addi x2 x2 8	addi x2 x2 8
0x3c 0x026D0D33	mul x26 x26 x6	mul x26 x26 x6
0x40 0x00008067	jalr x0 x1 0	jalr x0, x1, 0
0x44 0x00100D13	addi x26 x0 1	addi x26 x0 1
0x48 0x00008067	jalr x0 x1 0	jalr x0, x1, 0