cmake_minimum_required(VERSION 3.18.0)
project(qtpropertybrowser)

# Include
include("${PROJECT_SOURCE_DIR}/../../cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/../../cmake/export_package.cmake")

# Variables
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

# Build
set(headers
    qttreepropertybrowser.h
    qtbuttonpropertybrowser.h
    qtgroupboxpropertybrowser.h
    qtpropertybrowserutils_p.h
    qtpropertybrowser.h
    qtpropertymanager.h
    qtvariantproperty.h
    qteditorfactory.h)
#add_executable(qtpropertybrowser
#    main.cpp
add_library(qtpropertybrowser SHARED
    ${headers}
    qttreepropertybrowser.cpp
    qtbuttonpropertybrowser.cpp
    qtgroupboxpropertybrowser.cpp
    qtpropertybrowser.cpp
    qtpropertymanager.cpp
    qteditorfactory.cpp
    qtpropertybrowserutils.cpp
    qtvariantproperty.cpp
    qtpropertybrowser.qrc)
set_target_properties(qtpropertybrowser PROPERTIES VERSION ${SKNRF_VERSION} SOVERSION ${SKNRF_VERSION_MAJOR})
set_target_properties(qtpropertybrowser PROPERTIES PUBLIC_HEADER "${headers}")
target_compile_definitions(qtpropertybrowser PRIVATE _USE_MATH_DEFINES)
if (WIN32)
    target_compile_definitions(qtpropertybrowser PRIVATE QT_QTPROPERTYBROWSER_EXPORT) # export WIN32 symbols in .lib file
endif()

# Linking Flags
target_link_libraries(qtpropertybrowser PRIVATE Qt6::Widgets)
target_link_libraries(qtpropertybrowser PRIVATE Qt6::Gui)
target_link_libraries(qtpropertybrowser PRIVATE Qt6::Core)

# Install
install(TARGETS qtpropertybrowser EXPORT qtpropertybrowserTargets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
    PUBLIC_HEADER DESTINATION include)
export_package(qtpropertybrowser ${SKNRF_VERSION})
