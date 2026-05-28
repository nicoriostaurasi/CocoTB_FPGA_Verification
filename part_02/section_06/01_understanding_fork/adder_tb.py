import cocotb
import logging
from cocotb.triggers import Timer
from cocotb.utils import get_sim_time
 
#fixed duration rst - 2 pos edge clk ,
 
@cocotb.coroutine
async def task1(dut):
      logging.warning('Task 1 get control @ %0s', str(get_sim_time(units = 'ns')))
      await Timer(1, units = 'ns')
      logging.warning('Inside Task 1 @ %0s', str(get_sim_time(units = 'ns')))
      await Timer(1, units = 'ns')
      logging.warning('Ended Task 1 @ %0s', str(get_sim_time(units = 'ns')))
 	 
 	 
@cocotb.coroutine
async def task2(dut):
      logging.warning('Task 2 get control @ %0s', str(get_sim_time(units = 'ns')))
      await Timer(2, units = 'ns')
      logging.warning('Inside Task 2 @ %0s', str(get_sim_time(units = 'ns')))
      await Timer(1, units = 'ns')
      logging.warning('Ended Task 2 @ %0s', str(get_sim_time(units = 'ns')))
 	 
 
 
@cocotb.coroutine
async def task3(dut):
      logging.warning('Task 3 get control @ %0s', str(get_sim_time(units = 'ns')))
      await Timer(3, units = 'ns')
      logging.warning('Inside Task 3 @ %0s', str(get_sim_time(units = 'ns')))
      await Timer(1, units = 'ns')
      logging.warning('Ended Task 3 @ %0s', str(get_sim_time(units = 'ns')))
 
 
@cocotb.test()
async def test(dut):
      cocotb.fork(task1(dut))
      cocotb.fork(task2(dut))
      cocotb.fork(task3(dut))
      await Timer(7, 'ns')
