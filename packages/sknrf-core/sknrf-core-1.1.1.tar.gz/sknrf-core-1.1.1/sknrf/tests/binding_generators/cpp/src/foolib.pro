win32: SKNRF_DIR = $$system(echo %SKNRF_DIR%)
unix: SKNRF_DIR = $$system(echo $SKNRF_DIR)
include($$SKNRF_DIR/root.pri)

TEMPLATE = lib
TARGET = foolib
DEFINES += FOOLIB_LIBRARY

SOURCES += \
    fooclass.cpp

HEADERS +=\
    FooLib_global.h \
    fooclass.h
