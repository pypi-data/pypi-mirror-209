cmake_minimum_required(VERSION 3.18.0)
project(qrangeslider_top)
option(SKNRF_BUILD_DOC    "Build Docs"             OFF)
option(SKNRF_BUILD_EXTRA  "Build Extra Modules"    ON)
option(SKNRF_BUILD_PLUGIN "Build QtCreator Plugin" OFF)
option(SKNRF_BUILD_PY     "Build Python Binding"   ON)
option(SKNRF_BUILD_TEST   "Build Test"             OFF)

# Include
include("${PROJECT_SOURCE_DIR}/cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/cmake/doxygen.cmake")

# Top-Level Macros
## Find package only when it is not a subproject
if(NOT COMMAND find_package)
    macro(find_package)
        if(NOT ${ARGV0} IN_LIST subprojects)
            _find_package(${ARGV})
        endif()
    endmacro()
endif()

# List Subprojects
set(subprojects qrangeslider qrangesliderplugin)
add_subdirectory(view/src)
if(SKNRF_BUILD_PLUGIN)
    add_subdirectory(view/plugin)
endif()
if(SKNRF_BUILD_PY)
    add_subdirectory(view/shiboken)
endif()
#if(SKNRF_BUILD_TEST)
#    add_subdirectory(view/test)
#endif()
