Single Measurement
==================

Main Menu
~~~~~~~~~

Assuming all devices are connected, a two-port system is modeled as follows:

..  figure:: ../_images/PNG/setup_type_ltf.png
    :width: 50 %
    :align: center

    A 2-Port System with Unknown DUT.

The Main Menu summarizes the test-bench as shown below:

..  figure:: ../_images/PNG/main_menu_view.png
    :width: 100 %
    :align: center

    The 2-port System Dashboard Representation

The Main Menu consists of two-primary elements:

    1. The Sidebar
    2. The Instrument Manager

Sidebar
-------

The Sidebar is a multi-tab window that can be customized based on the desired application. The Main Menu defaults to the
Main tab.

..  figure:: ../_images/PNG/main_tab.png
    :width: 100 %
    :align: center

Start by configuring the *global* System Settings in the sidebar by specifying:

    * Frequency Sweep
        * :code:`Settings().f_0`: The fundamental carrier frequency.
        * :code:`Settings().num_harmonics`: The number of harmonics frequencies.
    * Time Sweep
        * :code:`Settings().t_{stop}`: the measurement period.
        * :code:`Settings().t_{step}`: the measurement time-step.
    * Trigger
        * :code:`Settings().trigger_device`: the trigger output device type.
        * :code:`Settings().trigger_port`: the trigger output device port.
    * Datagroup
        * :code:`Settings().datagroup`: The name of the database file (default **Single.h5**).
        * :code:`Settings().trigger_port`: The name of a node in a database file (default **Default**).

You can specify additional global variables:

    * In the :code:`sknrf.yml` config file before runtime.
    * In the Settings Menu during runtime.

Instrument Manager
------------------

The Instrument Manager consists of:

    * :code:`Settings().num_ports + 1` ports
        * Port 0 is a reserved calibration reference port.
    * :code:`Settings().num_duts` DUTs
    * The aux devices consisting of non-compatible instruments:
        * Power Meter
        * Spectrum Analyzer
        * Vector Network Analyzer

Ports
-----

The number of ports is configured in  :code:`sknrf.yml` and is available at runtime in :code:`Settings().num_ports`.
Each measurement port is represented by a column in the Instrument Manager.

..  figure:: ../_images/PNG/instrument_manager_port.png
    :width: 100 %
    :align: center

A **Port** :py:class:`PortModel <sknrf.model.device.PortModel>` a collection of devices that can be connected to a
measurement port:

    1. :code:`port.lfsource`, a low-frequency signal source that *sets* :math:`v(t, f)`.
    2. :code:`port.lfreceiver`, a low-frequency signal receiver that *gets*  :math:`v(t, f)` and :math:`i(t, f)`.
    3. :code:`port.lfztuner`, a low-frequency impedance controller that *sets* and *gets*  :math:`z_p(t, f)`
    4. :code:`port.rfsource`, a high-frequency signal source that *sets* :math:`a_p(t, f)`.
    5. :code:`port.rfreceiver`, a high-frequency signal receiver that *gets* :math:`a_p(t, f)` and :math:`b_p(t, f)`.
    6. :code:`port.rfztuner`, a high-frequency impedance controller that *sets* and *gets* :math:`\gamma_p(t, f)`.

Each measurement port provides a Thevenin Equivalent at Low-Frequency (LF) and High-Frequency (HF). Thus the following
equations fully describe the inputs and outputs of a port:

**VIZ->BAG**

..  figure:: ../_images/PNG/NVNA_meas_AB.png
    :width: 100 %
    :align: center

.. math::
   :nowrap:

    \begin{eqnarray}
        B_p & = & \frac{1}{2 \sqrt{ \Re Z_p }} \left( V - Z_p^*I \right) \\
        A_p & = & \frac{1}{2 \sqrt{ \Re Z_p }} \left( V + Z_pI \right) \\
        \Gamma_p & = & \frac{Z_p - Z_0}{Z_p + Z_0} \\
    \end{eqnarray}

**BAG->VIZ**

..  figure:: ../_images/PNG/NVNA_meas_VI.png
    :width: 100 %
    :align: center

.. math::
   :nowrap:

    \begin{eqnarray}
        V & = & \frac{1}{\sqrt{ \Re Z_p }} * \left( Z_p^*a + Z_pb \right) \\
        I & = & \frac{1}{\sqrt{ \Re Z_p }} * \left( a - b \right) \\
        Z_p & = & z0 \frac{1 + \Gamma_p}{-\Gamma_p + 1} \\
    \end{eqnarray}

    where,

.. math::
   :nowrap:

    \begin{eqnarray}
        V & = & \mathcal{F} \left( v(t, f) \right) \text{w.r.t } t\\
        I & = & \mathcal{F} \left( i(t, f) \right) \text{w.r.t } t\\
        Z_p & = & \mathcal{F} \left( z_p(t, f) \right) \text{w.r.t } t\\
        B_p & = & \mathcal{F} \left( v(t, f) \right) \text{w.r.t } t\\
        A_p & = & \mathcal{F} \left( i(t, f) \right) \text{w.r.t } t\\
        \Gamma_p & = & \mathcal{F} \left( \gamma_p(t, f) \right) \text{w.r.t } t\\
    \end{eqnarray}

These raw waveforms have the following meaning:

    * :math:`v(t, f)`: The input voltage (default :math:`0.0`).
    * :math:`i(t, f)`: The output current (default :math:`0.0`).
    * :math:`z(t, f)`: The port termination impedance (default :math:`z_0 = 50.0`)
    * :math:`b_p(t, f)`: The output (reflected) power-wave (default :math:`0.0`).
    * :math:`a_p(t, f)`: The input (incident) power-wave (default :math:`0.0`).
    * :math:`\gamma_p(t, f)`: The port reflection coefficient (default :math:`0.0`).

Since each of these waveforms has a *default value*, we need only connect an instrument when we know that
the DUT does not meet these assumptions:

    * Devices with direct access to power and ground do not require a :code:`port.lfztuner`.
    * Devices matched to 50 Ohm do not require a :code:`port.rfztuner`.
    * Devices matched to 50 Ohm do not require a :code:`port.rfreceiver` that can measure :math:`a_p(t, f)`.
    * LF circuits do not require :code:`port.rfsource`, :code:`port.rfreceiver`, :code:`port.rfztuner`.
    * RF circuits do not require :code:`port.lfsource`, :code:`port.lfreceiver`, :code:`port.lfztuner`.

Supported Instruments
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <div class="row">
        <div class="col-sm-3">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title" style="font-size:17px">
                        <img src="../_images/PNG/white/32/lfsource.png" alt="LF Source" width="32pt" height="32pt" border="0">
                        <a class="reference internal" href="../developers/api/sknrf.device.instrument.lfsource.base.html#sknrf.device.instrument.lfsource.base.NoLFSource" title="sknrf.device.instrument.lfsource.base.NoLFSource"><code class="xref py py-class docutils literal notranslate"><span class="pre">LF Source</span></code></a>
                    </h2>
                </div>
                <div class="panel-body" style="font-size:14px">
                    <p>DC Supply</p>
                    <p>AWG</p>
                    <p>DAC</p>
                    <p>&nbsp;</p>
                    <p>&nbsp;</p>
                </div>
            </div>
        </div>
        <div class="col-sm-3">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title" style="font-size:17px">
                        <img src="../_images/PNG/white/32/lfreceiver.png" alt="LF Receiver" width="32pt" height="32pt" border="0">
                        <a class="reference internal" href="../developers/api/sknrf.device.instrument.lfreceiver.base.html#sknrf.device.instrument.lfreceiver.base.NoLFReceiver" title="sknrf.device.instrument.lfreceiver.base.NoLFReceiver"><code class="xref py py-class docutils literal notranslate"><span class="pre">LF Receiver</span></code></a>
                    </h2>
                </div>
                <div class="panel-body" style="font-size:14px">
                    <p>Multimeter</p>
                    <p>Oscilloscope</p>
                    <p>ADC</p>
                    <p>&nbsp;</p>
                    <p>&nbsp;</p>
                </div>
            </div>
        </div>
        <div class="col-sm-3">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title" style="font-size:17px">
                        <img src="../_images/PNG/white/32/lfztuner.png" alt="LF ZTuner" width="32pt" height="32pt" border="0">
                        <a class="reference internal" href="../developers/api/sknrf.device.instrument.lfztuner.base.html#sknrf.device.instrument.lfztuner.base.NoLFZTuner" title="sknrf.device.instrument.lfztuner.base.NoLFZTuner"><code class="xref py py-class docutils literal notranslate"><span class="pre">LF ZTuner</span></code></a>
                    </h2>
                </div>
                <div class="panel-body" style="font-size:14px">
                    <p>Open/Short Circuit</p>
                    <p>Varactor</p>
                    <p>Active Load</p>
                    <p>&nbsp;</p>
                    <p>&nbsp;</p>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-3">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title" style="font-size:17px">
                        <img src="../_images/PNG/white/32/rfsource.png" alt="RF Source" width="32pt" height="32pt" border="0">
                        <a class="reference internal" href="../developers/api/sknrf.device.instrument.rfsource.base.html#sknrf.device.instrument.rfsource.base.NoRFSource" title="sknrf.device.instrument.rfsource.base.NoRFSource"><code class="xref py py-class docutils literal notranslate"><span class="pre">RF Source</span></code></a>
                    </h2>
                </div>
                <div class="panel-body" style="font-size:14px">
                    <p>Signal Generator</p>
                    <p>VSG</p>
                    <p>AWG</p>
                    <p>Pulse Generator</p>
                    <p>SRD</p>
                </div>
            </div>
        </div>
        <div class="col-sm-3">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title" style="font-size:17px">
                        <img src="../_images/PNG/white/32/rfreceiver.png" alt="RF Receiver" width="32pt" height="32pt" border="0">
                        <a class="reference internal" href="../developers/api/sknrf.device.instrument.rfreceiver.base.html#sknrf.device.instrument.rfreceiver.base.NoRFReceiver" title="sknrf.device.instrument.rfreceiver.base.NoRFReceiver"><code class="xref py py-class docutils literal notranslate"><span class="pre">RF Receiver</span></code></a>
                    </h2>
                </div>
                <div class="panel-body" style="font-size:14px">
                    <p>VNA</p>
                    <p>VSA</p>
                    <p>Power-Meter</p>
                    <p>Oscilloscope</p>
                    <p>Sampling Scope</p>
                </div>
            </div>
        </div>
        <div class="col-sm-3">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title" style="font-size:17px">
                        <img src="../_images/PNG/white/32/rfztuner.png" alt="LF ZTuner" width="32pt" height="32pt" border="0">
                        <a class="reference internal" href="../developers/api/sknrf.device.instrument.rfztuner.base.html#sknrf.device.instrument.rfztuner.base.NoRFZTuner" title="sknrf.device.instrument.rfztuner.base.NoRFZTuner"><code class="xref py py-class docutils literal notranslate"><span class="pre">RF ZTuner</span></code></a>
                    </h2>
                </div>
                <div class="panel-body" style="font-size:14px">
                    <p>50 Ohms</p>
                    <p>Passive Load</p>
                    <p>Active Load</p>
                    <p>&nbsp;</p>
                    <p>&nbsp;</p>
                </div>
            </div>
        </div>
    </div>

The choice of :code:`port.rfreceiver` determines the trade-off between:

    * speed vs. accuracy
    * digital vs. analog
    * affordable vs. expensive

This architecture manage the trade-off between digital and analog verification:

    * **Oscilloscope**: Low-Cost, digitally sampled receiver in an embedded-device.
    * **(Sub)-Sampling Oscilloscope**: Mixed-Signal with a slow digital sample-rate and fast analog sample-rate.
    * **Network Analyzer**: High-Cost, high accuracy measurement for analog circuits in an R&D lab.

Auxiliary Port
~~~~~~~~~~~~~~

The following instruments (found in most labs) provide turn-key design verification, but result in significant
challenges due to low inter-operability. These instruments (and suggested alternatives) are:

    * **Power Meter (Anything Else)**
        * Calibrated to NIST standards, but are limited to scalar measurements.
        * Requires manual range adjustment to achieve accuracy
    * **Spectrum Analyzer (Signal Analyzer)**:
        * Scalar frequency swept measurements do not translate to the envelope domain.
        * A Signal Analyzer is a good alternative.
    * **3-Receiver VNA (4-Receiver VNA)**:
        * 3-Receiver VNAs use 12-Term error correction to extract S-Parameter models.
        * 4-Receiver VNAs use 8-Term (or 12-term error correction) to measrure reflectometry (o extract S-Parameter models).

Since these instruments are still common, the **Aux Port** provides a way to log these measurements:
