cmake_minimum_required(VERSION 3.18.0)
project(qprogressindicatorplugin)

# Include
include("${PROJECT_SOURCE_DIR}/../../cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/../../cmake/export_package.cmake")

# Variables
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(qprogressindicator REQUIRED)

# Build
set(headers
    qprogressindicatorplugin.h)
add_library(qprogressindicatorplugin SHARED
    ${headers}
    qprogressindicatorplugin.cpp)
set_target_properties(qprogressindicatorplugin PROPERTIES VERSION ${SKNRF_VERSION} SOVERSION ${SKNRF_VERSION_MAJOR})
target_compile_definitions(qprogressindicatorplugin PRIVATE QPROGRESSINDICATORPLUGIN_USE_LIBRARY) # export WIN32 symbols in .lib file
target_compile_definitions(qprogressindicatorplugin PRIVATE QPROGRESSINDICATORPLUGIN_LIBRARY)


# Include Flags
target_include_directories(qprogressindicatorplugin PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../src)

# Linking Flags
target_link_libraries(qprogressindicatorplugin PRIVATE qprogressindicator::qprogressindicator)
target_link_libraries(qprogressindicatorplugin PRIVATE Qt6::Widgets)
target_link_libraries(qprogressindicatorplugin PRIVATE Qt6::Gui)
target_link_libraries(qprogressindicatorplugin PRIVATE Qt6::Core)

# Install
install (TARGETS qprogressindicatorplugin EXPORT qprogressindicatorpluginTargets
         DESTINATION ${QT_PLUGIN_DIR})
export_package(qprogressindicatorplugin ${SKNRF_VERSION})
