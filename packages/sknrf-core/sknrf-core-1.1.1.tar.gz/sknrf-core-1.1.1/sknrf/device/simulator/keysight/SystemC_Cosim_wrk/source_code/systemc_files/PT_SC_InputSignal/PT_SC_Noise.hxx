/** ***************************************************************** 
 Random noise generator.

 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan
 
*********************************************************************/

#ifndef PT_SC_Noise_H_INCLUDE
#define PT_SC_Noise_H_INCLUDE 

#include <systemc.h>
#include <math.h>

SC_MODULE(PT_SC_Noise) {
	sc_fifo_out<double> outputNoise;
	sc_fifo_in<double>  inputNoiseMag;
	
	

	double arg;
	SC_CTOR(PT_SC_Noise) {
		SC_THREAD(go);
	}
	void go();
};

#endif 
