/** ***************************************************************** 
 
 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

 This file implemenst ptolemy_sc_main to cosimulate with ADS-Ptolemy
*********************************************************************/

#include <systemc.h>
#include "PT_SC_SineGen.hxx"
#include "SystemCPtolemyInterface_PT_SC_SineGen.hxx"

void ptolemy_sc_main(int argc, char * argv[], SystemCPtolemyInterface_PT_SC_SineGen & p){
	
	sc_fifo<double> sc2pt;

    PT_SC_SineGen source("Source");

	p.output(sc2pt);
	source.output(sc2pt);

	/// Assign the parameter values from PtolemyInterface

	source.RadiansPerSample = p.getDoubleParamValue(p.RadiansPerSample); 
	source.InitialRadians = p.getDoubleParamValue(p.InitialRadians);


sc_start(-1);
}
