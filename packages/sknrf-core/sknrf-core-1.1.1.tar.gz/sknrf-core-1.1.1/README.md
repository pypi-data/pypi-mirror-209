# scikit-nrf-core

## Build Flow

Building and Deploying Python code with native shared libraries
a continuously involving ordeal, hence I have provided the equivalent
CMake/Makefile command in comments to be relatable to C++. Internally
Cmake and Make are invoked. The build-flow currently uses setuptools,
which is deprecated in Python 3.12.

### Install Dependencies

See requirements.txt

### Environment Variables

   <table>
       <tr>
           <th> Variable </th>
           <th> Default Value </th>
           <th> Description </th>
       </tr>
       <tr>
           <td> LLVM_INSTALL_DIR </td>
           <td> ${HOME}/libclang </td>
           <td> libclang directory </td>
       </tr>
       <tr>
           <td> SKNRF_DIR </td>
           <td> import site ; site.getsitepackages()[0] </td>
           <td> Python sknrf-core Module Directory </td>
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

### Release Build

```bash
   python3 setup.py clean                                   # sudo make clean
   python3 setup.py config    `                             # cmake ..
   python3 setup.py build                                   # make
   python3 setup.py install                                 # sudo make install
 ```

`python3 setup.py install` will take a while to execute because it builds the python documentation. As an alternative `python3 setup.py develop`
creates the same outcome by symbolicly linking the src directory `sknrf` to a file in the `site-packages` folder. NOTE: This is a PYTHON-SPECIFIC
symbolic link that works cross-platform for PYTHON ONLY. You still need to `install` all other files as follows!

```bash
   python3 setup.py clean                                   # sudo make clean
   python3 setup.py config    `                             # cmake ..
   python3 setup.py build                                   # make
   python3 setup.py install_clib                            # sudo make install
   python3 setup.py install_data                            # sudo make install
   python3 setup.py develop                                 # All changes in the source directory are now installed instantly
   python3 setup.py install_doc                             # sudo make install
 ```

### Example

```bash
   python3 ${SKNRF_DIR}/sknrf/main.py
```

### Tests

```bash
   cd ${SKNRF_DIR}/sknrf ; nosetests --config=nose.cfg
```

### Runtime Configuration

`${SKNRF_DIR}/sknrf/sknrf.yml` contains runtime configuration settings. Beware of Environment Variables set in this file.
