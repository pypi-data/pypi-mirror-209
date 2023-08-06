cmake_minimum_required(VERSION 3.18.0)
project(qprogressindicatorpy)

# Include
include("${PROJECT_SOURCE_DIR}/../../cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/../../cmake/export_package.cmake")

# Variables
pyside_config(--shiboken-generator-path shiboken_generator_path)
pyside_config(--shiboken-generator-include-path shiboken_include_dir 1)
pyside_config(--shiboken-module-shared-libraries-cmake shiboken_shared_libraries 0)

find_package(qprogressindicator REQUIRED)

# Build
## Generate the binding cpp files.
set(generated_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/qprogressindicator/qprogressindicator_module_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qprogressindicator/qprogressindicator_wrapper.cpp)
set(BINDINGS_H ${CMAKE_CURRENT_SOURCE_DIR}/bindings.h)
set(BINDINGS_XML ${CMAKE_CURRENT_SOURCE_DIR}/bindings.xml)
add_custom_command(OUTPUT ${generated_sources}
                   COMMAND ${shiboken_generator}
                   "--enable-pyside-extensions"
                   ${SHIBOKEN_OPT} ${BINDINGS_H} ${BINDINGS_XML}
                   DEPENDS ${BINDINGS_H} ${BINDINGS_XML}
                   WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                   COMMENT "Running binding generator for ${CMAKE_CURRENT_SOURCE_DIR}.")
add_custom_target(qprogressindicatorpy_shiboken_generator ALL
    DEPENDS ${generated_sources}
)

## Build the Python binding.
add_library(qprogressindicatorpy MODULE ${generated_sources})
## Define Python module_name.so
set_target_properties(qprogressindicatorpy PROPERTIES PREFIX "")
set_target_properties(qprogressindicatorpy PROPERTIES OUTPUT_NAME "qprogressindicator")
if(WIN32)
    set_target_properties(qprogressindicatorpy PROPERTIES SUFFIX ".pyd")
    target_compile_definitions(qprogressindicatorpy PRIVATE QPROGRESSINDICATOR_USE_LIBRARY) # export WIN32 symbols in .lib file
endif()

# Include Flags
target_include_directories(qprogressindicatorpy PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../src)
target_include_directories(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide6/include)
target_include_directories(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide6/include/QtWidgets)
target_include_directories(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide6/include/QtGui)
target_include_directories(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide6/include/QtCore)
target_include_directories(qprogressindicatorpy PRIVATE ${shiboken_include_dir})
target_include_directories(qprogressindicatorpy PRIVATE ${PYTHON_INC})
target_include_directories(qprogressindicatorpy PRIVATE ${Qt6Widgets_INCLUDE_DIRS})

# Link Flags
target_link_libraries(qprogressindicatorpy PRIVATE qprogressindicator::qprogressindicator)
if(WIN32)
    target_link_libraries(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide6/pyside6.cp${Python_VERSION_MAJOR}${Python_VERSION_MINOR}-win_amd64${CMAKE_STATIC_LIBRARY_SUFFIX})
    target_link_libraries(qprogressindicatorpy PRIVATE ${CONDA_PREFIX}/libs/python${PYTHONVERSION}${CMAKE_STATIC_LIBRARY_SUFFIX})
elseif(APPLE)
    target_link_libraries(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide6/libpyside6.cpython-${Python_VERSION_MAJOR}${Python_VERSION_MINOR}-darwin.${Qt_VERSION_MAJOR}.${Qt_VERSION_MINOR}${CMAKE_SHARED_LIBRARY_SUFFIX})
    set_target_properties(qprogressindicatorpy PROPERTIES LINK_FLAGS "-undefined dynamic_lookup")
else()
    target_link_libraries(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide${Qt_VERSION_MAJOR}/libpyside${Qt_VERSION_MAJOR}.abi${Python_VERSION_MAJOR}${CMAKE_SHARED_LIBRARY_SUFFIX}.${Qt_VERSION_MAJOR}.${Qt_VERSION_MINOR})
endif()
target_link_libraries(qprogressindicatorpy PRIVATE ${shiboken_shared_libraries})
target_link_libraries(qprogressindicatorpy PRIVATE Qt6::Widgets)
target_link_libraries(qprogressindicatorpy PRIVATE Qt6::Gui)
target_link_libraries(qprogressindicatorpy PRIVATE Qt6::Core)

# Install
if (WIN32)
    install (TARGETS qprogressindicatorpy EXPORT qprogressindicatorpyTargets
             DESTINATION bin)
else()
    install (TARGETS qprogressindicatorpy EXPORT qprogressindicatorpyTargets
             DESTINATION lib)
endif()
export_package(qprogressindicatorpy ${SKNRF_VERSION})
