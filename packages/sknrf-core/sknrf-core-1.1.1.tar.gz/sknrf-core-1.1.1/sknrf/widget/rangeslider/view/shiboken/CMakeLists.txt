cmake_minimum_required(VERSION 3.18.0)
project(qrangesliderpy)

# Include
include("${PROJECT_SOURCE_DIR}/../../cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/../../cmake/export_package.cmake")

# Variables
pyside_config(--shiboken-generator-path shiboken_generator_path)
pyside_config(--shiboken-generator-include-path shiboken_include_dir 1)
pyside_config(--shiboken-module-shared-libraries-cmake shiboken_shared_libraries 0)

find_package(qrangeslider REQUIRED)

# Build
## Generate the binding cpp files.
set(generated_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/qrangeslider/qrangeslider_module_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qrangeslider/qrangeslider_wrapper.cpp)
set(BINDINGS_H ${CMAKE_CURRENT_SOURCE_DIR}/bindings.h)
set(BINDINGS_XML ${CMAKE_CURRENT_SOURCE_DIR}/bindings.xml)
add_custom_command(OUTPUT ${generated_sources}
                   COMMAND ${shiboken_generator}
                   "--enable-pyside-extensions"
                   ${SHIBOKEN_OPT} ${BINDINGS_H} ${BINDINGS_XML}
                   DEPENDS ${BINDINGS_H} ${BINDINGS_XML}
                   WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                   COMMENT "Running binding generator for ${CMAKE_CURRENT_SOURCE_DIR}.")
add_custom_target(qrangesliderpy_shiboken_generator ALL
    DEPENDS ${generated_sources}
)

## Build the Python binding.
add_library(qrangesliderpy MODULE ${generated_sources})
## Define Python module_name.so
set_target_properties(qrangesliderpy PROPERTIES PREFIX "")
set_target_properties(qrangesliderpy PROPERTIES OUTPUT_NAME "qrangeslider")
if(WIN32)
    set_target_properties(qrangesliderpy PROPERTIES SUFFIX ".pyd")
    target_compile_definitions(qrangesliderpy PRIVATE QRANGESLIDER_USE_LIBRARY) # export WIN32 symbols in .lib file
endif()

# Include Flags
target_include_directories(qrangesliderpy PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../src)
target_include_directories(qrangesliderpy PRIVATE ${PYTHON_SP_DIR}/PySide6/include)
target_include_directories(qrangesliderpy PRIVATE ${PYTHON_SP_DIR}/PySide6/include/QtWidgets)
target_include_directories(qrangesliderpy PRIVATE ${PYTHON_SP_DIR}/PySide6/include/QtGui)
target_include_directories(qrangesliderpy PRIVATE ${PYTHON_SP_DIR}/PySide6/include/QtCore)
target_include_directories(qrangesliderpy PRIVATE ${shiboken_include_dir})
target_include_directories(qrangesliderpy PRIVATE ${PYTHON_INC})
target_include_directories(qrangesliderpy PRIVATE ${Qt6Widgets_INCLUDE_DIRS})

# Link Flags
target_link_libraries(qrangesliderpy PRIVATE qrangeslider::qrangeslider)
if(WIN32)
    target_link_libraries(qrangesliderpy PRIVATE ${PYTHON_SP_DIR}/PySide6/pyside6.cp${Python_VERSION_MAJOR}${Python_VERSION_MINOR}-win_amd64${CMAKE_STATIC_LIBRARY_SUFFIX})
    target_link_libraries(qrangesliderpy PRIVATE ${CONDA_PREFIX}/libs/python${PYTHONVERSION}${CMAKE_STATIC_LIBRARY_SUFFIX})
elseif(APPLE)
    target_link_libraries(qrangesliderpy PRIVATE ${PYTHON_SP_DIR}/PySide6/libpyside6.cpython-${Python_VERSION_MAJOR}${Python_VERSION_MINOR}-darwin.${Qt_VERSION_MAJOR}_${Qt_VERSION_MINOR}${CMAKE_SHARED_LIBRARY_SUFFIX})
    set_target_properties(qrangesliderpy PROPERTIES LINK_FLAGS "-undefined dynamic_lookup")
else()
    target_link_libraries(qrangesliderpy PRIVATE ${PYTHON_SP_DIR}/PySide${Qt_VERSION_MAJOR}/libpyside${Qt_VERSION_MAJOR}.abi${Python_VERSION_MAJOR}${CMAKE_SHARED_LIBRARY_SUFFIX}.${Qt_VERSION_MAJOR}.${Qt_VERSION_MINOR})
endif()
target_link_libraries(qrangesliderpy PRIVATE ${shiboken_shared_libraries})
target_link_libraries(qrangesliderpy PRIVATE Qt6::Widgets)
target_link_libraries(qrangesliderpy PRIVATE Qt6::Gui)
target_link_libraries(qrangesliderpy PRIVATE Qt6::Core)

# Install
if (WIN32)
    install (TARGETS qrangesliderpy EXPORT qrangesliderpyTargets
             DESTINATION bin)
else()
    install (TARGETS qrangesliderpy EXPORT qrangesliderpyTargets
             DESTINATION lib)
endif()
export_package(qrangesliderpy ${SKNRF_VERSION})
