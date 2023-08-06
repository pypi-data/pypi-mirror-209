/** ***************************************************************** 
 Signal generator without noise

 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

*********************************************************************/

#ifndef PT_SC_InputSignal_H_INCLUDE
#define PT_SC_InputSignal_H_INCLUDE 

#include <systemc.h>
#include <math.h>

SC_MODULE(PT_SC_InputSignal) {
	sc_fifo_out<double> outputSignal;
	sc_fifo_in<double>  inputFreq;
	sc_fifo_in<double>  inputMagnitude;
	
	double rampStep;
	

	double arg;
	SC_CTOR(PT_SC_InputSignal) {
		arg=0;
		rampStep = 0.314159;
		SC_THREAD(go);
	}
	void go();
};

#endif 
