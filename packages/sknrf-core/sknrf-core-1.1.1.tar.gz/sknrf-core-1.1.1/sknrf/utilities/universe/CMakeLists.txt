cmake_minimum_required(VERSION 3.18.0)
project(universe_top)

# Include
include("${PROJECT_SOURCE_DIR}/../../../cmake/root.cmake")

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
set(subprojects universe)
add_subdirectory(src)
add_subdirectory(shiboken)
