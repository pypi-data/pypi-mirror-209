/** ***************************************************************** 
 Simple Adder: Blocking fifo read/write makes this logic to work 
               inside while(1) loop.

 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

 *********************************************************************/


#include "PT_SC_Adder.hxx"

void PT_SC_Adder::go() {
	
	while(1) {
		
		output.write(input1.read() + input2.read());
		
	}
}
