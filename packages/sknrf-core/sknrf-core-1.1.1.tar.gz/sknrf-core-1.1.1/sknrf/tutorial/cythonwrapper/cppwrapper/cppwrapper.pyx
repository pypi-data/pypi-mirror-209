"""
    This tutorial demonstrates a c++ code wrapping using:

        1. A cython built-in c++ wrapping.
            - vector.h
        2. A user-defined c++ wrapping.
            -A(.h, .cpp)
        3. A Qt Widget Wrapper.
            - QtGui.QDialog

    In a user-defined wrapper the following build process is encapsulated by setup.py
    cython:
        A.h, rect.pxd, rect.pyx -> rect.cpp
    Compile:
        A.h, A.cpp, rect.cpp -> rect.o
    Link:
        rect.o -> rect(.so, .dll)

    How to Compile
    --------------
    Unix:
    $python setup.py build_ext --inplace
    (Generates a .so file)

    Windows
    $python setup.py build_ext --inplace  -c msvc2010
    (Generates a .pyd file)
"""

from libcpp.vector cimport vector

cpdef load_vector():
    cdef vector[int] vect
    cdef int i
    for i in range(10):
        vect.push_back(i)
    return vect

cpdef print_vector(vector[int] vect):
    for i in range(10):
        print(vect[i])
