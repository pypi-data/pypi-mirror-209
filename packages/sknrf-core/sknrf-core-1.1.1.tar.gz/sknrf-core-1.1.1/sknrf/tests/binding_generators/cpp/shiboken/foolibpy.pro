win32: SKNRF_DIR = $$system(echo %SKNRF_DIR%)
unix: SKNRF_DIR = $$system(echo $SKNRF_DIR)
include($$SKNRF_DIR/root.pri)

TEMPLATE = lib
TARGET = foolibpy
DEFINES += FOOLIBBINDING_LIBRARY

# Pre-build
# message("Running Shiboken Binding Generator")
# win32: BINDING = $$system(configure.bat)
# unix: BINDING = $$system(sh configure.sh)

INCLUDEPATH += $$PYTHON_PACKAGES/PySide/include/PySide \
               $$PYTHON_PACKAGES/PySide/include/PySide/QtCore \
               $$PYTHON_PACKAGES/PySide/include/PySide/QtGui \
               $$PYTHON_PACKAGES/PySide/include/shiboken \
               $$PYTHON_DIR/include \
               $$PWD/../src


unix: INCLUDEPATH += $$PYTHON_DIR/include/python3.4m \

win32 {
    LIBS += -L$$PYTHON_DIR/libs -lpython34 \
            -L$$PYTHON_PACKAGES/PySide -lpyside-python3.4 \
            -L$$PYTHON_PACKAGES/PySide -lshiboken-python3.4
}
unix {
    LIBS += -L$$PYTHON_DIR/lib -lpython3.4m \
            -L$$PYTHON_PACKAGES/PySide -lpyside.cpython-34m \
            -L$$PYTHON_PACKAGES/PySide -lshiboken.cpython-34m
}
LIBS += -L$$SKNRF_DIR/lib -lfoolib


SOURCES += \
    foolib/foolib_module_wrapper.cpp \
    foolib/fooclass_wrapper.cpp \
    foolib/foomenu_wrapper.cpp

HEADERS += \
    foolib/foolib_python.h \
    foolib/fooclass_wrapper.h \
    foolib/foomenu_wrapper.h