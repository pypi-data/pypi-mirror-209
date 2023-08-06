#!/bin/sh
SRC_DIR=$PWD/../src

QT_INC=$QT_DIR/include
PYSIDE_INC=$PYTHON_PACKAGES/PySide/include/PySide
QTTYPESYSTEM=$PYTHON_PACKAGES/PySide/typesystems

shiboken --include-paths=$SRC_DIR:$QT_INC:$PYSIDE_INC \
         --typesystem-paths=./data:$QTTYPESYSTEM \
         --output-directory=. \
         --enable-pyside-extensions \
         --avoid-protected-hack \
         ./data/global.h \
         ./data/typesystem.xml
