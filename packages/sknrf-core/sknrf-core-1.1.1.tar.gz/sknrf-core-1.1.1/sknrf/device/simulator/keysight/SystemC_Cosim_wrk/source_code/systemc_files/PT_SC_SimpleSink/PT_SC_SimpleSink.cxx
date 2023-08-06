/** ***************************************************************** 

 Simple sink that writes the values between sample indexed [start stop]
 and write these to a file. File name could be specified in ADS-Ptolemy
 schematic as CmdArgs. The sink issues a STOP command after collecting
 "stop" number of values.

 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

*********************************************************************/


#include "PT_SC_SimpleSink.hxx"

void PT_SC_SimpleSink::go() {

	outFile.open(outFileName);
    
	int count = 0;
	
	int tmpData;

	outFile << "#\t Index \t Data " << endl; 
	
	while(count <= stop  ) {
		tmpData = input.read();
		if(count >= start && count < stop) {
			outFile << " \t"<< count <<":\t" << tmpData << endl;
		}
		count++;
	}
	
	outFile.close();
	sc_stop();
}
