.. sknrf documentation introduction file

..  figure:: ../_images/PNG/sknrf_logo.png
    :width: 500 pt
    :align: center

Shared Objects
==============

macOS
-----

Apple has several ways of locating shared libraries:

@executable_path : relative to the main executable
@loader_path : relative to the referring binary
@rpath : relative to any of a list of paths.
@rpath is the most recent addition, introduced in OS X 10.5.

If for instance you want to have your executable in Contents/MacOS and libraries in Contents/Libraries you could do the following:

install_name_tool -id @rpath/Libraries/lib_this.dylib   builddir/lib_this.dylib
and in the top-level executable set rpath with:

install_name_tool -add_rpath @loader_path/..  myexecutable
and:

install_name_tool -change builddir/lib_this.dylib @rpath/Libraries/lib_this.dylib myexecutable
Note: that the first path after -change must match exactly what is currently in the binary.

If you get lost otool -l -v myexecutable will tell you what load commands exactly are currently in the executable.

See man dyld and man install_name_tool for more information.


Linux
-----


Windows
-------


Anaconda
--------

Windows .dlls should be located in %PYTHON_DIR%\\Library\\bin
macOS .dlybs shouuld be located in $PYTHON_DIR/lib
Linux .so should be located in $PYTHON_DIR/lib

Python
------
Windows .so should be located in %PYTHON_DIR%\\DLLs
macOS .so should be located in %PYTHON_DIR%/lib/python3.6/lib-dynload
linux .so should be located in %PYTHON_DIR%/lib/python3.6/lib-dynload
