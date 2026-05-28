import cocotb
import logging
import random
 
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue
 
def pri_model(din):
    if din >= 128 and din < 256:
        return 7
    elif din >= 64  and din < 128 :
    	return 6
    elif din >= 32  and din < 64 :
    	return 5
    elif din >= 16  and din < 32 :
    	return 4
    elif din >= 8  and din < 16 :
    	return 3
    elif din >= 4  and din < 8 :
    	return 2
    elif din >= 2  and din < 4 :
    	return 1
    elif din >= 1  and din < 2 :
    	return 0
    else:
        return 0	 
 
@cocotb.test()
async def test(dut):
    error_count = 0  # Initialize the error count
    logging.getLogger().setLevel(logging.INFO)
    
    #input_bin = BinaryValue(value=0, n_bits=8, bigEndian=False)
    #output_bin = BinaryValue(value=0, n_bits=3, bigEndian=False)
    data_in = 0
    data_out= 0
    for _ in range(30):
        data_in = random.randint(0, 255)
        
        dut.en.value = 1
        dut.i.value = data_in
        await Timer(10, 'ns')
        data_out = dut.y.value.integer  
        print('Input:', data_in, 'Output:', data_out)
        print('ref data:',pri_model(data_in))
        
        if pri_model(data_in) != data_out:
            error_count += 1
     
        await Timer(10, 'ns')
       
    print('--------------------------------------------------------')
    if error_count > 0:
        logging.error('Number of failed test cases: %d', error_count)
    else:
        logging.info('All test cases passed')
    print('--------------------------------------------------------')