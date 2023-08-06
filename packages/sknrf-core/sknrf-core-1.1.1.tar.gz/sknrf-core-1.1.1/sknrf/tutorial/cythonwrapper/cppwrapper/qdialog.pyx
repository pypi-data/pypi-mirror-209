cdef extern from "QtGui/qapplication.h":
    cdef cppclass QApplication:
        QApplication(int &argc, char **argv, int application_flags) except +

cdef extern from "QtGui/qwidget.h":
    cdef cppclass QWidget:
        QWidget() except +
        void show()

cdef extern from "QtGui/qdialog.h":
    cdef cppclass QDialog(QWidget):
        QDialog() except +


cdef class PyQApplication:
    cdef QApplication *qapplication_ptr
    def __cinit__(self, int argc , char[::,::1] argv, int application_flags):
        if type(self) is PyQApplication:
            self.qapplication_ptr = new QApplication(argc, argv, application_flags)

    def __dealloc__(self):
        if type(self) is PyQApplication:
            del self.qapplication_ptr


cdef class PyQWidget:
    cdef QWidget *qwidget_ptr
    def __cinit__(self):
        if type(self) is PyQWidget:
            self.qwidget_ptr = new QWidget()

    def show(self):
        self.qwidget_ptr.show()

    def __dealloc__(self):
        if type(self) is PyQWidget:
            del self.qwidget_ptr


cdef class PyQDialog(PyQWidget):
    cdef QDialog *qdialog_ptr
    def __cinit__(self):
        if type(self) is PyQDialog:
            self.qdialog_ptr = new QDialog()
    def __dealloc__(self):
        if type(self) is PyQDialog:
            del self.qdialog_ptr
