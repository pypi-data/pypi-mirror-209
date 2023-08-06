.. sknrf documentation useful_commands file

    
Useful Commands
===============


Build C++ Project
-----------------

.. code-block:: shell

    # Run Qt pre-compiler and generate makefile
    qmake [-o MAKEFILE_NAME] [PRO_FILE.pro]

    # Clean build files (*.o, *.moc)
    make clean

    # Compile C++ Code
    make

Convert QT Files to Python
--------------------------

.. code-block:: shell

    # Convert Qt resource file (*.qrc) to Python resource module (*_rc.py)
    pyside-rcc *.qrc -o *_rc.py

    # Convert Qt widget file (.ui) to Python widget module (*.py)
    pyside-uic *.ui -o *.py

Testing
-------

.. code-block:: shell

    # Run a Specific Test
    nosetests sknrf/utilities/tests/test_numeric.py

    # Run All tests (Except Device Drivers)
    nosetests --config=nose.cfg

    # Run All Tests With Coverage (Except Device Drivers)
    nosetests --config=nose.cfg --with-coverage --cover-package sknrf.model --cover-package sknrf.utilities

Generate Build
--------------

.. code-block:: shell

    python3.4 setup.py bdist_wheel

Install Python Package
----------------------

There are two Python Package Installers of Interest

conda (preferred)
Python/C/R/etc package installer.
Installs binaries.
Installed in the user's local directory.
Manages virtual environments.

pip
Python package installer.
Compiles everything from source.
Installed in the system global directory.
Does not manage virtual environments.

Python packages can be compiled as conda packages and installed using conda with conda-build installed.

.. code-block:: shell

    conda skeleton pypi PACKAGE_NAME # Compile Python Package PACKAGE_NAME into conda skeleton
    conda-build --python 3.4 PACKAGE_NAME # Compile Python Package PACKAGE_NAME into conda binary in the anaconda/conda-bld dir
    conda install --use-local PACKAGE_NAME

Update Help Doc
---------------

.. code-block:: shell

    # Navigate to the project/doc folder
    cd doc

    # Make the Programmable API
    make apidoc

    # Make the html documentation
    make html

    # Make the html images
    make htmlimage


Docker
------

.. code-block:: shell

    ## List Docker CLI commands
    docker
    docker container --help

    ## Display Docker version and info
    docker --version
    docker version
    docker info

    ## Execute Docker image
    docker run hello-world

    ## List Docker images
    docker image ls

    ## List Docker containers (running, all, all in quiet mode)
    docker container ls
    docker container ls --all
    docker container ls -aq


Run sknrf
----------

.. code-block:: shell

    import sknrf # Import the sknrf package
    sknrf.main() # Run the sknrf entry point