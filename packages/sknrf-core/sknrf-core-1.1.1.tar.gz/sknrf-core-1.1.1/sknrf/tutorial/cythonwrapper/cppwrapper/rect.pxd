cdef extern from "A.h" namespace "shapes":
    cdef cppclass _Rectangle "shapes::A":
        _Rectangle() except +
        _Rectangle(int, int, int, int) except +
        int x0, y0, x1, y1
        int getArea()
        void getSize(int* width, int* height)
        void move(int, int)