# cocotb simulation settings for this exercise.
TOPLEVEL_LANG ?= verilog
SIM ?= icarus

VERILOG_SOURCES = $(shell pwd)/adder.sv
TOPLEVEL := adder  # Verilog/SystemVerilog top module
MODULE   := adder_tb  # Python testbench module

include $(shell cocotb-config --makefiles)/Makefile.sim
