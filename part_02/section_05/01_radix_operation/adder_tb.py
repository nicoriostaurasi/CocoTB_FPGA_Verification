import cocotb
import logging
import random
     
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue
     
@cocotb.test()
async def test(dut):
                                                                                            logging.getLogger().setLevel(logging.INFO)
    a = BinaryValue(n_bits = 8, bigEndian = False, value = 0)
    b = BinaryValue(n_bits = 8, bigEndian = False, value = 0)
    # adding values to binaryvalue variable
    # integer , signed_integer, binstr
    #a.integer = 10
    #a.binstr = '1111'
    #print(a.integer)
    #print(a.binstr)
    #a.integer = 35
    
    #convert to value to diff repre
    #print(a._convert_to_unsigned(a.integer))
    #print(b._convert_to_signed_mag(-35))
    #print(b._convert_to_twos_comp(-35))
      # convert to different radix 
    #bin, hex, bool, oct
    #print(a.binstr)
    #print(hex(a.integer))
    #print(bool(a.integer))
    
    a.binstr = '10100011' # 
    #bitwise : ilshift, irshift, _invert, 
    #print(a.__ilshift__(1))
    #print(a._invert(a.binstr))
    #print(a.__lshift__(1))
    
    
    print(len(a.binstr))
    print(a.is_resolvable)
