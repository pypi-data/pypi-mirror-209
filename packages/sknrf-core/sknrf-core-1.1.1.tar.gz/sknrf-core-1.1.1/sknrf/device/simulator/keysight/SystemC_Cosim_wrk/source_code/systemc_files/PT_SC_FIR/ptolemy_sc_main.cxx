/** ***************************************************************** 
 
 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

 This file implemenst ptolemy_sc_main to cosimulate with ADS-Ptolemy
*********************************************************************/

 
#include <systemc.h>
#include "stimulus.h"
#include "display.h"
#include "fir_top.h"
#include "SystemCPtolemyInterface_PT_SC_FIR.hxx"

void ptolemy_sc_main(int argc, char * argv[], SystemCPtolemyInterface_PT_SC_FIR & p) {
  sc_clock        clock;
  sc_signal<bool> reset;
  sc_signal<bool> input_valid;        
  sc_signal<int>  sample;  	    
  sc_signal<bool> output_data_ready;
  sc_signal<int>  result;
  sc_fifo<int> pt2sc;
  sc_fifo<int> sc2pt;

  stimulus stimulus1("stimulus_interface");
  stimulus1.reset(reset); 
  stimulus1.input_valid(input_valid); 
  stimulus1.sample(sample); 
  stimulus1.CLK(clock.signal());
  stimulus1.sampleFromPtolemy(pt2sc);

  p.input(pt2sc);
  p.output(sc2pt);

  fir_top   fir_top1    ( "process_body");
  fir_top1.RESET(reset); 
  fir_top1.IN_VALID(input_valid); 
  fir_top1.SAMPLE(sample); 
  fir_top1.OUTPUT_DATA_READY(output_data_ready); 
  fir_top1.RESULT(result); 
  fir_top1.CLK(clock.signal());

  display  display1 ( "display_interface");
  display1.output_data_ready(output_data_ready);
  display1.result(result); 
  display1.outputToPtolemy(sc2pt);


  for(int i =0 ; i < 16; i++) {
	  fir_top1.coefs[i] = p.getIntegerParamValue(p.Taps,i);
  }


  sc_start(clock, -1);
}

