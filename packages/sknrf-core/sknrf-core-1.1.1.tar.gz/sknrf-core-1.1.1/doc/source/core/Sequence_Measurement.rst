
Sequencer Menu
==============

The sequencer provides a way to perform automated "drag-and-drop" parametric sweeps without programming:

..  figure:: ../_images/PNG/sequencer_menu.png
    :width: 100 %
    :align: center

    The Sequencer Menu.

The Sequencer Menu consists of **three colums**:

    1. The :py:class:`ActionTreeView <sknrf.view.desktop.sequencer.widgets.ActionTreeView>`: A tree of top-level modules that export a sequencer interface.
    2. The :py:class:`SequencerView <sknrf.view.desktop.sequencer.menu.SequencerView>`: A top-to-bottom graphical representation of the measurement sequence.
    3. THe :py:class:`PreviewFrame <sknrf.view.desktop.preview.frame>`: Preview plots of the measurement stimulus and response.

An automated power sweep of **a_1** is described below:

.. raw:: html

    <div class="container mt-3">
        <div class="row" align="center">
            <div class="col-sm-9">
                <div id="sequencerCarousel" class="carousel slide" data-ride="carousel" data-interval="false">

                    <!-- Wrapper for slides -->
                    <div class="carousel-inner">
                        <div class="item active"><img src="../_images/PNG/sequencer/sequencer0.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer1.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer2.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer3.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer4.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer5.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer6.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer7.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer8.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer9.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer10.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer12.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer13.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer14.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer15.png" width="100%"></div>
                        <div class="item"><img src="../_images/PNG/sequencer/sequencer16.png" width="100%"></div>
                    </div>

                    <!-- Left and right controls -->
                    <a class="left carousel-control" href="#sequencerCarousel" role="button" data-slide="prev">
                        <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                        <span class="sr-only">Previous</span>
                    </a>
                    <a class="right carousel-control" href="#sequencerCarousel" role="button" data-slide="next">
                        <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                        <span class="sr-only">Next</span>
                    </a>

                    <!-- Indicators -->
                    <ol class="carousel-indicators">
                        <li data-target="#sequencerCarousel" data-slide-to="0" class="active"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="1"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="2"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="3"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="4"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="5"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="6"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="7"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="8"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="9"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="10"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="11"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="12"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="13"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="14"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="15"></li>
                        <li data-target="#sequencerCarousel" data-slide-to="16"></li>
                    </ol>
                </div>
            </div>
        </div>
    </div>

* Press **New** to clear an exisiting test sequence.

    * Import **sweep.real** module

        * Define a **linear_sweep** variable

            * Accept the default sweep settings.
            * Preview plot the sweep plan.

    * Import **sequencer.measure** module

        * Define a **swept_measurement** variable

            * Accept the default measurement settings.
            * Add the **linear_sweep** using the **add_sweep** method.

                * **sweep_id**: "A_SET"
                * **port_index**: 1
                * **harm_index**: 1
                * **sweep_plan**: **linear_sweep**

            * Add a swept measurement using the **swept_measurement** method.

* Press **Code** to generate the Python script (Press close when done).
* Press **Run** to run the measurement sweep.
* Preview plot the **b_2** output response.


You can always copy the code generated by the sequencer into a Python script.