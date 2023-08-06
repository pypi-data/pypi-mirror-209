cmake_minimum_required(VERSION 3.18.0)
project(qtpropertybrowserpy)

# Include
include("${PROJECT_SOURCE_DIR}/../../cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/../../cmake/export_package.cmake")

# Variables
pyside_config(--shiboken-generator-path shiboken_generator_path)
pyside_config(--shiboken-generator-include-path shiboken_include_dir 1)
pyside_config(--shiboken-module-shared-libraries-cmake shiboken_shared_libraries 0)

find_package(qtpropertybrowser REQUIRED)

# Build
## Generate the binding cpp files.
set(generated_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtproperty_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtvariantproperty_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtbrowseritem_wrapper.cpp

    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtabstractpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtgrouppropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtintpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtboolpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtdoublepropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtcomplexpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtvectorcomplexpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtstringpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtfilepropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtdatepropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qttimepropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtdatetimepropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtkeysequencepropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtcharpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtlocalepropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtpointpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtpointfpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtsizepropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtsizefpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtrectpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtrectfpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtenumpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtflagpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtsizepolicypropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtfontpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtcolorpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtcursorpropertymanager_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtvariantpropertymanager_wrapper.cpp

    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtabstracteditorfactorybase_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtgroupeditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtspinboxfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtinteditfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtsliderfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtscrollbarfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtcheckboxfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtdoublespinboxfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtdoubleeditfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtcomplexeditfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtvectorcomplexeditfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtlineeditfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtfileeditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtdateeditfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qttimeeditfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtdatetimeeditfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtkeysequenceeditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtchareditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtlocaleeditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtpointeditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtpointfeditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtsizeeditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtsizefeditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtrecteditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtrectfeditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtenumeditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtflageditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtsizepolicyeditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtcursoreditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtcoloreditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtfonteditorfactory_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtvarianteditorfactory_wrapper.cpp

    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtabstractpropertybrowser_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qttreepropertybrowser_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtgroupboxpropertybrowser_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtbuttonpropertybrowser_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qtpropertybrowser/qtpropertybrowser_module_wrapper.cpp)
set(BINDINGS_H ${CMAKE_CURRENT_SOURCE_DIR}/bindings.h)
set(BINDINGS_XML ${CMAKE_CURRENT_SOURCE_DIR}/bindings.xml)
add_custom_command(OUTPUT ${generated_sources}
                   COMMAND ${shiboken_generator}
                   "--enable-pyside-extensions"
                   ${SHIBOKEN_OPT} ${BINDINGS_H} ${BINDINGS_XML}
                   DEPENDS ${BINDINGS_H} ${BINDINGS_XML}
                   WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                   COMMENT "Running binding generator for ${CMAKE_CURRENT_SOURCE_DIR}.")
add_custom_target(qtpropertybrowserpy_shiboken_generator ALL
    DEPENDS ${generated_sources}
)

## Build the Python binding.
add_library(qtpropertybrowserpy MODULE ${generated_sources})
## Define Python module_name.so
set_target_properties(qtpropertybrowserpy PROPERTIES PREFIX "")
set_target_properties(qtpropertybrowserpy PROPERTIES OUTPUT_NAME "qtpropertybrowser")
if(WIN32)
    set_target_properties(qtpropertybrowserpy PROPERTIES SUFFIX ".pyd")
    target_compile_definitions(qtpropertybrowserpy PRIVATE QT_QTPROPERTYBROWSER_IMPORT) # export WIN32 symbols in .lib file
    target_compile_definitions(qtpropertybrowserpy PRIVATE _USE_MATH_DEFINES)
endif()

# Include Flags
target_include_directories(qtpropertybrowserpy PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../src)
target_include_directories(qtpropertybrowserpy PRIVATE ${PYTHON_SP_DIR}/PySide6/include)
target_include_directories(qtpropertybrowserpy PRIVATE ${PYTHON_SP_DIR}/PySide6/include/QtWidgets)
target_include_directories(qtpropertybrowserpy PRIVATE ${PYTHON_SP_DIR}/PySide6/include/QtGui)
target_include_directories(qtpropertybrowserpy PRIVATE ${PYTHON_SP_DIR}/PySide6/include/QtCore)
target_include_directories(qtpropertybrowserpy PRIVATE ${shiboken_include_dir})
target_include_directories(qtpropertybrowserpy PRIVATE ${PYTHON_INC})
target_include_directories(qtpropertybrowserpy PRIVATE ${Qt6Widgets_INCLUDE_DIRS})

# Link Flags
target_link_libraries(qtpropertybrowserpy PRIVATE qtpropertybrowser::qtpropertybrowser)
if(WIN32)
    target_link_libraries(qtpropertybrowserpy PRIVATE ${PYTHON_SP_DIR}/PySide6/pyside6.cp${Python_VERSION_MAJOR}${Python_VERSION_MINOR}-win_amd64${CMAKE_STATIC_LIBRARY_SUFFIX})
    target_link_libraries(qtpropertybrowserpy PRIVATE ${CONDA_PREFIX}/libs/python${PYTHONVERSION}${CMAKE_STATIC_LIBRARY_SUFFIX})
elseif(APPLE)
    target_link_libraries(qtpropertybrowserpy PRIVATE ${PYTHON_SP_DIR}/PySide6/libpyside6.cpython-${Python_VERSION_MAJOR}${Python_VERSION_MINOR}-darwin.${Qt_VERSION_MAJOR}.${Qt_VERSION_MINOR}${CMAKE_SHARED_LIBRARY_SUFFIX})
    set_target_properties(qtpropertybrowserpy PROPERTIES LINK_FLAGS "-undefined dynamic_lookup")
else()
    target_link_libraries(qtpropertybrowserpy PRIVATE ${PYTHON_SP_DIR}/PySide${Qt_VERSION_MAJOR}/libpyside${Qt_VERSION_MAJOR}.abi${Python_VERSION_MAJOR}${CMAKE_SHARED_LIBRARY_SUFFIX}.${Qt_VERSION_MAJOR}.${Qt_VERSION_MINOR})
endif() 
target_link_libraries(qtpropertybrowserpy PRIVATE ${shiboken_shared_libraries})
target_link_libraries(qtpropertybrowserpy PRIVATE Qt6::Widgets)
target_link_libraries(qtpropertybrowserpy PRIVATE Qt6::Gui)
target_link_libraries(qtpropertybrowserpy PRIVATE Qt6::Core)

# Install
if (WIN32)
    install (TARGETS qtpropertybrowserpy EXPORT qtpropertybrowserpyTargets
             DESTINATION bin)
else()
    install (TARGETS qtpropertybrowserpy EXPORT qtpropertybrowserpyTargets
             DESTINATION lib)
endif()
export_package(qtpropertybrowserpy ${SKNRF_VERSION})
