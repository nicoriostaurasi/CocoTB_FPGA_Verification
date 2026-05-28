"""cocotb testbench for this exercise.

Run from this directory with `make clean && make icarus=sim`.
"""

import cocotb
import logging
 
@cocotb.test()
async def test(dut):
      print('Executing DUT Code from python TB')