/** ***************************************************************** 
 Generates random noise.

 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

 *********************************************************************/

#include "PT_SC_Noise.hxx"

void PT_SC_Noise::go() {

	arg = 0;
	double uniformnoise;
	while(1) {
		
		// Gnerate uniform noise between -1 & +1
		uniformnoise = 2.0 * (double)rand() / ((double)RAND_MAX);
		uniformnoise -= 1;

		uniformnoise *= inputNoiseMag.read()/1000000; // divided by 1000000 to conver from uV to V
		
		outputNoise.write(uniformnoise);
		
	}
}
