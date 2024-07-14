import re
def Extra(code):
    for ins in code:
        if "ADM" in ins:
            new="LD0100"
            new+=ins[13:16]
            new+=ins[7:10]
            new+='0'
            code.insert(code.index(ins),new)
            a=code.index(ins)
            ins=ins.replace("ADM","ADD")
            ins=list(ins)
            ins[7:10]=ins[13:16]
            ins=''.join(ins)
            code[a]=ins
            print(ins,code[a-1])
        if "NDM" in ins:
            new="LD0100"
            new+=ins[13:16]
            new+=ins[7:10]
            new+='0'
            code.insert(code.index(ins),new)
            a=code.index(ins)
            ins=ins.replace("NDM","NDD")
            ins=list(ins)
            ins[7:10]=ins[13:16]
            ins=''.join(ins)
            code[a]=ins
            print(ins,code[a-1])


def Modify(instructions):
    Modified=[]
    i=0
    print("reached")
    for ins in instructions:
        if "MOV" in ins:
            ins=ins.replace("MOV","ADI0000")
            ins+=" 0"
            print(ins)
        if "ADW" in ins:
            ins=ins.replace("ADW","")
            ins+="011"
        elif "ADC" in ins:
            print("reached")
            ins=ins.replace("ADC","")
            print("reached")
            ins+="010"
        elif "ADZ" in ins:
            ins=ins.replace("ADZ","")
            ins+="001"
        elif "ADD" in ins:
            print("reacheda")
            ins=ins.replace("ADD","")
            ins+="000"
        elif "ACW" in ins:
            ins=ins.replace("ACW","")
            ins+="111"
        elif "ACC" in ins:
            ins=ins.replace("ACC","")
            ins+="110"
        elif "ACZ" in ins:
            ins=ins.replace("ACZ","")
            ins+="101"
        elif "ACD" in ins:
            ins=ins.replace("ACD","")
            ins+="100"
        elif "NDC" in ins:
            ins=ins.replace("NDC","")
            ins+="010"
        elif "NDZ" in ins:
            ins=ins.replace("NDZ","")
            ins+="001"
        elif "NDD" in ins:
            ins=ins.replace("NDD","")
            ins+="000"
        elif "NCC" in ins:
            ins=ins.replace("NCC","")
            ins+="110"
        elif "NCZ" in ins:
            ins=ins.replace("NCZ","")
            ins+="101"
        elif "NCD" in ins:
            ins=ins.replace("NCD","")
            ins+="100"
        elif "LLI" in ins or "JPC" in ins or "JRC" in ins:
            ins2=ins[10:]
            ins=ins[3:10]
            ins2=format(int(ins2), f'09b')
            ins=ins+ins2
        elif "ST" in ins or "LD" in ins:
            ins2=ins[12:]
            ins=ins[2:12]
            ins2=format(int(ins2), f'06b')
            ins=ins+ins2
        elif "SM" in ins or "LM" in ins:
            ins2=ins[9:]
            ins=ins[2:9]
            ins2=format(int(ins2), f'09b')
            ins=ins+ins2
        elif "BEQ" in ins or "BLT" in ins or "BEL" in ins or "JTR" in ins or "ADI" in ins:
            ins2=ins[13:]
            ins=ins[3:13]
            ins2=format(int(ins2), f'06b')
            ins=ins+ins2
        if len(ins)==16:
            Modified.append(ins)
        else:
            print("Syntax Error at Line:",i)
            break
        i=i+1
    j=0
    print('(',j,"=>","\""+Modified[j][0:8]+"\",")
    print(' ',j+1,"=>","\""+Modified[j][8:16]+"\",")
    for j in range(1,len(instructions)):
        print(' ',2*j,"=>","\""+Modified[j][0:8]+"\",")
        print(' ',2*j+1,"=>","\""+Modified[j][8:16]+"\",")
    print("  others","=>","\"11100000\");")
    print(Modified)
        
text = """LLI R1 2     
          LLI R2 1
          LLI R3 19
          ADD R0 R1 R1
          ADC R3 R2 R0
          ACD R2 R1 R1
          ADC R3 R2 R0
          LM R6 127
          SM R7 255
          LM R6 255
          ADD R2 R3 R4
          ADZ R2 R3 R0 
          LLI R2 3
          LLI R1 10   
          LD R3 R1 1  
          ACZ R3 R2 R0
          LD R5 R0 3
          ACZ R3 R2 R0
          LD R0 R0 0
          LLI R1 31
          LLI R2 30
          BEQ R1 R2 1
          LLI R2 31
          BEQ R2 R1 3
          ADI R3 R3 1
          ADI R3 R0 37
          LLI R3 60
          JTR R4 R3 0
          JPC R4 2
          NDD R4 R4 R0
          ST R4 R4 2
          LLI R0 56
          """


replacements = {"ADI": "ADI0000", "ADD": "ADD0001", "ADC": "ADC0001","ADZ": "ADZ0001","ADW": "ADW0001", "ACD": "ACD0001", "ACC": "ACC0001","ACZ": "ACZ0001","ACW": "ACW0001","R1":"001","R0":"000","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","R7":"111","LLI":"0011","NDD": "NDD0010", "NDC": "NDC0010","NDZ": "NDZ0010", "NCD": "NCD0010", "NCC": "NCDC0010","NCZ": "NCDZ0010",", ":"\n", "LLI":"LLI0011", "LD":"LD0100", "ST":"ST0101", "SM":"SM0111", "LM":"LM0110", "BEQ":"BEQ1000", "BLT":"BLT1001", "BEL":"BEL1010", "SETZ":"1011000100000000", "SETC":"1011010000000000", "CLRC":"1011100000000000", "CLRZ":"1011001000000000", "CPLC":"1011110000000000", "CPLZ":"1011001100000000","JPC": "JPC1100","ADM":"ADM0001","JTR": "JTR1101","JRC": "JRC1111"}
for old, new in replacements.items():
    text = text.replace(old, new)
text=text.replace(" ","")
textlist=text.split()
Extra(textlist)
print(textlist)
Modify(textlist)