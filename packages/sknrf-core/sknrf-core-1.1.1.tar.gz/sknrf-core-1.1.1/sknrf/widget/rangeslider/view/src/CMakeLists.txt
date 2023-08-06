cmake_minimum_required(VERSION 3.18.0)
project(qrangeslider)

# Include
include("${PROJECT_SOURCE_DIR}/../../cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/../../cmake/export_package.cmake")

# Variables
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

# Build
set(headers
        qrangeslider.h)
#add_executable(qrangeslider
#    main.cpp
add_library(qrangeslider SHARED
    ${headers}
    qrangeslider.cpp)
set_target_properties(qrangeslider PROPERTIES VERSION ${SKNRF_VERSION} SOVERSION ${SKNRF_VERSION_MAJOR})
set_target_properties(qrangeslider PROPERTIES PUBLIC_HEADER "${headers}")
target_compile_definitions(qrangeslider PRIVATE QRANGESLIDER_COMPILE_LIBRARY) # export WIN32 symbols in .lib file

# Linking Flags
target_link_libraries(qrangeslider PRIVATE Qt6::Widgets)
target_link_libraries(qrangeslider PRIVATE Qt6::Gui)
target_link_libraries(qrangeslider PRIVATE Qt6::Core)

# Install
install(TARGETS qrangeslider EXPORT qrangesliderTargets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
    PUBLIC_HEADER DESTINATION include)
export_package(qrangeslider ${SKNRF_VERSION})
