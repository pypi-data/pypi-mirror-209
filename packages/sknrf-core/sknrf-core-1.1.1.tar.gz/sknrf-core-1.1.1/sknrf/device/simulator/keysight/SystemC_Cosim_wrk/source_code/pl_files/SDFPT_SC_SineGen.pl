defstar {
  
  name {PT_SC_SineGen}
  
  derivedFrom { SystemC_Cosim }
  
  domain {SDF}
  
  author { Junaid A. Khan }
  
  explanation {A SystemC Cosim Star. Provides Cosim with a SystemC sine wave generator.}
  
  copyright {
  Copyright (c) Agilent Technologies 2007.
  All rights reserved.
  }
  
  vendor { AgilentEEsof }
  
  location { SystemC }
  
  defstate {
     name { RadiansPerSample }
     range { (-inf:inf) }
     type { float }
     default { "pi/50" }
     desc { radians per sample }
  }
  
  defstate {
	name { InitialRadians }
	range { (-inf:inf) }
    type { float }
    default { 0 }
    desc { initial phase in radians }
  }
  
  output {
    name { output }
    type { float }
    desc { output signal }
  }

  constructor {
    SystemC_Executable.setInitValue("ptscsinegen");
  }
}
