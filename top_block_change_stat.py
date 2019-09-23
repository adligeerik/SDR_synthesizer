#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Sep 23 14:08:34 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.spacing = spacing = 1
        self.samp_rate = samp_rate = 2e6
        self.C_on = C_on = "1010100110011111100011100"
        self.C_off = C_off = "1010111001110110010111100"
        self.B_on = B_on = "1010110001010000000001010"
        self.B_off = B_off = "1010100010001110110001010"
        self.A_on = A_on = "1010010000010100101011000"
        self.A_off = A_off = "1010111100111001001011000"

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=530/2,
                decimation=1,
                taps=(1, ),
                fractional_bw=4,
        )
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(433.92e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.digital_map_bb_0 = digital.map_bb(([0x03C0,0xffff,0x0000]))
        self.blocks_vector_source_x_0 = blocks.vector_source_b([ int (x) for x in A_on ] + [ 2 ] * spacing, True, 1, [])
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(10)
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((1, ))
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(530/2, 1, 4000)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_complex_0, 0), (self.osmosdr_sink_0, 0))    
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_uchar_to_float_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_uchar_to_float_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.digital_map_bb_0, 0))    
        self.connect((self.digital_map_bb_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_moving_average_xx_0, 0))    

    def get_spacing(self):
        return self.spacing

    def set_spacing(self, spacing):
        self.spacing = spacing
        self.blocks_vector_source_x_0.set_data([ int (x) for x in self.A_on ] + [ 2 ] * self.spacing, [])

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_C_on(self):
        return self.C_on

    def set_C_on(self, C_on):
        self.C_on = C_on

    def get_C_off(self):
        return self.C_off

    def set_C_off(self, C_off):
        self.C_off = C_off

    def get_B_on(self):
        return self.B_on

    def set_B_on(self, B_on):
        self.B_on = B_on

    def get_B_off(self):
        return self.B_off

    def set_B_off(self, B_off):
        self.B_off = B_off

    def get_A_on(self):
        return self.A_on

    def set_A_on(self, A_on):
        self.A_on = A_on
        self.blocks_vector_source_x_0.set_data([ int (x) for x in self.A_on ] + [ 2 ] * self.spacing, [])

    def get_A_off(self):
        return self.A_off

    def set_A_off(self, A_off):
        self.A_off = A_off


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
