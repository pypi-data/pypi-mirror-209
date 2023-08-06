cmake_minimum_required(VERSION 3.18.0)
project(universe)

# Include
include("${PROJECT_SOURCE_DIR}/../../../../cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/../../../../cmake/export_package.cmake")

# Build
add_library(universe SHARED
    icecream.cpp
    truck.cpp)
set(headers
    icecream.h
    truck.h)
set_target_properties(universe PROPERTIES VERSION ${SKNRF_VERSION} SOVERSION ${SKNRF_VERSION_MAJOR})
set_target_properties(universe PROPERTIES PUBLIC_HEADER "${headers}")
target_compile_definitions(universe PRIVATE BINDINGS_BUILD) # export WIN32 symbols in .lib file


# Install
install(TARGETS universe EXPORT universeTargets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
    PUBLIC_HEADER DESTINATION include)
export_package(universe ${SKNRF_VERSION})
