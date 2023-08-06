.. sknrf documentation introduction file

..  figure:: ../_images/PNG/sknrf_logo.png
    :width: 500 pt
    :align: center

Linux
=====

Build from Source
-----------------

Download the source code:

.. code-block:: bash

    eval $ENV
    git clone https://gitlab.com/scikit-nonlinear/sknrf-core.git
    cd ${HOME}/repos/sknrf-core
    git submodule sync
    git submodule update --init --recursive --remote


Build an install both the Python front-end and C++ back-end:

.. code-block:: bash

    python setup.py clean                         # make clean
    python setup.py config                        # configure
    python setup.py build                         # make
    python setup.py install                       # make install DESTDIR="${CONDA_PREFIX}"
    python setup.py develop                       # make install DESTDIR="${CONDA_PREFIX}" as symlink


Optionally, build (or rebuild) just the C++ back-end:

.. code-block:: bash

    rm -rf build ; mkdir build ; cd build         # make clean
    cmake -G"Ninja" ..                            # configure
    cmake --build .                               # make
    cmake --install . --prefix "${CONDA_PREFIX}"  # make install DESTDIR="${CONDA_PREFIX}"


Run the unit tests:

.. code-block:: bash

    nosetests --config=nose.cfg --with-coverage