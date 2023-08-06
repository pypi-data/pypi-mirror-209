cmake_minimum_required(VERSION 3.18.0)
project(universepy)

# Include
include("${PROJECT_SOURCE_DIR}/../../../../cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/../../../../cmake/export_package.cmake")

# Variables
pyside_config(--shiboken-generator-path shiboken_generator_path)
pyside_config(--shiboken-generator-include-path shiboken_include_dir 1)
pyside_config(--shiboken-module-shared-libraries-cmake shiboken_shared_libraries 0)

# Dependencies
find_package(universe REQUIRED)

# Build
## Generate the binding cpp files.
set(generated_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/universe/universe_module_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/universe/icecream_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/universe/truck_wrapper.cpp)
set(BINDINGS_H ${CMAKE_CURRENT_SOURCE_DIR}/bindings.h)
set(BINDINGS_XML ${CMAKE_CURRENT_SOURCE_DIR}/bindings.xml)
add_custom_command(OUTPUT ${generated_sources}
                   COMMAND ${shiboken_generator}
                   ${SHIBOKEN_OPT} ${BINDINGS_H} ${BINDINGS_XML}
                   DEPENDS ${BINDINGS_H} ${BINDINGS_XML} universe::universe
                   IMPLICIT_DEPENDS CXX ${BINDINGS_H}
                   WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                   COMMENT "Running binding generator for ${CMAKE_CURRENT_SOURCE_DIR}.")
## Build the Python binding.
add_library(universepy MODULE ${generated_sources})
## Define Python module_name.so
set_target_properties(universepy PROPERTIES VERSION ${SKNRF_VERSION} SOVERSION ${SKNRF_VERSION_MAJOR})
set_target_properties(universepy PROPERTIES PREFIX "")
set_target_properties(universepy PROPERTIES OUTPUT_NAME "universe")
set_target_properties(universepy PROPERTIES INSTALL_RPATH "$ORIGIN/../lib") 
if(WIN32)
    set_target_properties(universepy PROPERTIES SUFFIX ".pyd")
endif()

# Include Flags
target_include_directories(universepy PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../src)
target_include_directories(universepy PRIVATE ${shiboken_include_dir})
target_include_directories(universepy PRIVATE ${PYTHON_INC})

# Link Flags
target_link_libraries(universepy PRIVATE universe::universe)	
if (WIN32)
    target_link_libraries(universepy PRIVATE ${CONDA_PREFIX}/libs/python${PYTHONVERSION}${CMAKE_STATIC_LIBRARY_SUFFIX})
elseif(APPLE)
    set_target_properties(universepy PROPERTIES LINK_FLAGS "-undefined dynamic_lookup")
endif()
target_link_libraries(universepy PRIVATE ${shiboken_shared_libraries})	

# Install
if (WIN32)
    install (TARGETS universepy EXPORT universepyTargets
             DESTINATION bin)
else()
    install (TARGETS universepy EXPORT universepyTargets
             DESTINATION lib)
endif()
export_package(universepy ${SKNRF_VERSION})
