
.. sknrf documentation master file, created by
   sphinx-quickstart on Wed Dec 31 19:25:10 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

..  figure:: ./_images/PNG/sknrf_logo.png
    :width: 500 pt
    :align: center

.. raw:: html

    <div class="container">
        <div class="row" align="center">
            <div class="col-sm-2">
                <div class="panel-heading">
                    <h2 class="panel-title" style="font-size:20px">Source</h2>
                </div>
                <div class="panel-body" style="font-size:18px">
                    <a href="https://gitlab.com/scikit-nonlinear"><img src="./_images/PNG/black/64/github.png" class="img-circle" alt="Source" width="40%" height="40%"></a>
                </div>
            </div>
            <div class="col-sm-2">
                <div class="panel-heading">
                    <h2 class="panel-title" style="font-size:20px">Issue Tracker</h2>
                </div>
                <div class="panel-body" style="font-size:18px">
                    <a href="https://gitlab.com/groups/scikit-nonlinear/-/issues"><img src="./_images/PNG/black/64/jira.png" class="img-circle" alt="Issue Tracker" width="40%" height="40%"></a>
                </div>
            </div>
            <div class="col-sm-2">
                <div class="panel-heading">
                    <h2 class="panel-title" style="font-size:20px">Forum</h2>
                </div>
                <div class="panel-body" style="font-size:18px">
                    <a href="https://app.slack.com/client/TMZ7Q3JBE/CMZMFMXC0/details/info"><img src="./_images/PNG/black/64/slack.png" class="img-circle" alt="Forum" width="40%" height="40%"></a>
                </div>
            </div>
            <div class="col-sm-2">
                <div class="panel-heading">
                    <h2 class="panel-title" style="font-size:20px">Tutorial</h2>
                </div>
                <div class="panel-body" style="font-size:18px">
                    <a href="https://www.youtube.com"><img src="./_images/PNG/black/64/youtube.png" class="img-circle" alt="Tutorial" width="40%" height="40%"></a>
                </div>
            </div>
        </div>
    </div>

.. toctree::
    :titlesonly:
    :maxdepth: 2

    Installation<installation/Installation>
    Core<core/Core>
    Calibration<calibration/calibration>
    Developers<developers/Developers>
    sknrf<sknrf/sknrf>
    API<./api/modules>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Build Flow
==========

Building and Deploying Python code with native shared libraries
a continuously involving ordeal, hence I have provided the equivalent
CMake/Makefile command in comments to be relatable to C++. Internally
Cmake and Make are invoked. The build-flow currently uses setuptools,
which is deprecated in Python 3.12.

Install Dependencies
--------------------

See requirements.txt

Environment Variables
---------------------

.. raw:: html

   <table>
       <tr>
           <th> Variable </th>
           <th> Default Value </th>
           <th> Description </th>
       </tr>
       <tr>
           <td> SKNRF_DIR </td>
           <td> import site ; site.getsitepackages()[0] </td>
           <td> Python SKNRF Module Directory </td>
       </tr>
       <tr>
           <td> CONDA_PREFIX </td>
           <td> /usr/local </td>
           <td> C++ Sysroot </td>
       </tr>
       <tr>
           <td> VISA_LIB </td>
           <td> @py </td>
           <td> Visa Library Location </td>
       </tr>
   </table>

Release Build
-------------

.::

   sudo python3 setup.py clean                              # sudo make clean
   python3 setup.py config                                  # cmake ..
   python3 setup.py build                                   # make
   sudo python3 setup.py install                            # sudo make install

Example
-------

.::

   python3 ${SKNRF_DIR}/sknrf/main.py

Tests
-----

.::

   cd ${SKNRF_DIR}/sknrf ; nosetests --config=nose.cfg

Runtime Configuration
---------------------

`${SKNRF_DIR}/sknrf/sknrf.yml` contains runtime configuration settings. Beware of Environment Variables set in this file.

Measurement Architectures
=========================

.. raw:: html

    <div class="container">
        <div class="row" align="center">
            <div class="col-sm-9">
                <div id="myCarousel" class="carousel slide" data-ride="carousel" height="800">

                  <!-- Wrapper for slides -->
                  <div class="carousel-inner" role="listbox" align="center" height="350">
                    <div class="item active">
                      <img src="./_images/PNG/setup_type_d.png" alt="D-Type" width="66%">
                      <img src="./_images/PNG/mixed_signal_response_type_d.png" alt="DC Characterization" width="66%">
                      <div class="text-center">
                        <h3>D-Type</h3>
                        <p>DC Characteristics</p>
                      </div>
                    </div>
                    <div class="item" align="center">
                      <img src="./_images/PNG/setup_type_t.png" alt="T-Type" width="66%">
                      <img src="./_images/PNG/mixed_signal_response_type_t.png" alt="Time-Domain" width="66%">
                      <div class="text-center">
                        <h3>T-Type</h3>
                        <p>Time-Domain Envelope</p>
                      </div>
                    </div>
                    <div class="item" align="center">
                      <img src="./_images/PNG/setup_type_f.png" alt="F-Type" width="66%">
                      <img src="./_images/PNG/mixed_signal_response_type_f.png" alt="Frequency-Domain" width="66%">
                      <div class="text-center">
                        <h3>F-Type</h3>
                        <p>Frequency-Domain</p>
                      </div>
                    </div>
                    <div class="item" align="center">
                      <img src="./_images/PNG/setup_type_ltf.png" alt="LTF-Type" width="66%">
                      <img src="./_images/PNG/mixed_signal_response_type_ltf.png" alt="Envelope-Domain" width="66%">
                      <div class="text-center">
                        <h3>DTF-Type</h3>
                        <p>DC Characteristics, Time-Domain, Frequency-Domain</p>
                      </div>
                    </div>
                  </div>

                  <!-- Left and right controls -->
                  <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
                    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                  </a>
                  <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
                    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                  </a>
                  <!-- Indicators -->
                  <ol class="carousel-indicators">
                    <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                    <li data-target="#myCarousel" data-slide-to="1"></li>
                    <li data-target="#myCarousel" data-slide-to="2"></li>
                    <li data-target="#myCarousel" data-slide-to="3"></li>
                  </ol>
                </div>
            </div>
        </div>


        <div class="row">
            <div class="col-sm-3">
                <div class="panel panel-success">
                    <div class="panel-heading">
                        <h2 class="panel-title" style="font-size:17px">LF Source</h2>
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
                        <h2 class="panel-title" style="font-size:17px">LF Receiver</h2>
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
                        <h2 class="panel-title" style="font-size:17px">LF Impedance</h2>
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
                        <h2 class="panel-title" style="font-size:17px">RF Source</h2>
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
                        <h2 class="panel-title" style="font-size:17px">RF Receiver</h2>
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
                        <h2 class="panel-title" style="font-size:17px">RF Impedance</h2>
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
    </div>

Time/Frequency-Domain Characterization
======================================

.. raw:: html

    <img src="./_images/PNG/envelope_simulation.png"/  class="center">

Contributors
============

`Dylan T Bespalko <https://dylanbespalko.wixsite.com/dylanbespalko>`_.
