"""
    This tutorial compares:

        1. Pure python code.
        2. Cython code which adds static data types.

    How to Compile
    --------------
    Unix:
    $python setup.py build_ext --inplace
    (Generates a .so file)

    Windows
    $python setup.py build_ext --inplace  -c msvc2010
    (Generates a .pyd file)

    How to Run
    ----------
    $python
        from nimimo.tutorial.cythonext.pythonext import pythonext
        pythonext.python_fib(30)
        pythonext.cython_fib(30)

    Annotations
    -----------
    Annotations highlight the interactions with the python interpreter (yellow lines)
    cython pythonext.pyx
"""
import numpy as np

from sknrf.utilities.profiler import time_it

@time_it
def python_fib(n):
    a, b = 1.0, 1.0
    for i in range(n):
        a, b = a + b, a
    return a

@time_it
def cython_fib(int n):
    """ C Variables in a python function.
    """
    cdef int i, a, b
    a, b = 1, 1
    for i in range(n):
        a, b = a + b, a
    return a

def def_distance(x, y):
    return np.sum(x**2 - y**2)

cdef double cdef_distance(double *x, double *y, int n):
    """ C variables in a C function
    """
    cdef:
        int i
        float d = 0.0
    for i in range(n):
        d += (x[i]**2 - y[i]**2)
    return d

cpdef double cpdef_distance(double[:] x, double[:] y):
    """ Locally C function, External Python function.
    """
    cdef:
        int i
        int n = x.shape[0]
        double d = 0.0
    for i in range(n):
        d += (x[i]**2 - y[i]**2)
    return d


cdef class Particle(object):
    """ C Extension Types
    """
    cdef double psn[3]
    cdef double vel[3]
    cdef int id
    cdef list names # static list
    cdef dict name_to_id # static dict
    cdef object o # reference counted object

