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

    # CMake
    export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}

    # Clang
    export LLVM_INSTALL_DIR=`llvm-config-6.0 --prefix`

    # Qt 5.12.3
    export QT_DIR="$HOME/Qt"
    export QMAKESPEC="linux-clang"
    export QT_QPA_PLATFORM_PLUGIN_PATH="$QT_DIR/plugins/platforms"
    export QT_PLUGIN_PATH="$QT_DIR/plugins"
    export QML2_IMPORT_PATH="$QT_DIR/qml"
    export QT_PATH="$QT_DIR/bin"
    export QT_LD_LIBRARY_PATH="$QT_DIR/lib"

    # ADS
    # export HPEESOF_DIR="/ADS_2016/"
    # export COMPL_DIR="$HPEESOF_DIR"
    # export SIMARCH="linux_64"
    # export ADS_PATH="$HPEESOF_DIR/bin/$SIMARCH:$HPEESOF_DIR/bin:$HPEESOF_DIR/lib/$SIMARCH:$HPEESOF_DIR/circuit/lib.$SIMARCH:$HPEESOF_DIR/adsptolemy/lib.$SIMARCH"

    # Anaconda
    export CONDA_PYTHONPATH="$CONDA_PREFIX/lib"
    export CPLUS_INCLUDE_PATH="$CONDA_PREFIX/include/python3.6m:$CPLUS_INCLUDE_PATH"

    # PyTables
    export HDF5_DIR="/usr/lib/aarch64-linux-gnu/hdf5/serial"

    # PyTorch
    export USE_NCCL=0
    export USE_DISTRIBUTED=0
    export TORCH_CUDA_ARCH_LIST="5.3;6.2"

    # Scikit-Nonlinear
    #export SRC_DIR="$HOME/workspace/ci-cpp-python"
    #export SRC_DIR="$HOME/repos/ci-cpp-python-dev"

    # PATH
    echo $PATH > $CONDA_PREFIX/etc/conda/PATH.txt
    echo $LD_LIBRARY_PATH > $CONDA_PREFIX/etc/conda/LD_LIBRARY_PATH.txt
    echo $PYTHONPATH > $CONDA_PREFIX/etc/conda/PYTHONPATH.txt

    export PATH="$QT_PATH:$CMAKE_PATH:$PATH"
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


Jetson
~~~~~~
Install the Jetson Stats

.. code-block:: bash

    >>>sudo -H pip install -U jetson-stats

Check the Jetions stats using

.. code-block:: bash

    >>>sudo jtop


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


VNC
~~~

Install and configure a VNC Server based on the instructions here [https://poweruphosting.com/blog/setup-vnc-server-on-ubuntu/]

.. code-block:: bash

    >>>sudo apt install xfce4 xfce4-goodies tightvncserver
    >>>vncserver # Make sure to set password
    >>>vncserver -kill :1
    >>>netstat -tulpn
    >>>mv ~/.vnc/xstartup ~/.vnc/xstartup.bak
    >>> touch ~/.Xresources
    >>>nano ~/.vnc/xstartup

Copy the folloing in to ~/.vnc/xstartup

.. code-block:: bash

    ~/.vnc/xstartup
    #!/bin/bash
    xrdb $HOME/.Xresources
    startxfce4 &


Then restart the server

.. code-block:: bash

    >>>sudo chmod +x ~/.vnc/xstartup
    >>>vncserver -geometry 1024x640

Then connect client on remote machine

.. code-block:: bash

    >>>ping 192.168.2.2
    >>>ssh deepwave@192.168.2.2 -L 5901:localhost:5901
    >>>exit

Open VNC Client and connect to vnc://192.168.2.2:5901

Optionally load additional graphical configurations

.. code-block:: bash

    >>>sudo apt-get install ubuntu-gnome-desktop -y
    >>>sudo apt-get install gnome-do
    >>>vncserver -kill :1
    >>>nano ~/.vnc/xstartup

Add the folloing in to ~/.vnc/xstartup

.. code-block:: bash

    #!/bin/sh
    def
    export XKL_XMODMAP_DISABLE=1
    unset SESSION_MANAGER
    unset DBUS_SESSION_BUS_ADDRESS

    gnome-panel &
    gnome-settings-daemon &
    metacity &
    nautilus &
    gnome-terminal &

Then restart the server

.. code-block:: bash

    >>>vncserver -geometry 1024x640


Create a service that launches at startup:

.. code-block:: bash

    >>>sudo nano /etc/systemd/system/vncserver@.service

Copy the following into the file

.. code-block:: bash

    [Unit]
    Description=Start TightVNC server at startup
    After=syslog.target network.target

    [Service]
    Type=forking
    User=deepwave
    PAMName=login
    PIDFile=/home/deepwave/.vnc/%H:%i.pid
    ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null     2>&1
    ExecStart=/usr/bin/vncserver -depth 24 -geometry     1680x1050 :%i
    ExecStop=/usr/bin/vncserver -kill :%i

    [Install]
    WantedBy=multi-user.target

Reload the Services

.. code-block:: bash

    sudo systemctl daemon-reload
    sudo systemctl enable vncserver@1.service
    sudo systemctl list-unit-files | grep vnc


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

Test the installlation from the terminal: sug

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
    >>> sudo apt-get install libegl1-mesa-lts-xenial
    >>> sudo apt-get install libgles2-mesa-dev
    >>> sudo apt-get install libssl-dev
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

CCache
~~~~~~

Install ccache.

.. code-block:: bash

    >>> sudo apt install ccache

Test the installlation from the terminal:

.. code-block:: bash

    >>> which ccache

Make ccache masquerading as the compiler via symlinks.

.. code-block:: bash

    >>> ccache -M 25Gi  # Set the cache size
    >>> ccache -F 0 # Unlimited files
    >>> sudo /usr/sbin/update-ccache-symlinks
    >>> sudo ln -s /usr/bin/ccache /usr/lib/ccache/clang-6.0
    >>> sudo ln -s /usr/bin/ccache /usr/lib/ccache/clang++-6.0
    >>> sudo ln -s /usr/bin/ccache /usr/lib/ccache/nvcc
    >>> export PATH="/usr/lib/ccache:$PATH"

Test that ccache to make these paths are being used:

.. code-block:: bash

    >>> which gcc && gcc
    >>> which g++ && g++
    >>> which cc && cc
    >>> which c++ && c++
    >>> which clang && clang
    >>> which clang++ && clang++
    >>> which clang-6.0 && clang-6.0
    >>> which clang++-6.0 && clang++6.0
    >>> which nvcc && nvcc


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

    >>> which cmake
    >>> cmake --version


SSL
~~~

Install OpenSSL with the following commands:

.. code-block:: bash

    >>>sudo apt-get install openssl
    >>>apt-cache search libssl | grep SSL
    >>>sudo apt-get install libsslcommon2
    >>>sudo apt-get install libsslcommon2-dev

Qt
~~

Build from Source as follows

.. code-block:: bash

    >>> wget http://download.qt.io/official_releases/qt/5.12/5.12.3/single/qt-everywhere-src-5.12.3.tar.xz
    >>> md5sum qt-everywhere-src-5.12.3.tar.xz
    >>> sudo apt-get install xz-utils
    >>> unxz qt-everywhere-src-5.12.3.tar.xz
    >>> tar -xf qt-everywhere-src-5.12.3.tar
    >>> ./configure -list-features
    >>> ./configure -opensource -confirm-license -skip webengine -make libs -sysroot / -prefix $HOME/Qt/5.12.3


Test the installlation from the terminal:

.. code-block:: bash

    >>> export QT_DIR="$HOME/Qt"
    >>> export QMAKESPEC="linux-clang"
    >>> export QT_PATH="$QT_DIR/bin"
    >>> export PATH="$QT_PATH:$PATH"
    >>> which qmake

Anaconda
--------
Download and install `Archiconda3 <https://github.com/Archiconda/build-tools/releases>`_.


.. code-block:: bash

    >>> /bin/bash
    >>> bash Archiconda3-0.2.2-Linux-aarch64.sh
    >>> bash Anaconda3-5.3.1-Linux-x86_64.sh

    - Press ENTER To install to $HOME/anaconda3 folder

Test the installlation from the terminal:

.. code-block:: bash

    >>> /bin/bash
    >>> which conda

Python 3.6
----------
Create a Python 3.6 Anaconda virtual environment.

.. code-block:: bash

    >>> conda create -n py36 python=3.6
    >>> conda activate py36
    >>> conda uninstall qt

Test the installlation from the terminal:

.. code-block:: bash

    >>> which python
    >>> which cmake
    >>> which qmake

conda install python=3.6
conda install numpy
conda install scipy
conda install pillow
conda install six
conda install yaml
conda install pyyaml
conda install nose
pip install matplotlib
pip install numexpr
pip install lxml


PyVisa
------
Install PyVisa using pip as follows:

.. code-block:: bash

    >>>> python -m pip install -U pyvisa

Test the installlation from the terminal:

.. code-block:: bash

    >>> python
    >>> import visa

PyTables
~~~~~~~~

Compile Pytables from Source as follows:

.. code-block:: bash

    >>> sudo apt install libhdf5-dev
    >>> sudo apt install liblzo2-dev
    >>> sudo apt install libbz2-dev
    >>> export HDF5_DIR="/usr/lib/aarch64-linux-gnu/hdf5/serial"
    >>> python setup.py build
    >>> cd build/lib.linux-aarch64-3.6/
    >>> env PYTHONPATH=. python -c "import tables; tables.test()"
    >>> cd ../../
    >>> /bin/bash # unset the PYTHONPATH variable
    >>> python setup.py install

Shiboken/PySide
---------------

Build Shiboken/Shiboken Generator/PySide2 from source as follows:

.. code-block:: bash

    >>> git clone --recursive https://code.qt.io/pyside/pyside-setup
    >>> cd pyside-setup
    >>> git checkout 5.12.3
    >>> git submodule update --init
    >>> python setup.py build --qmake=$QT_DIR/bin/qmake  --module-subset=Core,Gui,Widgets,Network
    >>> python setup.py build --qmake=$QT_DIR/bin/qmake  --module-subset=Core,Gui,Widgets,Network,Qml,Quick,QuickWidgets  --parallel=5
    >>> python setup.py install --qmake=$QT_DIR/bin/qmake --parallel=5

Test the installlation from the terminal:

.. code-block:: bash

    >>> which shiboken2
    >>> which pyside2-rcc
    >>> which pyside2-uic

Test the installation inside Python

.. code-block:: bash

    >>> python
    >>> from PySide6 import QtCore, QtGui, QtWidgets, QtQuickWidgets


NCCL
~~~~

Folllow the instructions here: https://docs.nvidia.com/deeplearning/sdk/nccl-install-guide/index.html


.. code-block:: bash

    >>> sudo dpkg -i nvidia-machine-learning-repo-<version>.deb

PyTorch
~~~~~~~

Compile PyTorch from sorce as follows:

 .. code-block:: bash

    >>> export USE_NCCL=0
    >>> export USE_DISTRIBUTED=0
    >>> export TORCH_CUDA_ARCH_LIST="5.3;6.2"
    >>> sudo add-apt-repository ppa:ubuntu-toolchain-r/test
    >>> sudo apt-get update
    >>> sudo apt-get install gcc-7 g++-7
    >>> sudo apt-get install gfortran-7
    >>>
    >>> git clone --recursive https://github.com/pytorch/pytorch
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


Matplotlib
~~~~~~~~~~
Install Matplotlib using conda as follows:

.. code-block:: bash

    >>> pip install matplotlib

Test the installlation from the terminal:

.. code-block:: bash

    >>> python
    >>> import matplotlib

Scikit-RF
~~~~~~~~~
Install Scikit-RF using pip as follows:

.. code-block:: bash

    >>> pip install scikit-rf

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
Install PyLint using pip as follows:

.. code-block:: bash

    >>> pip install pylint

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




