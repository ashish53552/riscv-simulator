0x0	0x00600513	addi x10 x0 6	addi x10,x0,6
0x4	0x00000193	addi x3 x0 0	addi x3,x0,0
0x8	0x00100213	addi x4 x0 1	addi x4,x0,1
0xc	0x00100F93	addi x31 x0 1	addi x31,x0,1
0x10 0x008000EF	jal x1 8	jal x1,fib
0x14 0x06000863	beq x0 x0 112	beq x0,x0,bye
0x18 0xFFC10113	addi x2 x2 -4	addi x2,x2,-4
0x1c 0x00112023	sw x1 0(x2)	sw x1,0(x2)
0x20 0xFFC10113	addi x2 x2 -4	addi x2,x2,-4
0x24 0x00A12023	sw x10 0(x2)	sw x10,0(x2)
0x28 0x02050663	beq x10 x0 44	beq x10,x0,se1
0x2c 0x03F50863	beq x10 x31 48	beq x10,x31,se2
0x30 0xFFF50513	addi x10 x10 -1	addi x10,x10,-1
0x34 0xFE5FF0EF	jal x1 -28	jal x1,fib
0x38 0xFFC10113	addi x2 x2 -4	addi x2,x2,-4
0x3c 0x00B12023	sw x11 0(x2)	sw x11,0(x2)
0x40 0xFFF50513	addi x10 x10 -1	addi x10,x10,-1
0x44 0xFD5FF0EF	jal x1 -44	jal x1,fib
0x48 0xFFC10113	addi x2 x2 -4	addi x2,x2,-4
0x4c 0x00B12023	sw x11 0(x2)	sw x11,0(x2)
0x50 0x00000A63	beq x0 x0 20	beq x0,x0,exit1
0x54 0x003005B3	add x11 x0 x3	se1:add x11,x0,x3
0x58 0x00000E63	beq x0 x0 28	beq x0,x0,exit
0x5c 0x004005B3	add x11 x0 x4	se2:add x11,x0,x4
0x60 0x00000A63	beq x0 x0 20	beq x0,x0,exit
0x64 0x00012E03	lw x28 0(x2)	lw x28,0(x2)
0x68 0x00412E83	lw x29 4(x2)	lw x29,4(x2)
0x6c 0x00810113	addi x2 x2 8	addi x2,x2,8
0x70 0x01DE05B3	add x11 x28 x29	add x11,x28,x29
0x74 0x00012503	lw x10 0(x2)	lw x10,0(x2)
0x78 0x00412083	lw x1 4(x2)	lw x1,4(x2)
0x7c 0x00810113	addi x2 x2 8	addi x2,x2,8
0x80 0x00008067	jalr x0 x1 0	jalr x0,x1,0