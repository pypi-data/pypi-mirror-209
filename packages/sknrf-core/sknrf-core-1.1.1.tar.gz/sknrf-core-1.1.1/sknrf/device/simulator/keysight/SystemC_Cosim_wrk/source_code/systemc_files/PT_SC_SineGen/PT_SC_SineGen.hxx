/** ***************************************************************** 
 A Sine wave generator

 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

 *********************************************************************/


#ifndef PT_SC_Sine_H_INCLUDE
#define PT_SC_Sine_H_INCLUDE 

#include <systemc.h>
#include <math.h>

SC_MODULE(PT_SC_SineGen) {
	sc_fifo_out<double> output;

	double RadiansPerSample;
	double InitialRadians;
	double arg;

	SC_CTOR(PT_SC_SineGen) {
		RadiansPerSample = 3.141592653589793/50; // default value
		InitialRadians = 0.0;	
		SC_THREAD(go);
	}
	void go();
};

#endif 
