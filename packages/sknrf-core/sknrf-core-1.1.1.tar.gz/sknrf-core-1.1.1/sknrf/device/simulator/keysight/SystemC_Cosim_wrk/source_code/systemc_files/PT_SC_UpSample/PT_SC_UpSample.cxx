/** ***************************************************************** 
 UpSampler: This example shows the multi-rate Ptolemy-SystemC
    cosimulation. Please see corresponding .pl file for more details

 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

*********************************************************************/


#include "PT_SC_UpSample.hxx"

void PT_SC_UpSample::go() {

	int i, match ;
	match = Factor - Phase - 1;

	while(1) {

		for(i=0; i< Factor; i++)
		{
			if(i==match)
				output.write(input.read());
			else
				output.write(Fill);
		}
	}
}
