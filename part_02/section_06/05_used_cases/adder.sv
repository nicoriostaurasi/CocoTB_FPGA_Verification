module top(
    input rst,clk
    );

    // Dump waveforms for post-simulation debugging.
    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(1,top);
    end

endmodule
