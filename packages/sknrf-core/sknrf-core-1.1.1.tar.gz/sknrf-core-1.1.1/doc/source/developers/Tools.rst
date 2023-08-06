..  figure:: ../_images/PNG/sknrf_logo.png
    :width: 500 pt
    :align: center

Tools
=====

This document defines the development tools in terms of: \*
Documentation Page \* Summarized purpose \* Licencing

Software Languages
------------------

.. raw:: html

   <table border="1" width="100%">
    <tr>
        <th width="25%">Name</th>
        <th width="50%">Description</th>
        <th width="25%">License</th>
    </tr>
    <tr>
        <td><a href="http://www.w3schools.com/js/default.asp"><img src="../_internal_images/PNG/javascript_logo.png" /></a></td>
        <td>Dynamically-typed, interpreted language for deployment in front-end web applications
            <UL>
                <LI>Client-side webpage scripting.</LI>
                <LI>E-Commerce and user-forums available for purchase.</LI>
            </UL>
        </td>
        <td>
            <UL>
                <LI>License: Public</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://www.python.org"><img src="../_internal_images/PNG/python_logo.png" /></a></td>
        <td>Dynamically-type, object-oriented, interpreted language for deployment of cross-platform executable/library bytecode</td>
        <td>
            <UL>
                <LI>License: Python Software Foundation</LI>
                <LI>BSD-Like: Yes</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://www.cplusplus.com"><img src="../_internal_images/PNG/cpp_logo.png" /></a></td>
        <td>Static-typed, object-oriented, compiled language for deployment of native PC executable/library binaries</td>
        <td>
            <UL>
                <LI>License: Public</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://www.asic-world.com/verilog/veritut.html">Verilog</a></td>
        <td>Static-typed, hardware description language (HDL), for deployment on field-programmable gate array</td>
        <td>
            <UL>
                <LI>License: IEEE1364-2005</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://www.cmake.org"><img src="../_internal_images/PNG/cmake_logo.png" /></a></td>
        <td>Cross-platform, open-source build system. CMake is a family of tools designed to build, test and package software.</td>
        <td>
        <UL>
            <LI>License: BSD</LI>
            <LI>BSD-Like: Yes</LI>
        </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://docutils.sourceforge.net/rst.html">reStructuredText</a></td>
        <td>Lightweight Markdown language capable of generating HTML, PDF, EPub, or man formats</td>
        <td>
            <UL>
            <LI>License: Public</LI>
            <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
   </table>

Python Packages (Libraries)
---------------------------

.. raw:: html

   <table width="100%">
    <tr>
        <th width="25%">Name</th>
        <th width="50%">Description</th>
        <th width="25%">License</th>
    </tr>
    <tr>
        <td width="25%"><a href="https://store.continuum.io/cshop/anaconda/"><img src="../_internal_images/PNG/anaconda_logo.png" /></a></td>
        <td>Python distribution for large-scale data processing, predictive analytics, and scientific computing.
            <UL>
                <LI>Python package manager installed to the local user directory.</LI>
                <LI>Containins nearly all of the packages listed in this table.</LI>
                <LI>Python packages can be installed or updated via command-line utility.</LI>
                <LI>Virtual python environments can be created for testing new packager versions without administrator priveleges.</LI>
                <LI>Local development python environments do not overright the system python installation.</LI>
            </UL>
        </td>
        <td>
            <UL>
                <LI>License: ???</LI>
                <LI>BSD-Like: ???</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://pypi.python.org/pypi">pip</a></td>
        <td>Built-In command line install any package from Python Package Index
            <UL>
                <LI>Python package manager installed to the global system directory.</LI>
                <LI>Contains minimal python installation.</LI>
                <LI>Python packages can be installed or updated via command-line utility.</LI>
            </UL>
        </td>
        <td>
            <UL>
                <LI>License: MIT</LI>
                <LI>BSD-Like: Yes</LI>
            </UL>
        </td>
        </tr>
    <tr>
        <td><a href="http://www.numpy.org"><img src="../_internal_images/PNG/numpy_logo.png" /></a></td>
        <td>
        N-dimensional array package
            <UL>
                <LI>More memory efficient that python List type, with vector operations implemented in C.</LI>
                <LI>Data is interpreted in 2 ways:</LI>
                <OL>
                    <LI>As N dimensional Arrays (for data buffers)</LI>
                    <LI>2D Matrix types (for linear algebra).</LI>
                </OL> 
                <LI>Algebra operations are implemented in 2 ways:</LI>
                <OL>
                    <LI>Short-hand convenience operators eg.(d = (a+b)*c).</LI>
                    <LI>Memory efficient "ufuncs" that avoid temporary variables multiply eg.(sum(a,b,out=d),c,out=d).</LI>
                </OL>
            </UL>
        </td>
        <td>
            <UL>
                <LI>License: BSD</LI>
                <LI>BSD-Like: Yes</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://docs.scipy.org/doc/scipy/reference/fftpack.html"><img src="../_internal_images/PNG/scipy_logo.png" /></a></td>
        <td>Scientific Library for Python
        <UL>
            <LI>A large linear algebra implementation of LINPAC and BLAS that uses numpy arrays.
            <LI>Slowly being broken up into separate scikits.
            <LI>Useful for fft and reading Matlab database files.
        </UL>
        </td>
        <td>
        <UL>
        <LI>License: BSD
        <LI>BSD-Like: Yes
        </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://scikit-rf-web.readthedocs.org"><img src="../_internal_images/PNG/scikit-rf_logo.png" /></a></td>
        <td>
        Package for RF/Microwave engineering
        <UL>
            <LI>RF tools, mainly centered around network theory.
            <LI>Calibration and De-embedding.
            <LI>RF plotting tools implemented in Matplotlib.
        </UL>
        </td>
        <td>
        <UL>
        <LI>License: BSD
        <LI>BSD-Like: Yes
        </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://matplotlib.org"><img src="../_internal_images/PNG/matplotlib_logo.png" /></a></td>
        <td>
        2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.
        <UL>
            <LI>A central Python analytical plotting library that many other libraries use.</LI>
            <LI>Very comprehensive, very interactive, but not suitable for real-time plotting.</LI>
            <LI>Can be embedded in Qt applications and IPython notebooks.</LI>
            <LI>Two programming modes:</LI>
            <OL>
                <LI>State-based Matlab-Like pyplot for interactive plotting commands (usefull for IPython notebook).</LI>
                <LI>Full object-oriented API for software development.</LI>
            </OL>
        </UL>
        </td>
        <td>
        <UL>
            <LI>License: PSF-based</LI>
            <LI>BSD-Like: Yes</LI>
        </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://plot.ly"><img src="../_internal_images/PNG/plotly_logo.png" /></a></td>
        <td>Online graphing, analytics, and stats tools for individuals and collaboration, as well as scientific graphing libraries for Python, R, MATLAB, Perl, Julia, Arduino, and REST.
            <UL>
                <LI>Web-based post-processing of data stored on a server.</LI>
                <LI>Can convert Matplotlib plots to online plots.</LI>
                <LI>Python, R, MATLAB, Node.js, Julia, and Arduino and a REST API.</LI>
                <LI>Can be embedded inside a IPython notebook or inside a custom Javascript dashboard using Plotly.js.</LI>
                <LI>Hosted on external or internal server.</LI>
                <LI>Implemented in Python, Django, and JavaScript.</LI>
            </UL>
        </td>
        <td>
            <UL>
                <LI>License: Commercial</LI>
                <LI>BSD-Like: No</LI>
                <LI>Pricing: $60/month/organization</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://www.pytables.org"><img src="../_internal_images/PNG/pytables_logo.png" /></a></td>
        <td>Managing hierarchical datasets and designed to efficiently and easily cope with extremely large amounts of data.
            <UL>
                <LI>Binding HDF5 databases (used in .mat files) with NumPy arrays.</LI>
                <LI>Useful for large datasets or hierarchical datasets.</LI>
                <LI>Data can be access from memory or disk using NumPy API.</LI>
            </UL>
        </td>
        <td>
            <UL>
                <LI>License: BSD</LI>
                <LI>BSD-Like: Yes</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://nose.readthedocs.org/en/latest/">nose</a></td>
        <td>Extends unittest to make batch testing easier
            <UL>
                <LI>Enhancement of built-in Unit testing.</LI>
                <LI>Good for running unit-tests in batches.</LI>
            </UL>
        </td>
        <td>
            <UL>
                <LI>License: LGPL</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://sphinx-doc.org"><img src="../_internal_images/PNG/sphinx_logo.png" /></a></td>
        <td>Makes it easy to create intelligent and beautiful documentation
            <UL>
                <LI>Web Docs are written using reStructured Text (.rst) which is converted to HTML.</LI>
                <LI>Web API is autogenerated from comments in Python/C++ code.</LI>
            </UL>
        </td>
        <td>
            <UL>
                <LI>License: BSD</LI>
                <LI>BSD-Like: Yes</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://wiki.qt.io/PySide"><img src="../_internal_images/PNG/pyside_logo.png" /></a></td>
        <td>Python bindings for the Qt.
            <UL>
                <LI>C++ wrappers of Qt4 that are compiled as shared objects (.so).</LI>
                <LI>Command line tool that converts Qt Designer (.ui) files to python (.py) files.</LI>
            </UL>
        </td>
        <td>
            <UL>
                <LI>License: LGPL</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://shiboken.readthedocs.org/en/latest/">Shiboken</a></td>
        <td>Plugin (front-end) for Generator Runner. It generates bindings for C++ libraries using CPython source code.
            <UL>
                <LI>CPython wrapper generator that binds C++ objects (Qt) to Python objects.</LI>
                <LI>Supports cross-language inheritance, overloading, and encapsulation.</LI>
                <LI>Basic support for C++ container types and no support for C++ template classes.</LI>
            </UL>
        </td>
        <td>
            <UL>
                <LI>License: LGPL</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://www.boost.org/doc/libs/1_58_0/libs/python/doc/">Boost.Python</a></td>
        <td>A C++ library which enables seamless interoperability between C++ and the Python programming language.
            <UL>
                <LI>C++ template wrapper generator that binds C++ objects to Python objects.</LI>
                <LI>Better support for C++ containers with dynamic types (eg. NumPy arrays).</LI>
                <LI>Generates very large binary files.</LI>
            </UL>
        </td>
        <td>
            <UL>
                <LI>License: BSL</LI>
                <LI>BSD-Like: ???</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://github.com/ndarray/Boost.NumPy">Boost.NumPy</a></td>
        <td>Boost.NumPy is an extension for Boost.Python that adds NumPy support.</td>
        <td>
            <UL>
                <LI>License: BSL</LI>
                <LI>BSD-Like: ???</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://cython.org"><img src="../_internal_images/PNG/cython_logo.png" /></a></td>
        <td>Optimising static compiler for both the Python programming language and the extended Cython programming language
            <UL>
                <LI>Used to bind C and Python
                <OL>
                    <LI>Convert any Python (.py) to Cython (.pyc) by changing the file extension.</LI>
                    <LI>Add Cython specific syntax including static types, function type information, and disable limit checking to optimize code.</LI>
                    <LI>Compile as a shared object (.so) and import into Python.</LI>
                </OL>
            </UL>
        </td>
        <td>
            <UL>
                <LI>License: Apache</LI>
                <LI>BSD-Like: Yes</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://numba.pydata.org">Numba</a></td>
        <td>With a few annotations, array-oriented and math-heavy Python code can be just-in-time (JIT) compiled to native machine instructions, similar in performance to C, C++ and Fortran, without having to switch languages or Python interpreters.
            <UL>
                <LI>Just-In-Time (JIT) compiler that uses LLVM compiler to compile Python code on the fly.</LI>
                <LI>The code is compiled on first execution and may produce lag.</LI>
                <LI>Can be used to optimize Python code without converting to Cython using (@)decorators.</LI>
                <OL>
                    <LI>Add "@jit" for lazy function optimization.</LI>
                    <LI>Add addtional function type information for better optimization.</LI>
                </OL>
            </UL>
        </td>
        <td>
            <UL>
                <LI>License: BSD</LI>
                <LI>BSD-Like: Yes</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://www.paramiko.org">Paramiko</a></td>
        <td>Implementation of the SSHv2 protocol, providing both client and server functionality.</td>
        <td>
            <UL>
                <LI>License: LGPL</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://www.djangoproject.com"><img src="../_internal_images/PNG/django_logo.png" /></a></td>
        <td>High-level Python Web framework that encourages rapid development and clean, pragmatic design</td>
        <td>
            <UL>
                <LI>License: BSD</LI>
                <LI>BSD-Like: Yes</LI>
            </UL>
        </td>
    </tr>
   </table>

C++ Libraries
-------------

.. raw:: html

   <table width="100%">
    <tr>
        <th width="25%">Name</th>
        <th width="50%">Description</th>
        <th width="25%">License</th>
    </tr>
    <tr>
        <td><a href="http://doc.qt.io"><img src="../_internal_images/PNG/qt_logo.png" /></a></td>
        <td>Cross-platform application framework that is widely used for developing application software.</td>
        <td>
            <UL>
            <LI>License: LGPL</LI>
            <LI>BSD-Like: Yes</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://www.boost.org"><img src="../_internal_images/PNG/boost_logo.png" /></a></td>
        <td>Provide support for tasks and structures such as linear algebra, pseudorandom number generation, multithreading, image processing, regular expressions, and unit testing</td>
        <td>
            <UL>
                <LI>License: BSD</LI>
                <LI>BSD-Like: Yes</LI>
            </UL>
        </td>
    </tr>
   </table>

Productivity Tools
------------------

.. raw:: html

   <table width="100%">
    <tr>
        <th width="25%">Name</th>
        <th width="50%">Description</th>
        <th width="25%">License</th>
    </tr>
    <tr>
        <td><a href="https://products.office.com/en-CA/"><img src="../_internal_images/PNG/ms-office_logo.png" /></a></td>
        <td>General-purpose document generation</td>
        <td>
            <UL>
                <LI>License: Proprietary</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://slack.zendesk.com/hc/en-us"><img src="../_internal_images/PNG/slack_logo.png" /></a></td>
        <td>All your communication in one place, integrating with the tools and services you use every day.</td>
        <td>
            <UL>
                <LI>License: Proprietary</LI>
                <LI>BSD-Like: No</LI>
                <LI>Price: $96/person</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://www.gmail.com"><img src="../_internal_images/PNG/gmail_logo.png" /></a></td>
        <td>Email and Google Account</td>
        <td>
            <UL>
                <LI>License: Proprietary</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://www.google.ca/drive/"><img src="../_internal_images/PNG/google-drive_logo.png" /></a></td>
        <td>Cloud file storage for collaboration</td>
        <td>
            <UL>
                <LI>License: Proprietary</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://mercurial.selenic.com"><img src="../_internal_images/PNG/mercurial_logo.png" /></a></td>
        <td>A cross-platform, distributed revision control tool for software developer.</td>
        <td>
            <UL>
                <LI>License: Proprietary</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://tortoisehg.bitbucket.org"><img src="../_internal_images/PNG/tortoise-hg_logo.png" /></a></td>
        <td>Shell extension and a series of applications for the Mercurial distributed revision control system.</td>
        <td>
            <UL>
                <LI>License: Proprietary</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://bitbucket.org/"><img src="../_internal_images/PNG/bit-bucket_logo.png" /></a></td>
        <td>A web-based hosting service for projects that use either the Mercurial (since launch) or Git (since October 2011[1]) revision control systems.</td>
        <td>
            <UL>
                <LI>License: Proprietary</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://ipython.org"><img src="../_internal_images/PNG/ipython_logo.png" /></a></td>
        <td>Rich console/notepad architecture for interactive computing</td>
        <td>
            <UL>
                <LI>License: BSD</LI>
                <LI>BSD-Like: Yes</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://www.jetbrains.com/pycharm/"><img src="../_internal_images/PNG/pycharm_logo.png" /></a></td>
        <td>Python, Javascript intellegent interactive development environment (IDE)</td>
        <td>
            <UL>
                <LI>License: Public</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://doc.qt.io/qtcreator/"><img src="../_internal_images/PNG/qt-creator_logo.png" /></a></td>
        <td>Cross-platform IDE (integrated development environment) tailored to the needs of Qt developers.</td>
        <td>
            <UL>
                <LI>License: LGPL</LI> 
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://www.virtualbox.org"><img src="../_internal_images/PNG/virtual-box_logo.png" /></a></td>
        <td>A powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.</td>
        <td>
            <UL>
                <LI>License: GPL</LI> 
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="https://www.lucidchart.com/"><img src="../_internal_images/PNG/lucid-chart_logo.png" /></a></td>
        <td>A web-based diagramming software which allows users to collaborate and work together in real time to create flowcharts, organisational charts, website wireframes, UML designs, mind maps, software prototypes, and many other diagram types.</td>
        <td>
            <UL>
                <LI>License: Proprietary</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
    <tr>
        <td><a href="http://www.papersapp.com"><img src="../_internal_images/PNG/papers_logo.png" /></a></td>
        <td>Primarily used to organize references and maintain a library of PDF documents</td>
        <td>
            <UL>
                <LI>License: Proprietary</LI>
                <LI>BSD-Like: No</LI>
            </UL>
        </td>
    </tr>
   </table>
