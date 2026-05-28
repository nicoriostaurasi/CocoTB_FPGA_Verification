module mux(
    input [7:0] a,b,c,d,
    input [1:0] sel,
    output reg  [7:0] dout
    );

    always @(*)
    begin
        case (sel)
            2'b00: dout = a;
            2'b01: dout = b;
            2'b10: dout = c;
            2'b11: dout = d;
            default: dout = 8'h00;
        endcase
    end

    // Dump waveforms for post-simulation debugging.
    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(1,mux);
    end

endmodule
