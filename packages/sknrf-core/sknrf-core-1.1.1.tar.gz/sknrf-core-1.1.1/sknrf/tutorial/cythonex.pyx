from libc.stdlib cimport atoi

cdef extern from "math.h":
    double sin(double x)

def fib(n):
    a, b = 1, 1
    for i in range(n):
        a, b = a + b, a
    return a

def primes(int kmax):
    cdef int n, k, i
    cdef int p[1000]
    result = []
    if kmax > 1000:
        kmax = 1000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result

cdef parse_charptr_to_py_int(char* s):
    assert s is not NULL, "byte string value is NULL"
    return atoi(s)   # note: atoi() has no error detection!

def sin_test(char* x):
    return sin(parse_charptr_to_py_int(s=x))