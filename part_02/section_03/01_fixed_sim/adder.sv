`timescale 1ns/1ps

module adder(
    input rst
    );

    // Dump waveforms for post-simulation debugging.
    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(1,adder);
    end

endmodule
