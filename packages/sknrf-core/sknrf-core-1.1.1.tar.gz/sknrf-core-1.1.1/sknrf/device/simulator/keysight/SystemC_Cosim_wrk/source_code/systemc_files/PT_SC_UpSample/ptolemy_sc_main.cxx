/** ***************************************************************** 
 
 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

 This file implemenst ptolemy_sc_main to cosimulate with ADS-Ptolemy
*********************************************************************/


#include <systemc.h>
#include "PT_SC_UpSample.hxx"
#include "SystemCPtolemyInterface_PT_SC_UpSample.hxx"

void ptolemy_sc_main(int argc, char * argv[], SystemCPtolemyInterface_PT_SC_UpSample & p){
	
	sc_fifo<double> sc2pt;
	sc_fifo<double> pt2sc;

    PT_SC_UpSample upSample("UpSample");

	p.output(sc2pt);
	upSample.output(sc2pt);

	p.input(pt2sc);
	upSample.input(pt2sc);


	/// Reading Up-Sampler paramters specified in ADS-Ptolemy Schematic
	/// These includes Factor that specify the multi-rate property of the
	/// Up-Sampler

	upSample.Fill = p.getDoubleParamValue(p.Fill);
	upSample.Factor = p.getIntegerParamValue(p.Factor);
	upSample.Phase = p.getIntegerParamValue(p.Phase);
	

sc_start(-1);
}
