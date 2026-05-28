import cocotb
import logging
import random
 
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue
 
def pri_model(input_bin):
 
    if input_bin.binstr[0] == '1':
        exp_val = '111'  
    elif input_bin.binstr[1] == '1':
        exp_val = '110'
    elif input_bin.binstr[2] == '1':
        exp_val = '101'
    elif input_bin.binstr[3] == '1':
        exp_val = '100'
    elif input_bin.binstr[4] == '1':
        exp_val = '011'
    elif input_bin.binstr[5] == '1':
        exp_val = '010'
    elif input_bin.binstr[6] == '1':
        exp_val = '001'
    elif input_bin.binstr[7] == '1':
        exp_val = '000'
   
    return exp_val
 
@cocotb.test()
async def test(dut):
    error_count = 0  # Initialize the error count
    logging.getLogger().setLevel(logging.INFO)
    
    input_bin = BinaryValue(value=0, n_bits=8, bigEndian=False)
    output_bin = BinaryValue(value=0, n_bits=3, bigEndian=False)
    
    for _ in range(30):
        input_rand = random.randint(0, 255)
        
        input_bin.integer = input_rand
       
        dut.en.value = 1
        dut.i.value = input_rand
        await Timer(10, 'ns')
        output = dut.y.value
        output_bin.integer = output
 
        
        
        print('Input:', input_bin.binstr, 'Output:', output_bin.binstr)
        print('ref_data :',pri_model(input_bin))
        
        if pri_model(input_bin) != output_bin.binstr:
            error_count += 1
            
        await Timer(10, 'ns')
       
    print('--------------------------------------------------------')
    if error_count > 0:
        logging.error('Number of failed test cases: %d', error_count)
    else:
        logging.info('All test cases passed')
    print('--------------------------------------------------------')





