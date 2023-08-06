/** ***************************************************************** 
 Simple Adder SC_MODULE

 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

*********************************************************************/

#ifndef PT_SC_Adder_H_INCLUDE
#define PT_SC_Adder_H_INCLUDE 

#include <systemc.h>


SC_MODULE(PT_SC_Adder) {
	sc_fifo_out<double> output;
	sc_fifo_in<double>  input1;
	sc_fifo_in<double>  input2;

	double arg;
	SC_CTOR(PT_SC_Adder) {
		SC_THREAD(go);
	}
	void go();
};

#endif 
