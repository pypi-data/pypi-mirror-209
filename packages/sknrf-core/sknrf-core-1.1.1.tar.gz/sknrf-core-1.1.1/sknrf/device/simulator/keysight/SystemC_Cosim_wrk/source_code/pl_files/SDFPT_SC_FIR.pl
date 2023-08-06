defstar {
  name {PT_SC_FIR}
  derivedFrom { SystemC_Cosim }
  domain {SDF}

  desc { FIR filter }
  explanation { A SystemC Cosim Star. Provides Cosim with a SystemC FIR written in RTL style.
  The FIR SystemC code is from OSCI SystemC 2.1 examples. Number of Taps in this example is 
  fixed and is equal to 16.
  }
  
  author { Junaid A. Khan }
  
  copyright {
	Copyright (c) Agilent Technologies 2007
	All rights reserved.
  }
  
  vendor { AgilentEEsof }
  
  location { SystemC }
	
  
  input {
    name{input}
    type{int}
  }
  
  output {
    name{output}
    type{int}
  }
  
  defstate {
    name {Taps}
    range { [-inf:inf) }
    type {intarray}
    default {
    "-6 -4 13 16 -18 -41 23 154 222 154 23 -41 -18 16 13 -4"
    }
    attributes { A_SETTABLE|A_NONCONSTANT };
    desc { FIR tap values. }
   }

  constructor {
     SystemC_Executable.setInitValue("ptscrtlfir");
  }
 
  method { 
   name {sc_setup}
   access{protected}
   arglist{"(void)"}
   code  {
    if (Taps.size() != 16 ){
     Error::abortRun(*this,"Number of Taps for this 16 tap FIR must be 16.");
     }
   }
 }

}
