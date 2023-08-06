/** ***************************************************************** 
 A Sine wave generator

 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

 *********************************************************************/

 
#include "PT_SC_SineGen.hxx"

void PT_SC_SineGen::go() {

	arg = InitialRadians;

	while(1) {
		output.write(sin(arg));
		arg += RadiansPerSample;
	}
}
