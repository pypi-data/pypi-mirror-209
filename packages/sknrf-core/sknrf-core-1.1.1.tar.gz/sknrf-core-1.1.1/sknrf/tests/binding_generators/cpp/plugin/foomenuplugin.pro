win32: SKNRF_DIR = $$system(echo %SKNRF_DIR%)
unix: SKNRF_DIR = $$system(echo $SKNRF_DIR)
include($$SKNRF_DIR/root.pri)

CONFIG += designer plugin
CONFIG -= full-pkg-config
TEMPLATE = lib
TARGET = foomenuplugin
DEFINES += FOOMENUPLUGIN_LIBRARY

INCLUDEPATH += $$PWD/../src

LIBS += -L$$SKNRF_DIR/lib -lfoolib

SOURCES = foomenuplugin.cpp

HEADERS = foomenuplugin.h


