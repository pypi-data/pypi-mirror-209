defstar {
  
  name {PT_SC_UpSample}
  
  derivedFrom { SystemC_Cosim }
  
  domain {SDF}

  desc { Data Up Sampler }
  
  explanation { A SystemC Cosim Star. Provides Cosim with a SystemC UpSampler.
Upsample by a given "factor" (default 2), giving inserted samples the
value "fill" (default 0.0).  The "phase" parameter (default 0) tells where
to put the sample in an output block.  A "phase" of 0 says to output
the input sample first followed by the inserted samples. The maximum
"phase" is "factor" - 1.  
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
    type{float}
  }
  
  output {
    name{output}
    type{float}
  }
  
  defstate {
    name {Factor}
    range { [1:inf) }
    type {int}
    default {2}
    desc { number of samples produced }
  }
  
  defstate {
    name {Phase}
    range { [0:Factor-1] }
    type {int}
    default {0}
    desc { where to put the input in the output block }
  }
  
  defstate {
    name {Fill}
    range { (-inf:inf) }
    type {float}
    default {0.0}
    desc { value to fill the output block }
  }

  constructor {
   SystemC_Executable.setInitValue("ptscupsample");
  }
 
  method{ 
   name {sc_setup}
   access{protected}
   arglist{"(void)"}
   code  {
    if (Factor <= 0) {
      Error::abortRun(*this,"Value of Factor must be greater than 0");
    }
    else
      output.setSDFParams(int(Factor),int(Factor)-1);
      
    if (Factor > 0 && Phase >= Factor)
      Error::abortRun(*this,"Value of Phase must be less than Factor");
    if (Phase < 0)
      Error::abortRun(*this,"Value of Phase must be greater than 0");

   }
 } 
  
}

