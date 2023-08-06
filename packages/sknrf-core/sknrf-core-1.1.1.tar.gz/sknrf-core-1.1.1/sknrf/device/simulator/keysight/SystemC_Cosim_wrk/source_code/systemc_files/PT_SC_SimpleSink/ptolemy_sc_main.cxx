/** ***************************************************************** 
 
 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

 This file implemenst ptolemy_sc_main to cosimulate with ADS-Ptolemy
*********************************************************************/


#include <systemc.h>
#include "PT_SC_SimpleSink.hxx"
#include "SystemCPtolemyInterface_PT_SC_SimpleSink.hxx"

void ptolemy_sc_main(int argc, char * argv[], SystemCPtolemyInterface_PT_SC_SimpleSink & p){
	
	sc_fifo<int> pt2sc;
        PT_SC_SimpleSink sink("Sink");

/// Parsing argv to obatain output file name specified in ADS-Ptolemy Schematic
	for(int i= 0; i < argc; i++)
	{
		if ( strcmp(argv[i],"-f") ) {
			i++;
			if(i>=argc){
				cout << "\n Filname is not specified; usin default file name\n";
				break;
			}
			strcpy (sink.outFileName,argv[i+1]);
			break;
		}
	}

	sink.stop = p.getIntegerParamValue(p.Stop);
	sink.start = p.getIntegerParamValue(p.Start);

	p.input(pt2sc);
	sink.input(pt2sc);



sc_start(-1);
}
