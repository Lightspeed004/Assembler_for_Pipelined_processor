This is an assembler programmed specifically for the Pipelined processor you'll find on the same repository
Note that R0 is PC, if the value of R0 changes, PC will jump to that location
Instructions:
ADD R1 R2 R3, adds content of R1 and R2 and stores it in R3
ADC R1 R2 R3, adds content of R1 and R2 and stores it in R3 if carry flag is set
ADZ R1 R2 R3, adds content of R1 and R2 and stores it in R3 if zero flag is set
ADW R1 R2 R3, adds content of R1 and R2 and the Carry flag and stores it in R3
ACD,ACC,ACZ and ACW are similar but they subtract R2 from R1
ADI R1 R2 23 adds R1 to 23 and stores it in R2, the immediate value cannot exceed 63, otherwise the number in consideration would be x%64
LLI R2 49 will load 49 into R2, the immediate has to be smaller than 512
NDD,NDC,NDZ,NCD,NCC,NCZ: These 3-address operations nand the content of the 1st and 2nd register and store them in the 3rd(conditionally or unconditionally
															   	just like in addition)
LD R1 R2 1 loads the content stored at the (R2+1)th location in Data Mem to R1, here the immediate value has to be smaller than 64 again
ST R1 R2 1 store the value in R1 at the (R2+1)th location in Data Mem
JPC R1 9 makes the PC jump to PC+2*9 and stores PC+2 in R1
JTR R1 R2 1, makes the PC jump to PC+R2+1 and stores PC+2 in R1
JRC R1 94, makes the PC jump to R1+2*94, immediate value cannot exceed 511 again
BEQ R1 R2 8, branches to PC+2*8 if R1=R2
BLT, branches on less than, BEL branches on less than or equal to
LM R1 3 will load values from Data Mem to R1,R2... which are stored at consecutive locations starting from @R1.T he registers in which the value will be loaded is decided by the 8 bit binary sequence of the immediate value so this instruction will store values into R7 and R6 only as 3="00000011"
SM does the same thing but it stores values at the aforementioned consecutive location, the binary sequence decides the values to be stored
MOV R1 R2 moves the value of R1 in R2
ADM adds the value of @R1 + R2 and stores it in R3
NDM nands the value of @R1 and R2 and stores it in R3

Given in this file is a Program which tests most instructions, Ill try to add some other sample programs soon













































Do not use LM SM for loading or storing the values of 2 or less registers

