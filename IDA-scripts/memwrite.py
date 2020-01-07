

import idautils 
import idaapi

# encode = 1 > ascii
# encode = 2 > wide char
def memwrite(ea, str , encode=1):
    i = 0 
    addr = ea
    for i in str:
        b = ord(i)
        idc.PatchByte(addr , b )
        
        if encode == 2:
            idc.PatchByte(addr + 1 , 0x00 )
            addr +=1
        
        addr +=1 
    
    idc.PatchByte(addr , 0x00 )
    idc.PatchByte(addr + 1 , 0x00 )
                

# example: memwrite(0x10000000 , "string" , 2)
