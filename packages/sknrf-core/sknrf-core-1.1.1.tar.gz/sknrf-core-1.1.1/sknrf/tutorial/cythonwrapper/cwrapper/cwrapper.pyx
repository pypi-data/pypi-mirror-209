"""
    This tutorial demonstrates a c code wrapping using:

        1. A cython built-in c wrapping.
            - string.h
            - time.h
        2. A user-defined c wrapping.
            -calg.queue

    In a user-defined wrapper the following build process is encapsulated by setup.py
    cython:
        queue.h, cwrapper.pxd, cwrapper.pyx -> cwrapper.c
    Compile:
        queue.h, cwrapper.c -> cwrapper.o
    Link:
        queue(.so, .dll, .dylib), cwrapper.o -> cwrapper(.so, .dll)

    How to Compile
    --------------
    Unix:
    $python setup.py build_ext --inplace
    (Generates a .so file)

    Windows
    $python setup.py build_ext --inplace  -c msvc2010
    (Generates a .pyd file)
"""
cimport cqueue

cdef extern from "string.h": # Includes a header file
    # Import External C function
    int strlen(char *c) # Describe the function used

cdef extern from "time.h":
    struct tm:
        int tm_mday
        int tm_mon
        int tm_year

    ctypedef long time_t
    tm* localtime(time_t *timer)
    time_t time(time_t *tloc)


def get_len(char *message):
    """ Wrap the C function with a Python functon"""
    return strlen(message)

def get_time_data():
    """Wrap a C struct pointer"""
    cdef time_t t
    cdef tm* ts
    t = time(NULL)
    ts = localtime(&t)
    return ts.tm_mday, ts.tm_mon + 1, ts.tm_year


cdef class Queue:
    cdef cqueue.Queue* _c_queue
    def __cinit__(self):
        self._c_queue = cqueue.queue_new()
        if self._c_queue is NULL:
            raise MemoryError()

    def __bool__(self):
        return not cqueue.queue_is_empty(self._c_queue)

    cpdef append(self, int value):
        if not cqueue.queue_push_tail(self._c_queue,
                                      <void*>value):
            raise MemoryError()

    cdef c_extend(self, int* values, size_t count):
        cdef size_t i
        for i in range(count):
            if not cqueue.queue_push_tail(
                    self._c_queue, <void*>values[i]):
                raise MemoryError()

    def extend(self, values):
        for v in values:
            self.append(v)

    cpdef int peek(self) except? -1:
        value = <int>cqueue.queue_peek_head(self._c_queue)
        if value == 0:
            # this may mean that the queue is empty, or
            # that it happens to contain a 0 value
            if cqueue.queue_is_empty(self._c_queue):
                raise IndexError("Queue is empty")
        return value

    cpdef int pop(self) except? -1:
        if cqueue.queue_is_empty(self._c_queue):
            raise IndexError("Queue is empty")
        return <int>cqueue.queue_pop_head(self._c_queue)

    def __dealloc__(self):
        if self._c_queue is not NULL:
            cqueue.queue_free(self._c_queue)
