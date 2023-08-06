.. sknrf documentation introduction file

..  figure:: ../_images/PNG/sknrf_logo.png
    :width: 500 pt
    :align: center

Build & Distribute
==================

Build
-----


Build C++ Libraries
~~~~~~~~~~~~~~~~~~~

Build C++ ibraries and save in $CONDA_PREFIX/sknrf/lib directory.

.. code-block:: bash

    >>> python setup.py build_cpp --force

Options:

    --force      -f  forcibly build everything.
    --spec       -s  apply a specific QMAKESPEC to Qt libraries.
    --debug      -d  build with debugging information.


Build Python
~~~~~~~~~~~~

Build Source Distribution and save in ./build directory.

.. code-block:: bash

    >>> python setup.py build_py


Build Doc
~~~~~~~~~

Build HTML Documentation and save in ./doc/build/html directory.

.. code-block:: bash

    >>> python setup.py build_doc --apidoc --html --imagehtml

Options:

    --clean         -f  clean the documentation folder.
    --apidoc        -a  build programmable api.
    --html          -w  build html documentation.
    --imagehtml     -i  build html images.


Install
-------

Install Build
~~~~~~~~~~~~~

Install latest build from ./build directory in python packages.

.. code-block:: bash

    >>> python setup.py install

Install Default Config
~~~~~~~~~~~~~~~~~~~~~~

Install application config data from ./sknrf/data

.. code-block:: bash

    >>> python setup.py install_config


Upload Build
~~~~~~~~~~~~

Upload latest build from ./build/lib directory.

.. code-block:: bash

    >>> python setup.py upload --install-dir=BuildDestination


Upload Docs
~~~~~~~~~~~

Upload latest doc from ./doc/build/html directory.

.. code-block:: bash

    >>> python setup.py upload_docs --install-dir=DocDestination

