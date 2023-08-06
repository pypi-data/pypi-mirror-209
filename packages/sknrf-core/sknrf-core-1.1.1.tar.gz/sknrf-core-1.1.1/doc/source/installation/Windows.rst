.. sknrf documentation introduction file

..  figure:: ../_images/PNG/sknrf_logo.png
    :width: 500 pt
    :align: center

Windows
=======

Environment Variables
---------------------

.. note::
    For C/C++ Developers Only.

.. tip::
   Replace %username% with your local user folder.

.. code-block:: bat

    @echo off
    CALL "C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\VC\Auxiliary\Build\vcvars64.bat"

    rem C++ Compiler
    set "SDK=C:\Program Files (x86)\Windows Kits\10">NUL

    rem Clang
    set LLVM_INSTALL_DIR=%USERPROFILE%\libclang>NUL
    set CLANG_PATH=%LLVM_INSTALL_DIR%\bin>NUL

    rem Qt 5.12.0
    set QTDIR=%HOMEDRIVE%\Qt\5.12.0\msvc2017_64>NUL
    set QMAKESPEC=win32-clang-msvc>NUL
    set QT_PATH=%QTDIR%\bin>NUL
    set QT_LD_LIBRARY_PATH=%QTDIR%\lib:%QTDIR%\plugins\platforms>NUL

    rem ADS
    rem set HPEESOF_DIR=C:\ADS_2016>NUL
    rem set COMPL_DIR=%HPEESOF_DIR%>NUL
    rem set SIMARCH=win32_64>NUL
    rem set ADS_PATH=%HPEESOF_DIR%\bin\%SIMARCH%;%HPEESOF_DIR%\bin;%HPEESOF_DIR%\lib\%SIMARCH%;%HPEESOF_DIR%\circuit\lib.%SIMARCH%;$

    rem Anaconda 4.5.11
    set CONDA_PYTHONPATH=%CONDA_PREFIX%\Library\bin>NUL

    rem Shiboken/PySide
    set SHIBOKEN_PATH=%CONDA_PREFIX%\Lib\site-packages\shiboken2>NUL
    set PYSIDE_PATH=%CONDA_PREFIX%\Lib\site-packages\PySide2>NUL

    rem Scikit-Nonlinear
    rem set SRC_DIR=%USERPROFILE%\workspace\ci-cpp-python>NUL
    rem set SRC_DIR=%USERPROFILE%\repos\ci-cpp-python>NUL

    rem PyCharm
    set PYDEVD_PYQT_MODE=pyside>NUL

    rem PATH
    echo %PATH%>%CONDA_PREFIX%\etc\conda\PATH.txt
    echo %PYTHONPATH%>%CONDA_PREFIX%\etc\conda\PYTHONPATH.txt

    rem set PATH="%PYSIDE_PATH%;%SHIBOKEN_PATH%;%QT_PATH%;%QT_LD_LIBRARY_PATH%;%CONDA_PATH%;%CLANG_PATH%;%PATH%"
    set PATH=%PYSIDE_PATH%;%SHIBOKEN_PATH%;%QT_PATH%;%QT_LD_LIBRARY_PATH%;%CLANG_PATH%;%PATH%
    set PYTHONPATH=%CONDA_PYTHONPATH%;%PYTHONPATH%

Installation
------------

Visual Studio 2017
~~~~~~~~~~~~~~~~~~

.. note::
    Install Native Tools
    Install Python Support

.. tip::
   Pin the "x64 Native Command Prompt for VS2017" to your Start Menu so that you always use it.

Test the installation from the terminal:

.. code-block:: bat

    >>> where nmake
    >>> where cl

Chocolately
~~~~~~~~~~~

Install `Chocolately Website  <https://chocolatey.org/>`_.

Test the installation from the terminal:

.. code-block:: bat

    >>> where choco

jom
~~~

Instal jom:

.. code-block:: bat

    >>> choco install jom

Test the installation from the terminal:

.. code-block:: bat

    >>> where jom

Git
~~~

Install Git:

.. code-block:: bat

    >>> choco install git
    >>> git config --global core.autocrlf true

Test the installation from the terminal:

.. code-block:: bat

    >>> where git

7zip
~~~~

Install Git.

.. code-block:: bat

    >>> choco install 7zip.install

Test the installlation from the terminal:

.. code-block:: bat

    >>> where 7z


libClang
~~~~~~~~

Download libClang and extract libClang

.. code-block:: bat

    >>> 7z x libclang-release_60-windows-vs2015_64-clazy.7z

.. code-block:: bat

    >>> which clang


CMake
~~~~~

Install Git:

.. code-block:: bat

    >>> choco install cmake

Test the installation from the terminal:

.. code-block:: bat

    >>> where cmake

Ninja
~~~~~


Perl
~~~~

Install `Strawberry Perl <http://strawberryperl.com/>`_.

Test the installation from the terminal:

.. code-block:: bat

    >>> where perl

Docker
~~~~~~

Install Docker.

.. code-block:: bat

    >>> TBD

Test the installlation from the terminal:

.. code-block:: bat

    >>> where docker

NI VISA Libraries
~~~~~~~~~~~~~~~~~

.. note::
    For measurement instrument i/o support.

Install the `National Instruments VISA libraries <http://www.ni.com/download/ni-visa-17.0/6646/en/>`_.

Test the installation from the terminal by launching NI MAX.

Qt
~~

.. note::
    For C/C++ Developers Only.

Install using the online installer. Select the version of Qt that you would like to install (eg. Qt 5.12.0)

Test the installlation from the terminal:

.. code-block:: bat

    >>> which qmake


QWT
~~~

.. note::
    For C/C++ Developers Only.

Download `QWT Library <http://qwt.sourceforge.net>`_ and compile
using the following process:

- Open Windows SDK 7.1 > x64 Build environment as Administrator.
- Unzip QWT Library to C:\\Qwt %VERSION% and navigate to this folder.

    .. code-block:: bat

        >>> qmake -spec %QMAKESPEC% qwt.pro
        >>> nmake
        >>> sudo nmake install

Advanced Design System
~~~~~~~~~~~~~~~~~~~~~~

.. note::
    For simulation support.

Install the Advanced Design System support as follows:

    - Download and install ADS.
    - Set the ADS environment variables (see ./doc/cktsim/ADS_Simulator_Input_Syntax.html in ADS Help).
    - Test the installation from the terminal:

    .. code-block:: bat

        >>> where hpeesofsim

    - Unzap and the Simulated_Characterization_wrk workspace.
    - Specify the location of the workspace root directory in the following VARS:
        - _root in the DataImport schematic.
        - _root in the Modulated Characterization schematic.
        - Matlab Output.filename in the Modulated Characterization schematic.
    - Run the DataImport simulation to import I/Q data from the text files in ./data.
    - Run the Simulated Characterization simulation to test simulation environment.
    - Export the Simulated Characterization netlist from the schematic using.
        - Select DynamicLink>Top Level Netlist.
        - Save the Netlist as .\test_ADSCW_netlist.txt.
    - Test the Simulated Characterization simulation from the terminal.

    .. code-block:: bat

        >>> hpeesofsim .\test_ADSCW_netlist.txt

Anaconda
~~~~~~~~
Download and install `Anaconda for Python3 64-bit windows <https://www.continuum.io/downloads#windows>`_.

    - Make sure PYTHONPATH environment variable is not set during installation.
    - Install for "Just me".
    - Don't Add to Path
    - Make default version of python.

Test the installlation from the terminal:

.. code-block:: bat

    >>> %USERPROFILE%\Anaconda3\Library\bin\conda --version

Python 3.6
~~~~~~~~~~
Create a Python 3.6 Anaconda virtual environment.

.. code-block:: bat

    >>> cd %USERPROFILE%\Anaconda3\Scripts\
    >>> conda create -n py36 python=3.6 anaconda
    >>> activate py36

Test the installlation from the terminal:

.. code-block:: bat

    >>> where python

Register Python 3.6 in the Registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For external applications (installers) to recognize the virtual environment python 3.4, add it to the registry.

.. code-block:: bat

    >>> where python # Record the filepath to the python executable.

1. Open Registry using:
    - Start->Run: regedit
2. Navigate to HKEY_CURRENT_USER\\Software\\Python\\PythonCore\\3.4. (If this path does not exist export > modify > import another entry).
    - Modify HKEY_CURRENT_USER\\Software\\Python\\PythonCore\\3.4\\InstallPath and edit the default key with the output of the "where python" command.
    - Modify HKEY_CURRENT_USER\\Software\\Python\\PythonCore\\3.4\\InstallPath\\InstallGroup and edit the default key with Python 3.4
    - Modify HKEY_CURRENT_USER\\Software\\Python\\PythonCore\\3.4\\Help\\Main Python Documentation and edit the default key with C:\\\\Users\\\\username\\\\Anaconda3\\\\envs\\\\py34\\Doc\\\\python444.chm
    - Modify HKEY_CURRENT_USER\\Software\\Python\\PythonCore\\3.4\\PythonPath\ and edit the default key with C:\\Users\\username\\Anaconda3\\envs\\py34\\Lib;C:\\Users\\username\\Anaconda3\\envs\\py34\\DLLs;

3. Logout to apply registry changes.

Scikit-RF
~~~~~~~~~
Install Scikit-RF using conda as follows:

.. code-block:: bat

    >>> conda install scikit-rf

Test the installlation from the terminal:

.. code-block:: bat

    >>> python
    >>> import skrf


CommPy
~~~~~~
Install CommPy using the git source distribution

.. code-block:: bat

    >>> git clone https://github.com/veeresht/CommPy.git
    >>> cd CommPy
    >>> python setup.py install

Parmiko
~~~~~~~
Install Parmiko using conda as follows:

.. code-block:: bat

    >>> conda install paramiko

Test the installation from the terminal:

.. code-block:: bat

    >>> python
    >>> import paramiko

Shiboken/PySide2
~~~~~~~~~~~~~~~~
Build Shiboken/Shiboken Generator/PySide2 from source as follows:

.. code-block:: bat

    >>> git clone --recursive https://code.qt.io/pyside/pyside-setup
    >>> cd pyside-setup && git checkout 5.12
    >>> python setup.py build --qmake=%QT_DIR%\bin\qmake.exe --build-tests --ignore-git --jobs=8
    >>> python setup.py install --qmake=%QT_DIR%\bin\qmake.exe --build-tests --ignore-git --jobs=8

Test the installlation from the terminal:

.. code-block:: bat

    >>> which shiboken2
    >>> which pyside2-rcc
    >>> which pyside2-uic


PyTorch
~~~~~~~

Compile PyTorch from sorce as follows:

 .. code-block:: bash

    >>> conda install numpy pyyaml mkl mkl-include setuptools cmake cffi typing
    >>>
    >>> REM Download MKL files
    >>> curl https://s3.amazonaws.com/ossci-windows/mkl_2018.2.185.7z -k -O
    >>> 7z x -aoa mkl_2018.2.185.7z -omkl

    >>> REM Download MAGMA files
    >>> REM cuda100 is also available for `CUDA_PREFIX`. There are also 2.4.0 binaries for cuda80/cuda92.
    >>> REM The configuration could be `debug` or `release` for 2.5.0. Only `release` is available for 2.4.0.
    >>> set CUDA_PREFIX=cuda90
    >>> set CONFIG=release
    >>> curl -k https://s3.amazonaws.com/ossci-windows/magma_2.5.0_%CUDA_PREFIX%_%CONFIG%.7z -o magma.7z
    >>> 7z x -aoa magma.7z -omagma

    >>> REM Setting essential environment variables
    >>> set "CMAKE_INCLUDE_PATH=%cd%\\mkl\\include"
    >>> set "LIB=%cd%\\mkl\\lib;%LIB%"
    >>> set "MAGMA_HOME=%cd%\\magma"
    >>> # Add LAPACK support for the GPU if needed

    >>> choco install coreinfo
    >>> choco install glogg
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

    >>> conda install matplotlib

Test the installlation from the terminal:

.. code-block:: bash

    >>> python
    >>> import matplotlib

Toposort
~~~~~~~~
Install Toposort using pip as follows:

.. code-block:: bat

    >>> python -m pip install toposort

Test the installation from the terminal:

.. code-block:: bat

    >>> python
    >>> import toposort

PyVisa
------
Install PyVisa using pip as follows:

.. code-block:: bat

    >>>> python -m pip install -U pyvisa

Test the installlation from the terminal:

.. code-block:: bat

    >>> python
    >>> import visa

Nose-Exclude
~~~~~~~~~~~~
Install Nose-Exclude using pip as follows:

.. code-block:: bat

    >>> python -m pip install nose-exclude

Test the installation from the terminal:

.. code-block:: bat

    >>> python
    >>> import nose_exclude

Sphinx Bootstrap Theme
~~~~~~~~~~~~~~~~~~~~~~
Install Sphinx Bootstrap Theme using pip as follows:

.. code-block:: bat

    >>> python -m pip install sphinx_bootstrap_theme

Test the installation from the terminal:

.. code-block:: bat

    >>> python
    >>> import sphinx_bootstrap_theme

PyWin32
~~~~~~~
Install PyPiWin32 using pip as follows:

.. code-block:: bat

    >>> C:\Windows\System32\UserAccountControlSettings.exe
    >>> python -m pip install pypiwin32


Test the installlation from the terminal:

.. code-block:: bat

    >>> python
    >>> import win32com

Winshell
~~~~~~~~

Install Winshell using pip as follows:

.. code-block:: bat

    >>> python -m pip install winshell

Test the installlation from the terminal:

.. code-block:: bat

    >>> python
    >>> import winshell

Python-PPTX
~~~~~~~~~~~

Install Winshell using pip as follows:

.. code-block:: bat

    >>> python -m pip install python-pptx

Test the installlation from the terminal:

.. code-block:: bat

    >>> python
    >>> import pptx

Windows COM Instrument Tips
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Follow the instructions for each COM connected instrument, but also make sure the following is applied:

    1. Always run Windows Command prompt with "Run as Administrator".
    2. Make sure to register all COM servers on the client PC.
    3. When asked to enter machine name, use the fixed IP address eg) "10.0.0.10".
    4. Make sure both machines (PC and instrument) allow the com server application through Windows Firewall:
        a. Open Control Panel -> System and Security -> Windows Firewall.
        b. Select "Allow a program or features through Windows Firewall".
    5. Ensure that both machines (PC and instrument) have the same login & password.
        a. This not necessary, but could help.
    6. Connect using COM in 3-ways:
        a. Connect using a VB script (This should always work).
        b. Connect using local win32com.client.Dispatch(prog_id) and run a command.
        c. Connect using remote win32com.client.DispatchEx(prog_id, machine_name) and run a command. (Best practice).

        .. code-block:: bat

            >>> from win32com.client import Dispatch, DispatchEx
            >>> machine_name = "127.0.0.1"
            >>> prog_id = "Excel.Application"
            >>> com = Dispatch(prog_id) # For local applications or remote applications with fixed machine name
            >>> com = DispatchEx(prog_id, machine_name) # For remote applications (Best practice)

