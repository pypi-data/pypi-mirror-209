cmake_minimum_required(VERSION 3.12.0)
project(qtpropertybrowsertest LANGUAGES CXX)

# Include
include("${PROJECT_SOURCE_DIR}/../../cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/../../cmake/export_package.cmake")

# Variables
find_package(Qt6 REQUIRED COMPONENTS Test)
find_package(qtpropertybrowser REQUIRED)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
enable_testing(true)

# Build
## Generate the Base Test Cases
set(generated_sources
    qtpropertybrowsertest.h
    qtpropertybrowsertest.cpp
 )
add_custom_command(
		OUTPUT ${generated_sources}
		COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/configure.py
		DEPENDS configure.py config.yml
		COMMENT "Generate BaseTests"
)
add_custom_target(generate_base_tests
		DEPENDS ${generated_sources}
)
add_executable(qtpropertybrowsertest
        mytest.cpp
        qtabstractpropertybrowsertest.h
        qtpropertybrowsertest.h
        qtcustompropertybrowsertest.h
        qtabstractpropertybrowsertest.cpp
        qtpropertybrowsertest.cpp
        qtcustompropertybrowsertest.cpp)

add_test(NAME qtpropertybrowsertest COMMAND qtpropertybrowsertest)
set_target_properties(qtpropertybrowsertest PROPERTIES VERSION ${SKNRF_VERSION} SOVERSION ${SKNRF_VERSION_MAJOR})
target_compile_definitions(qtpropertybrowsertest PRIVATE QT_QTPROPERTYBROWSER_IMPORT) # export WIN32 symbols in .lib file

# Include Flags
target_include_directories(qtpropertybrowsertest PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../src)

# Linking Flags
target_link_libraries(qtpropertybrowsertest PRIVATE qtpropertybrowser::qtpropertybrowser)
target_link_libraries(qtpropertybrowsertest PRIVATE Qt6::Widgets)
target_link_libraries(qtpropertybrowsertest PRIVATE Qt6::Gui)
target_link_libraries(qtpropertybrowsertest PRIVATE Qt6::Core)
target_link_libraries(qtpropertybrowsertest PRIVATE Qt6::Test)

# Install
install(TARGETS qtpropertybrowsertest EXPORT qtpropertybrowsertestTargets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
    PUBLIC_HEADER DESTINATION include)
#export_package(qtpropertybrowsertest ${SKNRF_VERSION})
