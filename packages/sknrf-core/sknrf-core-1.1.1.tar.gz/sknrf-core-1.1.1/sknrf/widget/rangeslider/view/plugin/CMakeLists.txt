cmake_minimum_required(VERSION 3.18.0)
project(qrangesliderplugin)

# Include
include("${PROJECT_SOURCE_DIR}/../../cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/../../cmake/export_package.cmake")

# Variables
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(qrangeslider REQUIRED)

# Build
set(headers
    qrangesliderplugin.h)
add_library(qrangesliderplugin SHARED
    ${headers}
    qrangesliderplugin.cpp)
set_target_properties(qrangesliderplugin PROPERTIES VERSION ${SKNRF_VERSION} SOVERSION ${SKNRF_VERSION_MAJOR})
target_compile_definitions(qrangesliderplugin PRIVATE QRANGESLIDER_USE_LIBRARY) # export WIN32 symbols in .lib file
target_compile_definitions(qrangesliderplugin PRIVATE QRANGESLIDERPLUGIN_LIBRARY)

# Include Flags
target_include_directories(qrangesliderplugin PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../src)

# Linking Flags
target_link_libraries(qrangesliderplugin PRIVATE qrangeslider::qrangeslider)
target_link_libraries(qrangesliderplugin PRIVATE Qt6::Widgets)
target_link_libraries(qrangesliderplugin PRIVATE Qt6::Gui)
target_link_libraries(qrangesliderplugin PRIVATE Qt6::Core)

# Install
install(TARGETS qrangesliderplugin EXPORT qrangesliderpluginTargets
        DESTINATION ${QT_PLUGIN_DIR})
export_package(qrangesliderplugin ${SKNRF_VERSION})
