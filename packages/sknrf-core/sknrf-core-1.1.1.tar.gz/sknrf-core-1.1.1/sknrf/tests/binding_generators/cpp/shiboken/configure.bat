@ECHO ON
SET SRC_DIR=%~dp0\..\src
SET QT_INC=%QT_DIR%\include
SET PYSIDE_INC=%PYTHON_PACKAGES%\PySide\include\PySide
SET QTTYPESYSTEM=%PYTHON_PACKAGES%\PySide\typesystems

shiboken --include-paths=%SRC_DIR%;%QT_INC%;%PYSIDE_INC% ^
         --typesystem-paths=.\data;%QTTYPESYSTEM% ^
         --output-directory=. ^
         --enable-pyside-extensions ^
         --avoid-protected-hack ^
         .\data\global.h ^
         .\data\typesystem.xml
