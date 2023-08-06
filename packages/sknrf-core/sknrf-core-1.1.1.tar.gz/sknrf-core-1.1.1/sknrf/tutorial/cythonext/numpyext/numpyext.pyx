"""
    This tutorial compares:

        1. Python code with numpy
        2. Cython code with typed memoryviews

    Supported Array Types
    ---------------------
    Cython supports the following numerical array types:

        1. numpy arrays: cdef np.ndarray[np.double_t, ndim=2] some_array
            - requires cimport numpy as np.
            - cython data types have "_t" suffix.
        2. Python/Cython memoryviews: cdef double[::, ::1] some_array
            - ::1 ensures the array is c-contiguous in memory.
        3. C Array: cdef double **some_array
            - Assumes data is c-contiguous (nparray.flags.c_contiguous == True)

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
        from nimimo.tutorial.cythonext.numpyext import numpy
        numpyext.python_sum(30)
        numpyext.cython_sum(30)

    Annotations
    -----------
    Annotations highlight the interactions with the python interpreter (yellow lines)
    cython numpyext.pyx -a
"""
import cython
import numpy as np
cimport numpy as np

from sknrf.utilities.profiler import time_it

@time_it
def numpy_sum(a):
    return np.sum(a)

@time_it
@cython.boundscheck(False) # Never index outside of the bounds of the array.
@cython.wraparound(False) # Eliminate support of negative indexing.
def cython_sum(double[::1] a): # contiguous 1D array of doubles
    cdef double s = 0.0
    cdef int i, n = a.shape[0]
    for i in range(n):
        s += a[i]
    return s
