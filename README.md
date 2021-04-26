# RISC-V-Simulator

A Simulator for a 32 bit RISC-V Instruction Set Architecture (ISA).

### Team Information & Contributions
#### Phase 1
	Divyansh Srivastava	2018MEB1009	Instructions for SB, U Format & Memory Organization	
	Vikram Setty		2018MED1010	Instructions for UJ Format, Five Stage Execution & IAG		
	Ashish Kaushik		2018MMB1279	Instructions for I Format & GUI
	Shrish Tripathi		2018MMB1294	Instructions for S Format & GUI
	Hrishikesh Pawar	2018MEB1241	Instructions for R Format, Register & PMI Organization
#### Phase 2
	Divyansh Srivastava	2018MEB1009	Hazard Detection Unit, Overall Datapath in the Pipeline	
	Vikram Setty		2018MED1010	New Control Circuitry for the Entire Pipelined Implementation	
	Ashish Kaushik		2018MMB1279	Auxilliary Pipeline Functions & GUI
	Shrish Tripathi		2018MMB1294	Auxilliary Pipeline Functions & GUI
	Hrishikesh Pawar	2018MEB1241	Buffer Implementation	
	
### Phase 1
  The **Simulator** executes a sequence of machine code instructions to mimic the basic data and control path of RISC-V ISA.
  
### Phase 2
  The **Simulator** is enabled with pipelining capabilities, equipped with data-forwarding & static branch prediction mechanisms, with statistics related to CPI, number of hazards, number of branch mispredictions, etc visible for executions under different conditions enabled in the GUI.
      
### Technology Stack
	Python 3 (for development of the simulator)
	NodeJS, ExpressJS, Javascript, HTML and CSS (for GUI)

### File Structure

```
RISC-V-Simulator
├─ app.js
├─ img
│  ├─ datapath.png
│  ├─ iag.png
│  └─ pmi.png
├─ package-lock.json
├─ package.json
├─ Phase1
│  ├─ execute_instruction.py
│  ├─ five_stage_execution.py
│  ├─ iag_file.py
│  ├─ instruction_encoding.py
│  ├─ main.py
│  ├─ memory_file.py
│  └─ register_file.py
├─ Phase2
|  ├─ auxilliary_functions.py
|  ├─ branch_address_table.py
|  ├─ demofile3.txt
│  ├─ execute_instruction.py
│  ├─ five_stage_execution.py
│  ├─ iag_file.py
|  ├─ inp.txt
│  ├─ instruction_encoding.py
│  ├─ main.py
|  ├─ main2.py
│  ├─ memory_file.py
|  ├─ pipeline_stage_functions.py
|  ├─ pipelined_execution.py
|  ├─ register_file.py
│  └─ test.txt
├─ Procfile
├─ public
│  ├─ css
│  │  └─ sim.css
│  └─ js
│     └─ venus.js
├─ README.md
├─ test
│  ├─ bubble_sort(10_inputs).mc
│  ├─ factorial(of_10_in_x26).mc
│  ├─ fibonacci(6th_number_in_x29).mc
│  └─ merge(4_inputs).mc
└─ views
   ├─ index.ejs
   └─ Partials
      ├─ footer.ejs
      └─ header.ejs

```		


	* Phase1 - Contains the python files for various stages like instruction decoding, five stage execution, memory file, register file.
	* Phase2 - Contains the python files for executing a set of instructuions in a pipelined fashion with data forwarding and static branch prediction techniques.
	* test - Contains few testcases to test the validity of the simulator.
	* public - Contains CSS and JS components of the front-end of the GUI.
	* views - Contains the Express.js and JS components for the back-end of the GUI.
	* app.js - Main file combining frontend and backend(both express and python components) of the Simulator. 

### How to Execute
   * The simulator is deployed at https://sheltered-journey-97920.herokuapp.com/#

   * For running it *locally* **(Python and Node Required)**<br>
  ```
		git clone "repo url"
		npm install
		node app.js
  ```
         Now the simulator can be accessed at http://localhost:80/
	 
   * Once the webpage is started, paste the machine code in the code window. You can optionally provide data directly to data memory from the input window like in case of codes like for bubble and merge sort. This accepts *space seperated values in decimal format*. You can optionally set the knobs to enable or disable pipelining and data forwarding. Additional knobs are also available to print all the pipeline buffer/register values, or their values for a particular instruction (which can be mentioned by typing it's program counter (PC) in the format *0xABCDEFGH* or in a capitalized 8 digit hexadecimal format). Then click on submit and check the registers and memory sections after program execution.
	
### Instructions Supported
	R-Type:
		add, and, or, sll, slt, sra, srl, sub, xor, mul, div, rem
	I-Type :
		addi, andi, ori, lb, lh, lw, jalr
	S-Type:
		sb, sw, sh
	SB-Type:
		beq, bne, bge, blt
	U-Type:
		auipc, lui
	UJ-Type:
		jal

### Input and Output Information
###### The input file/set of instructions should contain a sequence of machine code instructions (corresponding to 32 bit RISC-V instructions) in the format - 'Instruction number' followed by the 'machine code'. An example would look like :
	0x00 0x00a00e93
	0x04 0x00100e13
	0x08 0x01d00333
	.
	.
	.
	0x48 0x00008067
	0x4c 0x00000000
###### The output format in the GUI is in the following format :
	Register Data 	: 32 Registers with their Corresponding 32 bit Hexadecimal Values
	Memory Data 	: Text, Data & Stack Memory Segments in Little Endian Format
	Stats           : In case of pipeline implementations, features like CPI, number of hazard etc.
	Debug Info      : Details of interstage buffers after each cycle and buffer values of a given instruction (using its PC) in various cycles.
