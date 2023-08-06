defstar {
  
  name {PT_SC_SimpleSink}
  
  derivedFrom { SystemC_CosimSink }
  
  domain {SDF}
  
  author { Junaid A. Khan }
  
  explanation {A SystemC Cosim Star. Provides Cosim with a SystemC Simple Sink.}
  
  copyright {
  Copyright (c) Agilent Technologies 2007.
  All rights reserved.
  }
  
  vendor { AgilentEEsof }
  
  location { SystemC }
  
  defstate {
     name { Start }
     range { (0:inf) }
     type { int }
     default { 0 }
     desc { Starting index for sample collection. }
  }
  
  defstate {
	name { Stop }
	range { (0:inf) }
    type { int }
    default { 100 }
    desc { initial phase in radians }
  }
  
  input {
    name { input }
    type { int }
    desc { Input signal }
  }

  constructor {
    SystemC_Executable.setInitValue("ptscsimplesink");
  }
  
  method{ 
	name {sc_setup}
	access{protected}
	arglist{"(void)"}
	code  {
		if (Start < 0)
		  Error::abortRun(*this, "The value of Start must be greater than or equal to 0.");
		if (Stop < Start)
		  Error::abortRun(*this, "The value of Stop cannot be less than Start");
	}
 }
}
