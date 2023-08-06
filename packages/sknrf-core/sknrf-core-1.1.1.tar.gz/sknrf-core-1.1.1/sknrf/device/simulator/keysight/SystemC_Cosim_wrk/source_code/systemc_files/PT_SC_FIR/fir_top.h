/*****************************************************************************

  The following code is derived, directly or indirectly, from the SystemC
  source code Copyright (c) 1996-2004 by all Contributors.
  All Rights reserved.

  The contents of this file are subject to the restrictions and limitations
  set forth in the SystemC Open Source License Version 2.4 (the "License");
  You may not use this file except in compliance with such restrictions and
  limitations. You may obtain instructions on how to receive a copy of the
  License at http://www.systemc.org/. Software distributed by Contributors
  under the License is distributed on an "AS IS" basis, WITHOUT WARRANTY OF
  ANY KIND, either express or implied. See the License for the specific
  language governing rights and limitations under the License.

 *****************************************************************************/

/*****************************************************************************
 
  fir_top.h --
 
  Original Author: Rocco Jonack, Synopsys, Inc.
 
 *****************************************************************************/
 
/*****************************************************************************
 
  MODIFICATION LOG - modifiers, enter your name, affiliation, date and
  changes you are making here.
 
  Name, Affiliation, Date: Junaid A. Khan, Agilent Technologies, March 17, 2007.
  
  Description of Modification: Added support to Cosimulate with ADS-Ptolemy. Following 
    lines are added in this file to read paramters from ADS-Ptolemy inside ptolemy_sc_main
	and pass it to fir_data1. 
  
  sc_int<9> coefs[16]; 

  fir_data1 -> coefs = coefs;  
 *****************************************************************************/

#include <systemc.h>
#include "fir_fsm.h"
#include "fir_data.h"

SC_MODULE(fir_top) {

  sc_in<bool>       CLK;
  sc_in<bool>       RESET;
  sc_in<bool>       IN_VALID;
  sc_in<int>     SAMPLE;
  sc_out<bool>      OUTPUT_DATA_READY;
  sc_out<int>       RESULT;

  sc_signal<unsigned> state_out;

  /// Added to read Taps value inside ptolemy_sc_main before sc_start
  sc_int<9> coefs[16];
  
  fir_fsm  *fir_fsm1;
  fir_data *fir_data1;

  SC_CTOR(fir_top) {

      fir_fsm1 = new fir_fsm("FirFSM");
      fir_fsm1->clock(CLK);
      fir_fsm1->reset(RESET);
      fir_fsm1->in_valid(IN_VALID);
      fir_fsm1->state_out(state_out);

      fir_data1 = new fir_data("FirData");
      fir_data1 -> reset(RESET);
      fir_data1 -> state_out(state_out);
      fir_data1 -> sample(SAMPLE);
      fir_data1 -> result(RESULT);
      fir_data1 -> output_data_ready(OUTPUT_DATA_READY);
       
	  /// Pointer in fir_data1 ->coefs is assigned the address
	  /// of coefs in fir_top.
	  fir_data1 -> coefs = coefs;

    }
};

