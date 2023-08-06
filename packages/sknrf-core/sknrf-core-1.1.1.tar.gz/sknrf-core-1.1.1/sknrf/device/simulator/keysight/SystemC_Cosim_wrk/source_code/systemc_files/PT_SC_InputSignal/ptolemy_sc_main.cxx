/** ***************************************************************** 
 
 Copyright (c) 2007 Agilent Technologies Inc. All rights reserved.
 @author Junaid A. Khan

 This file implemenst ptolemy_sc_main to cosimulate with ADS-Ptolemy
*********************************************************************/

#include <systemc.h>
#include "PT_SC_Noise.hxx"
#include "PT_SC_InputSignal.hxx"
#include "PT_SC_Adder.hxx"
#include "SystemCPtolemyInterface_PT_SC_InputSignal.hxx"


/** ****************************************
Top level SC_MODULE that will be instanciated
inside ptolemy_sc_main
*******************************************/

SC_MODULE(PT_SC_InputSignalTop) {
	
	sc_fifo_out<double> outputSignal;
	sc_fifo_in<double>  inputFreq;
	sc_fifo_in<double>  inputMagnitude;
	sc_fifo_in<double>  inputNoiseMag;

	
	PT_SC_InputSignal *input;
	PT_SC_Noise *noise;
	PT_SC_Adder *adder;

	sc_fifo<double> adderin1;
	sc_fifo<double> adderin2;


	double arg;
	SC_CTOR(PT_SC_InputSignalTop) {

		input = new PT_SC_InputSignal("InputSignal");
	    input->inputFreq(inputFreq);
		input->inputMagnitude(inputMagnitude);
		input->outputSignal(adderin1);

		noise = new PT_SC_Noise("NoiseSignal");
		noise->inputNoiseMag(inputNoiseMag);
		noise->outputNoise(adderin2);

		adder = new PT_SC_Adder("SignalAdder");
		adder->input1(adderin1);
		adder->input2(adderin2);
		adder->output(outputSignal);
	}
};

 /*****************************************/

void ptolemy_sc_main(int argc, char * argv[], SystemCPtolemyInterface_PT_SC_InputSignal & p){
	
	sc_fifo<double> sc2ptout;
	
	sc_fifo<double> pt2scfreq;
	sc_fifo<double> pt2scmag;
	sc_fifo<double> pt2scnoise;

	PT_SC_InputSignalTop topSignalGen("SignalGenerator");

	p.inputFreq(pt2scfreq);
	p.inputNoiseMag(pt2scnoise);
	p.inputMagnitude(pt2scmag);
	p.outputSignal(sc2ptout);

	topSignalGen.inputFreq(pt2scfreq);
	topSignalGen.inputNoiseMag(pt2scnoise);
	topSignalGen.inputMagnitude(pt2scmag);
	topSignalGen.outputSignal(sc2ptout);

sc_start(-1);
}
