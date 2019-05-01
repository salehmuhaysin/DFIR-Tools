import idautils 
import idaapi

""" 
place the cursor in any address and it will read the list of strings:
example:
addr_0    str*
addr_4    size
addr_8    str*
addr_C    size
...

"""

cur_line_addr = int(GetCurrentLine().split(' ')[0].split(':')[1] ,16 )
cur_size_addr = cur_line_addr + 0x4

while True:
    cur_line_val = Dword(cur_line_addr)
    cur_size_val = Dword(cur_size_addr)
    
    if cur_size_val == 0:
        break
        
    string = idc.GetManyBytes(cur_line_val , cur_size_val)
    
    print string
    
    cur_line_addr = cur_line_addr + 8
    cur_size_addr = cur_size_addr + 8
    
