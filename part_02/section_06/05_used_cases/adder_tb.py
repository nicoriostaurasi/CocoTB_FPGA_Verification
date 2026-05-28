import cocotb
import logging
import random
 
from cocotb.triggers import Timer
from cocotb.utils import get_sim_time
from cocotb.clock import Clock
 
async def rst_stimuli(dut):
      logging.info('Applying reset to DUT @ %0s',str(get_sim_time('ns')))	
      dut.rst.value = 1;
      await Timer(100,'ns')
      dut.rst.value = 0
      logging.info('System Reset Done @ %0s',str(get_sim_time('ns')))
      
 
@cocotb.test()
async def test(dut):
      logging.getLogger().setLevel(logging.INFO)	
      
      cocotb.start_soon(rst_stimuli(dut))
      cocotb.start_soon(Clock(dut.clk,20,'ns').start())
 
      await Timer(200,'ns')
    