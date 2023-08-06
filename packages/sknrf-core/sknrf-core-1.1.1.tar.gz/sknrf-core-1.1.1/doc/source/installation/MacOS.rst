.. sknrf documentation introduction file

..  figure:: ../_images/PNG/sknrf_logo.png
    :width: 500 pt
    :align: center

macOS
=====

Environment Variables
---------------------

.. note::
    For C/C++ Developers Only.

.. tip::
   Make ~/.bash_profile environment variables accessable to all terminal/gui applications
    .. code-block:: bash

        >>> curl https://raw.githubusercontent.com/ersiner/osx-env-sync/master/osx-env-sync.plist -o ~/Library/LaunchAgents/osx-env-sync.plist
        >>> curl https://raw.githubusercontent.com/ersiner/osx-env-sync/master/osx-env-sync.sh -o ~/.osx-env-sync.sh
        >>> chmod +x ~/.osx-env-sync.sh
        >>> launchctl load ~/Library/LaunchAgents/osx-env-sync.plist

    Create a ~/.osx-env-sync-now script for reloading the environment variables after ~/.bash_profile is changed:
    .. code-block:: bash

        >>> curl https://raw.githubusercontent.com/ersiner/osx-env-sync/master/osx-env-sync-now -o ~/.osx-env-sync-now
        >>> chmod +x ~/.osx-env-sync-now

.. tip::
   Save settings in the user environment (~/.bashrc), not the system environment (~/.bash_profile)

.. code-block:: bash

    # Clang
    export CLANG_INSTALL_DIR="$HOME/libclang"

    # Qt 5.12.0
    export QT_DIR="$HOME/Qt/5.12.0/clang_64"
    export QMAKESPEC="macx-clang"
    export QT_PATH="$QT_DIR/bin"
    export QT_LD_LIBRARY_PATH="$QT_DIR/lib:$QT_DIR/plugins/platforms"

    # ADS
    #export HPEESOF_DIR="/ADS_2016/"
    #export COMPL_DIR="$HPEESOF_DIR"
    #export SIMARCH="linux_64"
    #export ADS_PATH="$HPEESOF_DIR/bin/$SIMARCH:$HPEESOF_DIR/bin:$HPEESOF_DIR/lib/$SIMARCH:$HPEESOF_DIR/circuit/lib.$SIMARCH:$HPEESOF_DIR/adsptolemy/lib.$SIMARCH"

    # Anaconda 4.5.11
    export CONDA_PYTHONPATH="$CONDA_PREFIX/lib"

    # Scikit-Nonlinear
    export SRC_DIR="$HOME/repos/scikit-nonlinear-core-dev"

    # PyCharm
    export PYDEVD_PYQT_MODE="pyside"

    # The above variables are shared with the GUI environment (after application restart)
    launchctl setenv CLANG_INSTALL_DIR $CLANG_INSTALL_DIR
    launchctl setenv QT_DIR $QT_DIR
    launchctl setenv QMAKESPEC $QMAKESPEC
    launchctl setenv QT_PATH $QT_PATH
    launchctl setenv QT_LD_LIBRARY_PATH $QT_LD_LIBRARY_PATH
    launchctl setenv CONDA_PYTHONPATH $CONDA_PYTHONPATH
    launchctl setenv SRC_DIR $SRC_DIR
    launchctl setenv PYDEVD_PYQT_MODE $PYDEVD_PYQT_MODE
    # The below variables are only available in the terminal.

    # PATH
    #echo $PATH > $CONDA_PREFIX/etc/conda/PATH.txt
    #echo $DYLD_LIBRARY_PATH > $CONDA_PREFIX/etc/conda/DYLD_LIBRARY_PATH.txt
    #echo $PYTHONPATH > $CONDA_PREFIX/etc/conda/PYTHONPATH.txt

    export PATH="$QT_PATH:$PATH"
    export DYLD_LIBRARY_PATH="$QT_LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH"
    export PYTHONPATH="$CONDA_PYTHONPATH:$PYTHONPATH"

Installation
------------

Xcode (C++ compiler)
~~~~~~~~~~~~~~~~~~~~

Install Xcode and the command line tools:

- Install `Xcode <https://developer.apple.com/xcode/>`_.
    - Open X-Code and accept Licence Agreement.
- Install Xcode Command Line Tools.

    .. code-block:: bash

        >>> xcode-select --install

Homebrew
~~~~~~~~

Install `Homebrew <https://brew.sh>`_.

.. code-block:: bash

    >>> /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Test the installlation from the terminal:

.. code-block:: bash

    >>> which brew

VPN
~~~

.. code-block:: bash

    >>> brew install openvpn
    >>> sudo brew services start openvpn

Git
~~~

Install Git.

.. code-block:: bash

    >>> brew install git
    >>> git config --global core.autocrlf input

Test the installlation from the terminal:

.. code-block:: bash

    >>> which git

7zip
~~~~

Install Git.

.. code-block:: bash

    >>> brew install p7zip

Test the installlation from the terminal:

.. code-block:: bash

    >>> which 7z


clang
~~~~~

Install Clang.

.. code-block:: bash

    >>> brew install clang++

Test the installlation from the terminal:

.. code-block:: bash

    >>> which clang
    >>> which clang++

libClang
~~~~~~~~

Install libClang.

.. code-block:: bash

    >>> wget https://download.qt.io/development_releases/prebuilt/libclang/libclang-release_60-mac-clazy.7z
    >>> 7z x libclang-release_60-mac-clazy.7z

Test the installlation from the terminal:

.. code-block:: bash

    which clang


CCache
~~~~~~

Install ccache.

.. code-block:: bash

    >>> brew install libb2
    >>> brew install zstd
    >>> brew install --HEAD ccache

Test the installlation from the terminal:

.. code-block:: bash

    >>> which ccache

Make ccache masquerading as the compiler via symlinks.

.. code-block:: bash

    >>> ccache -M 25Gi  # Set the cache size
    >>> ccache -F 0 # Unlimited files
    >>> ln -s ccache /usr/local/bin/gcc
    >>> ln -s ccache /usr/local/bin/g++
    >>> ln -s ccache /usr/local/bin/cc
    >>> ln -s ccache /usr/local/bin/c++

Test that ccache to make these paths are being used:

.. code-block:: bash

    >>> which gcc
    >>> which g++
    >>> which cc
    >>> which c++

CMake
~~~~~

Install Cmake from source (.dmg does not install command line).

.. code-block:: bash

    >>> brew install cmake

Test the installlation from the terminal:

.. code-block:: bash

    >>> which cmake

Perl
----
Should be pre-installed.
Test the installation from the terminal:

.. code-block:: bash

    >>> which perl

Docker
~~~~~~

Install Docker.

.. code-block:: bash

    >>> brew cask install docker

Launch the Docker Desktop Application and make sure it is running. Test the installlation from the terminal:

.. code-block:: bash

    >>> which docker
    >>> which docker-compose
    >>> which docker-credential-osxkeychain
    >>> which docker-machine

NI VISA Libraries
~~~~~~~~~~~~~~~~~

Install the `National Instruments VISA libraries <http://www.ni.com/download/ni-visa-15.0.1/5693/en/>`_.

Qt
~~

Install using the online installer.

Test the installlation from the terminal:

.. code-block:: bat

    >>> which qmake

Anaconda
~~~~~~~~
Download and install `Anaconda for Python3 macOS <https://www.continuum.io/downloads#macos>`_.

    - Install for "Just me".
    - Add to path.
    - Make default version of python.

Test the installlation from the terminal:

.. code-block:: bash

    >>> which conda

Python 3.6
~~~~~~~~~~
Create a Python 3.6 Anaconda virtual environment.

.. code-block:: bash

    >>> conda create -n py36 python=3.6 anaconda
    >>> source activate py36
    >>> conda uninstall qt

Test the installlation from the terminal:

.. code-block:: bash

    >>> which python
    >>> which qmake

Shiboken/PySide2
~~~~~~~~~~~~~~~~
Build Shiboken/Shiboken Generator/PySide2 from source as follows:

.. code-block:: bash

    >>> git clone --recursive https://code.qt.io/pyside/pyside-setup
    >>> cd pyside-setup && git checkout 5.12
    >>> python setup.py build --qmake=$QT_DIR/bin/qmake --build-tests --ignore-git --parallel=12
    >>> python setup.py install --qmake=$QT_DIR/bin/qmake --build-tests --ignore-git --parallel=12

Test the installlation from the terminal:

.. code-block:: bash

    >>> which shiboken2
    >>> which pyside2-rcc
    >>> which pyside2-uic

Add symlinks to the Qt installation directory so that Shiboken can find header files inside the Framwork folders

.. code-block:: bash

    >>> ln -s $QT_DIR/lib/QtCore.framework/Headers $QT_DIR/include/QtCore
    >>> ln -s $QT_DIR/lib/QtGui.framework/Headers $QT_DIR/include/QtGui
    >>> ln -s $QT_DIR/lib/QtWidgets.framework/Headers $QT_DIR/include/QtWidgets

PyTorch
~~~~~~~

Compile PyTorch from sorce as follows:

 .. code-block:: bash

    >>> conda install numpy ninja pyyaml mkl mkl-include setuptools cmake cffi typing
    >>> git clone --recursive git@github.com:dylanbespalko/pytorch.git
    >>> cd pytorch
    >>> # if you are updating an existing checkout
    >>> git submodule sync
    >>> git submodule update --init --recursive
    >>> export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
    >>> python setup.py install develop


Test the installlation from the terminal:

.. code-block:: bash

    >>> python
    >>> import torch

matplotlib
~~~~~~~~~~
Install matplotlib using conda as follows:

.. code-block:: bash

    >>> conda install matplotlib --no-dep


Test the installlation from the terminal:

.. code-block:: bash

    >>> python
    >>> import matplotlib

Scikit-RF
~~~~~~~~~
Install Scikit-RF using conda as follows:

.. code-block:: bash

    >>> conda install scikit-rf --no-dep


Test the installlation from the terminal:

.. code-block:: bash

    >>> python
    >>> import skrf


Python-PPTX
~~~~~~~~~~~

Install Python-PPTX using pip as follows:

.. code-block:: bash

    >>> pip install python-pptx

Test the installlation from the terminal:

.. code-block:: bash

    >>> python
    >>> import pptx

Parmiko
~~~~~~~
Install Parmiko using conda as follows:

.. code-block:: bat

    >>> conda install paramiko

Test the installation from the terminal:

.. code-block:: bat

    >>> python
    >>> import paramiko

Toposort
~~~~~~~~
Install Toposort using pip as follows:

.. code-block:: bat

    >>> pip install toposort

Test the installation from the terminal:

.. code-block:: bat

    >>> python
    >>> import toposort

PyVisa
------
Install PyVisa using pip as follows:

.. code-block:: bat

    >>>> pip install -U pyvisa

Test the installlation from the terminal:

.. code-block:: bat

    >>> python
    >>> import visa

Nose-Exclude
~~~~~~~~~~~~
Install Nose-Exclude using pip as follows:

.. code-block:: bat

    >>> pip install nose-exclude

Test the installation from the terminal:

.. code-block:: bat

    >>> python
    >>> import nose_exclude


PyLint
~~~~~~
Install PyLint using conda as follows:

.. code-block:: bash

    >>> conda install pylint

Test the installation from the terminal:

.. code-block:: bash

    which pylint


Radon
~~~~~
Install radon using pip as follows:

.. code-block:: bash

    >>> pip install radon

Test the installation from the terminal:

.. code-block:: bash

    which radon


Sphinx Bootstrap Theme
~~~~~~~~~~~~~~~~~~~~~~
Install Sphinx Bootstrap Theme using pip as follows:

.. code-block:: bat

    >>> pip install sphinx_bootstrap_theme

Test the installation from the terminal:

.. code-block:: bat

    >>> python
    >>> import sphinx_bootstrap_theme

