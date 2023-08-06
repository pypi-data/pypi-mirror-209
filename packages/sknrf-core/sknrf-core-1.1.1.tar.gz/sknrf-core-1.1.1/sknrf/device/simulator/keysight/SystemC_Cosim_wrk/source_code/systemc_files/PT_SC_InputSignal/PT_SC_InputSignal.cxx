/** ***************************************************************** 
 Generates Signal with input frequency and magnitude.

 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan
 
*********************************************************************/

#include "PT_SC_InputSignal.hxx"

void PT_SC_InputSignal::go() {

	arg = 0;
	double outsignal;
	while(1) {
		outsignal = sin(arg * inputFreq.read()) *  inputMagnitude.read()/1000; // devided by 1000 to convert into V from mV
		outputSignal.write(outsignal);
		arg += rampStep;
	}
}
