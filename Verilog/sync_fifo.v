//==============================================================================
// Copyright (C) 2015 By Kellen.Wang
// mail@kellen.wang, All Rights Reserved
//==============================================================================
// Module : sync_fifo
// Author : Kellen Wang
// Contact : kellen.wang124@gmail.com
// Date : Jan.17.2015
//==============================================================================
// Description :
//==============================================================================
module sync_fifo #(
 parameter DEPTH = 32,
 parameter DATA_W = 32
) (
 input wire clk ,
 input wire rst_n ,
 input wire wreq ,
 input wire [DATA_W-1:0] wdata ,
 output wire full_flg ,
 input wire rreq ,
 output wire [DATA_W-1:0] rdata ,
 output wire empty_flg
);
`ifdef DUMMY_SYNC_FIFO
assign full_flg = 1'd0;
assign rdata = 32'd0;
assign empty_flg = 1'd0;
`else
`include "get_width.inc"
//==============================================================================
// Constant Definition :
//==============================================================================
localparam DLY = 1'd1;
localparam FULL = 1'd1;
localparam NOT_FULL = 1'd0;
localparam EMPTY = 1'd1;
localparam NOT_EMPTY = 1'd0;
localparam ADDR_W = get_width(DEPTH-1);
//==============================================================================
// Variable Definition :
//==============================================================================
reg [ADDR_W-1:0] waddr;
reg [ADDR_W-1:0] raddr;
wire [ADDR_W-1:0] waddr_nxt;
wire [ADDR_W-1:0] raddr_nxt;
//==============================================================================
// Logic Design :
//==============================================================================
assign waddr_nxt = waddr + 1;
assign raddr_nxt = raddr + 1;
assign full_flg = (waddr_nxt == raddr)? FULL : NOT_FULL;
assign empty_flg = (waddr == raddr)? EMPTY : NOT_EMPTY;
assign iwreq = wreq & ~full_flg;
assign irreq = 1'd1;

always @(posedge clk or negedge rst_n) begin
 if (!rst_n) begin
 waddr <= #DLY 0;
 end
 else if(wreq & (full_flg == NOT_FULL)) begin
 waddr <= #DLY waddr_nxt;
 end
end

always @(posedge clk or negedge rst_n) begin
 if (!rst_n) begin
 raddr <= #DLY 0;
 end
 else if(rreq & (empty_flg == NOT_EMPTY)) begin
 raddr <= #DLY raddr_nxt;
 end
end

//synopsys translate_off
`ifdef DEBUG_ON
iError_fifo_write_overflow:
assert property (@(posedge wclk) disable iff (!rst_n) (iwreq & !full_flg));
iError_fifo_read_overflow:
assert property (@(posedge rclk) disable iff (!rst_n) (irreq & !empty_flg));
`endif
//synopsys translate_on 

//==============================================================================
// Sub-Module :
//==============================================================================
shell_dual_ram #(
 .ADDR_W (ADDR_W ),
 .DATA_W (DATA_W ),
 .DEPTH (DEPTH )
) u_shell_dual_ram (
 .wclk (clk ),
 .write (iwreq ),
 .waddr (waddr ),
 .wdata (wdata ),
 .rclk (clk ),
 .read (irreq ),
 .raddr (raddr ),
 .rdata (rdata )
);
`endif // `ifdef DUMMY_SYNC_FIFO
endmodule
