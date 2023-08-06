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
 
  fir_data.h -- 
 
  Original Author: Rocco Jonack, Synopsys, Inc.
 
 *****************************************************************************/
 
/*****************************************************************************
 
  MODIFICATION LOG - modifiers, enter your name, affiliation, date and
  changes you are making here.
 
  Name, Affiliation, Date: Junaid A. Khan, Agilent Technologies, March 17, 2007.

  Description of Modification: Added support to Cosimulate with ADS-Ptolemy.
    removed #include "fir_const.h" because these will be read now from ADS-Ptolemy.
    Changed sc_int<9>  coefs[16]; to sc_int<9>  * coefs; so that the pointer address
	could be assigned to coef in fir_top which are read inside ptolemy_sc_main.
	
 *****************************************************************************/

SC_MODULE(fir_data) {
   
  sc_in<bool>      reset;
  sc_in<unsigned>  state_out;
  sc_in<int>       sample;
  sc_out<int>      result;
  sc_out<bool>     output_data_ready;
  
  sc_int<19> acc;
  sc_int<8> shift[16];
  
  sc_int<9>  * coefs;

  SC_CTOR(fir_data)
    { 
      SC_METHOD(entry);
      dont_initialize();
      sensitive(reset);
      sensitive(state_out);
      sensitive(sample);
//#include "fir_const.h"
    };
  void entry();
};

