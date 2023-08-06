cdef class Rectangle:
    cdef _Rectangle c_rect
    def __cinit__(self, int x0, int y0, int x1, int y1):
        self.c_rect = _Rectangle(x0, y0, x1, y1)
    @property
    def x0(self):
        return self.c_rect.x0
    @x0.setter
    def x0(self, x0):
        self.c_rect.x0 = x0
    def get_area(self):
        return self.c_rect.getArea()
    def get_size(self):
        cdef int width, height
        self.c_rect.getSize(&width, &height)
        return width, height
    def move(self, dx, dy):
        self.c_rect.move(dx, dy)
