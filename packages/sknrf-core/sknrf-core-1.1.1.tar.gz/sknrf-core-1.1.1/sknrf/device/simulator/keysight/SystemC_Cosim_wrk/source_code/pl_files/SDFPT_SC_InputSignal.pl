defstar {
  name {PT_SC_InputSignal}
  derivedFrom { SystemC_Cosim }
  domain {SDF}
  
  desc { Input Signal Generator with added Uniform Noise }
  explanation { A SystemC Cosim Star. Provides Cosim with a SystemC signal generator.
SystemC generates a signal of magnitude inputMagnitude (mV)
with inputFreq (MHz) added with uniform random noise of inputNoiseMag (uV) .  
  }
  
  author { Junaid A. Khan }
  
  copyright {
Copyright (c) Agilent Technologies 2007
All rights reserved.
  }
  
  vendor { AgilentEEsof }
  
  location { SystemC }
    
  input {
	name {inputFreq}
	type{float}
	desc{Input Signal Frequency in MHz}
  }
  
  input {
	name {inputNoiseMag}
	type{float}
	desc{Input Noise Magnitude in uV }
  }
  
  input {
	name {inputMagnitude}
	type{float}
	desc{Input Signal Magnitude in  mV}
  }
  
  output {
	name {outputSignal}
	type {float}
	desc {Output Signal in V}
  }
  
 constructor {
   SystemC_Executable.setInitValue("ptscsignalsource");
 } 
  
}

