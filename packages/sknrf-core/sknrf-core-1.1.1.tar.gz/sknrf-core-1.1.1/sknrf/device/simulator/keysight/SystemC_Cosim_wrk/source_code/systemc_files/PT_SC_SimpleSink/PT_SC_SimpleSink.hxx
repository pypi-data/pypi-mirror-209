/** ***************************************************************** 

 Simple sink that writes the values between sample indexed [start stop]
 and write these to a file. File name could be specified in ADS-Ptolemy
 schematic as CmdArgs. The sink issues a STOP command after collecting
 "stop" number of values.

 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

*********************************************************************/



#ifndef PT_SC_SimpleSink_H_INCLUDE
#define PT_SC_SimpleSink_H_INCLUDE 

#include <systemc.h>
#include <fstream>
#include <string.h>

SC_MODULE(PT_SC_SimpleSink) {
	sc_fifo_in<int> input;

	char  outFileName[64];
	int start;
	int stop;
	ofstream outFile;

	SC_CTOR(PT_SC_SimpleSink) {
		strcpy(outFileName,"defaultSinkFile.txt");
	    start = 0;
		stop = 100;
		SC_THREAD(go);
	}
	void go();
};

#endif 
