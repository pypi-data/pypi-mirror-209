.. sknrf documentation introduction file

..  figure:: ../_images/PNG/sknrf_logo.png
    :width: 500 pt
    :align: center

Linux
=====

Environment Variables
---------------------

.. tip::
   Replace $USER with your local user folder.

.. tip::
   Save settings in the user environment (~/.bashrc), not the system environment (~/.bash_profile)

.. tip::
    Run  mv ~/anaconda3/bin/qtpaths ~/anaconda3/bin/qtpaths-qt5 to avoid qt conflict with KDE user login process

.. code-block:: bash

    # Clang
    export LLVM_INSTALL_DIR=`llvm-config-6.0 --prefix`

    # Qt 5.12.0
    export QTDIR="$HOME/Qt/5.12.2/gcc_64"
    export QMAKESPEC="linux-clang"
    export QT_PATH="$QTDIR/bin"
    export QT_LD_LIBRARY_PATH="$QTDIR/lib:$QTDIR/plugins/platforms"

    # ADS
    # export HPEESOF_DIR="/ADS_2016/"
    # export COMPL_DIR="$HPEESOF_DIR"
    # export SIMARCH="linux_64"
    # export ADS_PATH="$HPEESOF_DIR/bin/$SIMARCH:$HPEESOF_DIR/bin:$HPEESOF_DIR/lib/$SIMARCH:$HPEESOF_DIR/circuit/lib.$SIMARCH:$HPEESOF_DIR/adsptolemy/lib.$SIMARCH"

    # Anaconda 4.5.11
    export CONDA_PYTHONPATH="$CONDA_PREFIX/lib"
    export CPLUS_INCLUDE_PATH="$CONDA_PREFIX/include/python3.6m:$CPLUS_INCLUDE_PATH"

    # Scikit-Nonlinear
    export SRC_DIR="$HOME/repos/ci-cpp-python-dev"

    # PyCharm
    export PYDEVD_PYQT_MODE="pyside"

    # PATH
    echo $PATH > $CONDA_PREFIX/etc/conda/PATH.txt
    echo $LD_LIBRARY_PATH > $CONDA_PREFIX/etc/conda/LD_LIBRARY_PATH.txt
    echo $PYTHONPATH > $CONDA_PREFIX/etc/conda/PYTHONPATH.txt

    export PATH="$QT_PATH:$PATH"
    export LD_LIBRARY_PATH="$QT_LD_LIBRARY_PATH:$LD_LIBRARY_PATH"
    export PYTHONPATH="$CONDA_PYTHONPATH:$PYTHONPATH"

Installation
------------

Prerequisites
~~~~~~~~~~~~~
    * Setup root account
    * Disable automatic login
    * Install updates

Enable Port Forwarding in VirtualBox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VirtualBox->Settings->Network->Adapter1->Advanced->Port Forwarding
    * Protocol: TCP
    * Host IP: 127.0.0.1
    * Host Port: 2222
    * Guest IP: 10.0.2.15
    * Guest Port: 22

Jenkins
~~~~~~~

Create Jenkins Group/User on Remote machine (Linux)

 .. code-block:: bash

    >>>sudo groupadd jenkins
    >>>sudo useradd -m -s /bin/bash -g jenkins jenkins
    >>>sudo passwd jenkins
    >>>sudo usermod -a -G jenkins jenkins

Repeat the SSH step for jenkins USER

SSH
~~~

Check the status of the sshd server

 .. code-block:: bash

   >>>sudo apt install openssh-server
   >>>sudo systemctl status ssh
   >>>q

Generate Keys

 .. code-block:: bash

    >>>ssh-keygen -t rsa  # Default location, no passphrase

Remove existing known hosts from Remote Machine

 .. code-block:: bash

    >>> ssh-keygen -R [hostname]:port
    >>> sudo ssh-keygen -R hostname]:port

Connect from a Remote Machine

.. code-block:: bash

    >>>ssh-copy-id -p PORT USER@ADDRESS  // add local user to authorized_keys on host
    >>>sudo ssh-copy-id -p PORT USER@ADDRESS  // add root user to authorized_keys on host
    >>>ssh -p PORT USER@ADDRESS
    >>>sftp -P PORT USER@ADDRESS
    >>>sudo ssh -p PORT USER@ADDRESS
    >>>sudo sftp -P PORT USER@ADDRESS


C++ Compiler
~~~~~~~~~~~~

Install the developer tools:

.. code-block:: bash

    >>> sudo apt-get update
    >>> sudo apt-get upgrade
    >>> sudo apt install build-essential

 .. code-block:: bash

    >>> gcc -v
    >>> make -v

Git
~~~

Install Git.

.. code-block:: bash

    >>> sudo apt install git
    >>> git config --global core.autocrlf input

Test the installlation from the terminal:

.. code-block:: bash

    >>> which git

libClang
~~~~~~~~

Install Clang and libClang

.. code-block:: bash

    >>> sudo apt install llvm-6.0
    >>> sudo apt install clang
    >>> sudo apt install clang-6.0
    >>> sudo apt install libclang-6.0-dev
    >>> sudo apt install libxslt-dev
    >>> sudo apt install mesa-common-dev
    >>> sudo apt install libgl1-mesa-glx
    >>> sudo apt install libgl1-mesa-dev
    >>> sudo apt install libglib2.0-0
    >>> sudo apt install wget

Test the installlation from the terminal

.. code-block:: bash

    >>> export LLVM_INSTALL_DIR=`llvm-config-6.0 --prefix`
    >>> which clang-6.0
    >>> which clang

Perl
----
Should be pre-installed.
Test the installation from the terminal:

.. code-block:: bash

    >>> which perl

NI VISA Libraries
-----------------
Install the `National Instruments VISA libraries 15 <http://www.ni.com/download/ni-visa-15.0/5410/en/>`_.

    - Install the Visa libraries

.. code-block:: bash

    >>> cd ~/Downloads
    >>> sudo mkdir /mnt/visa
    >>> sudo mount -o loop NI-VISA*.iso /mnt/visa/
    >>> cd /mnt/visa
    >>> sudo ./INSTALL
    >>> sudo umount /mnt/visa
    >>> sudo rmdir /mnt/visa

Test the installlation from the terminal:

.. code-block:: bash

    >>> niiotrace

Cairo
~~~~~

sudo apt install libcairo2-dev
sudo apt install libgirepository1.0-dev

CMAKE
-----
Install Cmake.

.. code-block:: bash

    >>> sudo apt install cmake
    >>> # We require CMake >= 3.12 due to the improved Python support
    >>> wget https://github.com/Kitware/CMake/releases/download/v3.13.4/cmake-3.13.4-Linux-x86_64.tar.gz
    >>> tar xvf cmake-3.13.4-Linux-x86_64.tar.gz


Test the installlation from the terminal:

.. code-block:: bash

    >>> export CMAKE_PATH="$HOME/cmake-3.13.4-Linux-x86_64/bin"
    >>> export PATH="$CMAKE_PATH:$PATH"
    >>> which cmake
    >>> cmake --version

Qt
~~

Install using the online installer. Select the version of Qt that you would like to install (eg. Qt 5.12.2)

    .. code-block:: bash

        >>> chmod +x qt-unified-linux-x64-3.0.5-online.run
        >>> ./qt-unified-linux-x64-3.0.5-online.run

Test the installlation from the terminal:

.. code-block:: bat

    >>> export QTDIR="$HOME/Qt/5.12.2/gcc_64"
    >>> export QMAKESPEC="linux-clang"
    >>> export QT_PATH="$QTDIR/bin"
    >>> export PATH="$QT_PATH:$PATH"
    >>> which qmake

Anaconda
--------
Download and install `Anaconda for Python3 Linux <https://www.continuum.io/downloads#linux>`_.

.. code-block:: bash

    >>> /bin/bash
    >>> bash Anaconda3-5.3.1-Linux-x86_64.sh

    - Press ENTER To install to user/anaconda3 folder

Test the installlation from the terminal:

.. code-block:: bash

    >>> /bin/bash
    >>> which conda

Python 3.6
----------
Create a Python 3.4 Anaconda virtual environment.

.. code-block:: bash

    >>> conda create -n py36 python=3.6 anaconda
    >>> conda activate py36
    >>> conda uninstall qt

Test the installlation from the terminal:

.. code-block:: bash

    >>> which python
    >>> which cmake
    >>> whcih qmake

PyVisa
------
Install PyVisa using pip as follows:

.. code-block:: bat

    >>>> python -m pip install -U pyvisa

Test the installlation from the terminal:

.. code-block:: bat

    >>> python
    >>> import visa

Shiboken/PySide
---------------

Build Shiboken/Shiboken Generator/PySide2 from source as follows:

.. code-block:: bash

    >>> git clone --recursive https://code.qt.io/pyside/pyside-setup
    >>> cd pyside-setup
    >>> git checkout 5.12.2
    >>> git submodule update --init
    >>> python setup.py build --qmake=$QT_DIR/bin/qmake --jobs=4
    >>> python setup.py install --qmake=$QT_DIR/bin/qmake --jobs=4

Test the installlation from the terminal:

.. code-block:: bash

    >>> which shiboken2
    >>> which pyside2-rcc
    >>> which pyside2-uic

PyTorch
~~~~~~~

Compile PyTorch from sorce as follows:

 .. code-block:: bash

    >>> conda install numpy pyyaml mkl mkl-include setuptools cmake cffi typing
    >>>
    >>> # Add LAPACK support for the GPU if needed
    >>> conda install -c pytorch magma-cuda90 # or [magma-cuda80 | magma-cuda92 | magma-cuda100 ] depending on your cuda version
    >>> python setup.py install develop

Test the installlation from the terminal:

.. code-block:: bash

    >>> python
    >>> import torch

Matplotlib
~~~~~~~~~~
Install Matplotlib using conda as follows:

.. code-block:: bash

    >>> conda install matplotlib --no-deps

Test the installlation from the terminal:

.. code-block:: bash

    >>> python
    >>> import matplotlib

Scikit-RF
~~~~~~~~~
Install Scikit-RF using conda as follows:

.. code-block:: bash

    >>> conda install scikit-rf --no-deps

Test the installlation from the terminal:

.. code-block:: bash

    >>> python
    >>> import skrf


Parmiko
~~~~~~~
Install Parmiko using conda as follows:

.. code-block:: bash

    >>> conda install paramiko

Test the installation from the terminal:

.. code-block:: bash

    >>> python
    >>> import paramiko

Toposort
~~~~~~~~
Install Toposort using pip as follows:

.. code-block:: bash

    >>> pip install toposort

Test the installation from the terminal:

.. code-block:: bash

    >>> python
    >>> import toposort

Nose-Exclude
~~~~~~~~~~~~
Install Nose-Exclude using pip as follows:

.. code-block:: bash

    >>> pip install nose-exclude

Test the installation from the terminal:

.. code-block:: bash

    >>> python
    >>> import nose_exclude

Sphinx Bootstrap Theme
~~~~~~~~~~~~~~~~~~~~~~
Install Sphinx Bootstrap Theme using pip as follows:

.. code-block:: bash

    >>> pip install sphinx_bootstrap_theme

Test the installation from the terminal:

.. code-block:: bash

    >>> python
    >>> import sphinx_bootstrap_theme

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




