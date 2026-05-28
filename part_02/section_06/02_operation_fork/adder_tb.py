import cocotb
import logging
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge, Edge, ClockCycles
from cocotb.utils import get_sim_time
 
#fixed duration rst - 2 pos edge clk ,
 
@cocotb.coroutine
async def task1(dut):
  	cocotb.fork(task2(dut))
  	logging.warning('Task 1 Get Control @ %0s', str(get_sim_time(units = 'ns')))
  	await Timer(1, units = 'ns')
  	logging.warning('Inside Task 1 @ %0s', str(get_sim_time(units = 'ns')))
  	await Timer(1, units = 'ns')
  	logging.warning('Ended Task 1 @ %0s', str(get_sim_time(units = 'ns')))
 	 
 	 
@cocotb.coroutine
async def task2(dut):
  	cocotb.fork(task3(dut))
  	logging.warning('Task 2 Get Control @ %0s', str(get_sim_time(units = 'ns')))
  	await Timer(1, units = 'ns')
  	logging.warning('Inside Task 2 @ %0s', str(get_sim_time(units = 'ns')))
  	await Timer(1, units = 'ns')
  	logging.warning('Ended Task 2 @ %0s', str(get_sim_time(units = 'ns')))
 	 
 
 
@cocotb.coroutine
async def task3(dut):
  	logging.warning('Task 3 Get Control @ %0s', str(get_sim_time(units = 'ns')))
  	await Timer(1, units = 'ns')
  	logging.warning('Inside Task 3 @ %0s', str(get_sim_time(units = 'ns')))
  	await Timer(1, units = 'ns')
  	logging.warning('Ended Task 3 @ %0s', str(get_sim_time(units = 'ns')))
 
 
@cocotb.test()
async def test(dut):
  	cocotb.fork(task1(dut))
  	await Timer(20, 'ns')