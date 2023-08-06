.. sknrf documentation introduction file

..  figure:: ../_images/PNG/sknrf_logo.png
    :width: 500 pt
    :align: center

Calibration
===========

Calibration techniques are a sequence of measurements that contains enough information to calculate an equivalent model
of part of the measurement system. This can be as simple as measuring the coupling factor of a coupler that is placed
between the DUT and the RF Receiver. The sequence of measurements used during calibration is often presented to the user
in a step-by-step procedure called a Calibration Wizard. The resulting measurements are used to train circuit model
coefficients that produce a Circuit Transform. The Circuit Transform can exist independently of the Calibration Wizard,
as it contains the equivalent model extracted from a previous calibration routine, or provided externally.

The following topics describe the procedure for running and developing calibration procedures.

..  toctree::
    :maxdepth: 1

    Calibration Wizards<Calibration_Wizards>
    Circuit Transforms<Circuit_Transforms>
