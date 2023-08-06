/** ***************************************************************** 
 UpSampler: This example shows the multi-rate Ptolemy-SystemC
    cosimulation. Please see corresponding .pl file for more details

 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

*********************************************************************/


#ifndef PT_SC_UpSample_H_INCLUDE
#define PT_SC_UpSample_H_INCLUDE 

#include <systemc.h>
#include <math.h>

SC_MODULE(PT_SC_UpSample) {
	sc_fifo_out<double> output;
	sc_fifo_in<double>  input;

	int Factor;
	int Phase;
	double Fill;

	SC_CTOR(PT_SC_UpSample) {
		Factor = 2; 
		Phase = 0;
		Fill = 0.0;	
		SC_THREAD(go);
	}
	void go();
};

#endif 
