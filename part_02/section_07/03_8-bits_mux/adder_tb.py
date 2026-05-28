"""cocotb testbench for this exercise.

Run from this directory with `make clean && make icarus=sim`.
"""

import cocotb
import logging
import random
 
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue
 
	 
 
@cocotb.test()
async def test(dut):
    error_count = 0  # Initialize the error count
    logging.getLogger().setLevel(logging.INFO)
    
    a = 0
    b = 0
    c = 0
    d = 0
    dout = 0
 
    for _ in range(5):
        a = random.randint(0,255)
        b = random.randint(0,255)
        c = random.randint(0,255)
        d = random.randint(0,255)
        
        sel = random.randint(0, 3)
        
        dut.a.value = a
        dut.b.value = b
        dut.c.value = c
        dut.d.value = d
        
        dut.sel.value = sel
        
        await Timer(10, 'ns')
        
        dout = dut.dout.value.integer
        
        print('a:',a,'b:',b,'c:',c,'d:',d,'sel:',sel,'dout:', dout)
        
        if sel == 0 and dout != a :
            error_count += 1
        elif sel == 1 and dout != b :
            error_count += 1
        elif sel == 2 and dout != c :
            error_count += 1
        elif sel == 3 and dout != d :
            error_count += 1
        else:
            error_count = error_count
        
        await Timer(10, 'ns')
       
    print('--------------------------------------------------------')
    if error_count > 0:
        logging.error('Number of failed test cases: %d', error_count)
    else:
        logging.info('All test cases passed')
    print('--------------------------------------------------------')