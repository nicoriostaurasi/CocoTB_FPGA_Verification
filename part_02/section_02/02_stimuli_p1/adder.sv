`timescale 1ns/1ps

module adder(
    input [3:0] a,b,
    output [4:0] s
    );

    assign s = a + b;

    // Dump waveforms for post-simulation debugging.
    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(1,adder);
    end

endmodule
