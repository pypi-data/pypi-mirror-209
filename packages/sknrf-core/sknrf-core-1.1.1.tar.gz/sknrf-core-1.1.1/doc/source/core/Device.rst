Devices
=======

Concepts
~~~~~~~~

Mixed Signals
-------------

Mixed-signals describe nonlinear time-variant systems:

    - Nonlinear-Systems: Produce *nonlinear distortion*, described by *analog signals* w.r.t freq :math:`X(f)`
    - Time-Variant Systems: Produce *memory*, described by *digital signals* w.r.t time :math:`x(t)`
    - Time-Variant Nonlinear-Systems: Require *envelope signals* w.r.t time, freq :math:`x(t, f)`

.. raw:: html

    <img src="./../_images/PNG/envelope_simulation.png"/

All measurements are captured as envelope signals Once the signal is captured, you can use various Fourier Transforms
to convert to other relatable signals.

Signal Transforms
-----------------

.. raw:: html

    <div class="table-responsive">
      <table class="table colwidths-given align-default table table-sm table-bordered table-striped table-hover">
        <caption><center>Signal Transforms</center></caption>
        <colgroup>
          <col style="width: 20%">
          <col style="width: 20%">
          <col style="width: 20%">
          <col style="width: 20%">
          <col style="width: 20%">
        </colgroup>
        <thead class="thead-dark">
          <tr>
            <th scope="col">To \ From:</th>
            <th scope="col" style="text-align:center">Envelope</th>
            <th scope="col" style="text-align:center">Frequency</th>
            <th scope="col" style="text-align:center">Time</th>
            <th scope="col" style="text-align:center">Switching</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row" style="text-align:center">Envelope</th>
            <td><img style="height: 15pt" src="../_images/PNG/green/32/form_oval.png"/>&nbsp=&nbsptf.tf(&nbsp<img style="height: 15pt" src="../_images/PNG/green/32/form_oval.png"/>&nbsp)</td>
            <td><img style="height: 15pt" src="../_images/PNG/green/32/form_oval.png"/>&nbsp=&nbspff.tf(&nbsp<img style="height: 15pt" src="../_images/PNG/red/32/form_oval.png"/>&nbsp)</td>
            <td><img style="height: 15pt" src="../_images/PNG/green/32/form_oval.png"/>&nbsp=&nbsptt.tf(&nbsp<img style="height: 15pt" src="../_images/PNG/blue/32/form_oval.png"/>&nbsp)</td>
            <td><img style="height: 15pt" src="../_images/PNG/green/32/form_oval.png"/>&nbsp=&nbspft.tf(&nbsp<img style="height: 15pt" src="../_images/PNG/violet/32/form_oval.png"/>&nbsp)</td>
          </tr>
          <tr>
            <th scope="row" style="text-align:center">Frequency</th>
            <td><img style="height: 15pt" src="../_images/PNG/red/32/form_oval.png"/>&nbsp=&nbspff.ff(&nbsp<img style="height: 15pt" src="../_images/PNG/green/32/form_oval.png"/>&nbsp)</td>
            <td><img style="height: 15pt" src="../_images/PNG/red/32/form_oval.png"/>&nbsp=&nbspff.ff(&nbsp<img style="height: 15pt" src="../_images/PNG/red/32/form_oval.png"/>&nbsp)</td>
            <td><img style="height: 15pt" src="../_images/PNG/red/32/form_oval.png"/>&nbsp=&nbspff.ff(&nbsp<img style="height: 15pt" src="../_images/PNG/blue/32/form_oval.png"/>&nbsp)</td>
            <td><img style="height: 15pt" src="../_images/PNG/red/32/form_oval.png"/>&nbsp=&nbspff.ff(&nbsp<img style="height: 15pt" src="../_images/PNG/violet/32/form_oval.png"/>&nbsp)</td>
          </tr>
          <tr>
            <th scope="row" style="text-align:center">Time</th>
            <td><img style="height: 15pt" src="../_images/PNG/blue/32/form_oval.png"/>&nbsp=&nbsptt.tt(&nbsp<img style="height: 15pt" src="../_images/PNG/green/32/form_oval.png"/>&nbsp)</td>
            <td><img style="height: 15pt" src="../_images/PNG/blue/32/form_oval.png"/>&nbsp=&nbsptt.tt(&nbsp<img style="height: 15pt" src="../_images/PNG/red/32/form_oval.png"/>&nbsp)</td>
            <td><img style="height: 15pt" src="../_images/PNG/blue/32/form_oval.png"/>&nbsp=&nbsptt.tt(&nbsp<img style="height: 15pt" src="../_images/PNG/blue/32/form_oval.png"/>&nbsp)</td>
            <td><img style="height: 15pt" src="../_images/PNG/blue/32/form_oval.png"/>&nbsp=&nbsptt.tt(&nbsp<img style="height: 15pt" src="../_images/PNG/violet/32/form_oval.png"/>&nbsp)</td>
          </tr>
          <tr>
            <th scope="row" style="text-align:center">Switching</th>
            <td><img style="height: 15pt" src="../_images/PNG/violet/32/form_oval.png"/>&nbsp=&nbspft.ft(&nbsp<img style="height: 15pt" src="../_images/PNG/green/32/form_oval.png"/>&nbsp)</td>
            <td><img style="height: 15pt" src="../_images/PNG/violet/32/form_oval.png"/>&nbsp=&nbspft.ft(&nbsp<img style="height: 15pt" src="../_images/PNG/red/32/form_oval.png"/>&nbsp)</td>
            <td><img style="height: 15pt" src="../_images/PNG/violet/32/form_oval.png"/>&nbsp=&nbspft.ft(&nbsp<img style="height: 15pt" src="../_images/PNG/blue/32/form_oval.png"/>&nbsp)</td>
            <td><img style="height: 15pt" src="../_images/PNG/violet/32/form_oval.png"/>&nbsp=&nbspft.ft(&nbsp<img style="height: 15pt" src="../_images/PNG/violet/32/form_oval.png"/>&nbsp)</td>
          </tr>
        </tbody>
      </table>
    </div>

The signals describe a nonlinear time-variant system as follows:

    * **Envelope**: Raw data capture.
    * **Frequency**: Frequency Spectrum waveform centered around each harmonic of a carrier frequency.
    * **Time**: Sub-Sampled waveform where each digital sample (:math:`\tau_t`) contains analog sub-samples (:math:`\tau_f`).
    * **Switching**: Analog switching behaviour computed over a slice of bandwidth (BW).

Units
-----

To simplify data storage and manipulation, each mixed-signal is recorded in **base-linear** units:

-  Voltage: [:math:`V`]
-  Current: [:math:`A`]
-  Impedance: [:math:`\Omega`]
-  Power [:math:`\sqrt{W}`]

This ensures that all variables can be converted from base linear units to decibels (dB) using :py:class:`rW2dBW <sknrf.utilities.rf.rW2dBW>`

Objects
-------

An **Object** (such as an device) contains properties (such as signals). An object may also control the display,
sweep limits, and optimization limits of each property using the following metadata:

    1. :code:`obj.info` of type :py:class:`AttributeInfo <sknrf.utilities.numeric.AttributeInfo>`, which contains:
            * :py:class:`Info <sknrf.utilities.numeric.Info>` metadata for each object property.
    2. :code:`obj.__info__()`, a magic method that dynamically initializes the :code:`self.info` metadata.

Devices
-------

A **Device** :py:class:`AbstractDevice <sknrf.device.base.AbstractDevice>` is an **Object** that contains:

    1. :code:`DeviceClass.firmware_map`, a static dictionary that contains supported device firmware information.
    2. :code:`device.handles`, a dictionary of device handles (any type) that *uniquely* describes a remote connection to the physical device(s).
    3. :code:`device.connect_handles()`, connects the device and stores device references in :code:`self.handles`.
    4. :code:`device.preset()`, presets the device each time a *unique* connection is made.
    5. :code:`device.disconnect_handles()`, disconnects the device and removes device references from :code:`self.handles`.
    6. :code:`device.info` contains display, sweep limit, and optimization limit meta-data.

Programming
~~~~~~~~~~~

Adding a Device Driver
----------------------

1. Select the device(s) that best describe the instrument you want to control. Here are some common examples:

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

2. Select the device modulation complexity. For example, an RFSource can be inherit the following classes:

    a. :py:class:`NoRFSource (easy) <sknrf.device.instrument.rfsource.base.NoRFSource>`
    b. :py:class:`NoRFSourcePulsed (harder) <sknrf.device.instrument.rfsource.base.NoRFSourcePulsed>`
    c. :py:class:`NoRFSourceModulated (hard) <sknrf.device.instrument.rfsource.base.NoRFSourceModulated>`

3. Write the driver.

.. tip::
    It's usually best to copy from previous drivers.

.. tip::
    Store configuration data in a config file.

.. tip::
    Complex instruments may require multiple drivers. Some high-end VNAs may contain:

        * LF Source
        * LF Receiver
        * RF Source
        * RF Receiver

    Avoid repetition by programming *common* functionality in shared functions, such as:

        * preset()
        * arm()
        * trigger()

.. warning::::
    Realtime parametric sweeps reduce I/O bottlenecks by serializing a sweep into a really long time-domain signal.
    This implies that a signal :math:`x(t, f)` does not always contain the same dimensions along the time-axis.
    Avoid referencing the following time-domain settings in the device drivers:

        * Settings().time
        * Settings().t_stop
        * Settings().t_points

4. Register the driver by:

    a. Place the source code file in the following search path:

    .. code-block:: bash

        sknrf/device/instrument/<device_type>/*

    b. Place the config file in the following search path:

    .. code-block:: bash

        sknrf/data/config/device/instrument/<device_type>/*

5. Test the driver as follows:

    .. raw:: html

        <div class="container mt-3">
            <div class="row" align="center">
                <div class="col-sm-9">
                    <div id="testDeviceCarousel" class="carousel slide" data-ride="carousel" data-interval="false">

                        <!-- Wrapper for slides -->
                        <div class="carousel-inner">
                            <div class="item active"><img src="../_images/PNG/load_device/load_device0.png" width="100%"></div>
                            <div class="item"><img src="../_images/PNG/load_device/load_device1.png" width="100%"></div>
                            <div class="item"><img src="../_images/PNG/load_device/load_device2.png" width="100%"></div>
                            <div class="item"><img src="../_images/PNG/load_device/load_device3.png" width="100%"></div>
                            <div class="item"><img src="../_images/PNG/load_device/load_device4.png" width="100%"></div>
                            <div class="item"><img src="../_images/PNG/load_device/load_device5.png" width="100%"></div>
                            <div class="item"><img src="../_images/PNG/load_device/load_device6.png" width="100%"></div>
                        </div>

                        <!-- Left and right controls -->
                        <a class="left carousel-control" href="#testDeviceCarousel" role="button" data-slide="prev">
                            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                            <span class="sr-only">Previous</span>
                        </a>
                        <a class="right carousel-control" href="#testDeviceCarousel" role="button" data-slide="next">
                            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                            <span class="sr-only">Next</span>
                        </a>

                        <!-- Indicators -->
                        <ol class="carousel-indicators">
                            <li data-target="#testDeviceCarousel" data-slide-to="0" class="active"></li>
                            <li data-target="#testDeviceCarousel" data-slide-to="1"></li>
                            <li data-target="#testDeviceCarousel" data-slide-to="2"></li>
                            <li data-target="#testDeviceCarousel" data-slide-to="3"></li>
                            <li data-target="#testDeviceCarousel" data-slide-to="4"></li>
                            <li data-target="#testDeviceCarousel" data-slide-to="5"></li>
                            <li data-target="#testDeviceCarousel" data-slide-to="6"></li>
                        </ol>
                    </div>
                </div>
            </div>
        </div>

    * Select the driver

        * Modify the Address
        * Verify the firmware versions match
    * Test the driver
    * Load the driver
    * Run a Single Measurement
    * Plot the results.


API
---

The following is a minimal example of how to connect to an instrument:

.. code-block:: python

    from sknrf.device.base import AbstractDevice
    from sknrf.device.instrument.lfsource.base import NoLFSource

    AbstractModel.init()
    dev = NoLFSource()
