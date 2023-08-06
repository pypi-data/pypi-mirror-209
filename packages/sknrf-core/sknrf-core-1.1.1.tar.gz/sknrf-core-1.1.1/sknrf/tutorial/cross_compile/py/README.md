# Cross compilation of Pyside6.3.0 on Raspberry pi 4

# Prepare Target (Raspberry pi 4)

## Install Pre-requisites

sudo pacman -Syyuu
sudo pacman -S git net-tools vim
sudo pacman -S base-devel
sudo pacman -S qt6-base qt6-svg qt6-tools
sudo pacman -S cmake
sudo pacman -S python-pip
reboot

##

# Prepare Host (Ubuntu 20.0.4)

## Install Pre-requisites

```bash
sudo apt update
sudo apt upgrade
sudo apt -y install git net-tools vim 
sudo apt -y install build-essential
sudo apt -y install ipheth-utils libimobiledevice-dev libimobiledevice-utils
sudo apt -y install libgl-dev python-dev python-setuptools ninja-build
reboot
mkdir repos
cd !$
git clone --recursive https://code.qt.io/pyside/pyside-setup
sudo snap install pycharm-professional --classic

cd pyside-setup
python -m venv testenv
source testenv/bin/activate
pip install -r requirements.txt
git checkout 6.3.0
wget https://download.qt.io/development_releases/prebuilt/libclang/libclang-release_140-based-linux-Ubuntu20.04-gcc9.3-x86_64.7z
7z x libclang-release_140-based-linux-Ubuntu20.04-gcc9.3-x86_64.7z
export CLANG_INSTALL_DIR=$PWD/libclang
export QT_VERSION="${QT_VERSION:=6.3.0}"
export QT_DIR="/opt/Qt/${QT_VERSION}/gcc_64"
export QMAKESPEC="linux-g++"
export QT_QPA_PLATFORM_PLUGIN_PATH="$QT_DIR/plugins/platforms"
export QT_PLUGIN_PATH="$QT_DIR/plugins"
export QML2_IMPORT_PATH="$QT_DIR/qml"
export QT_PATH="$QT_DIR/bin"
export QT_LD_LIBRARY_PATH="$QT_DIR/lib"
export QT_API="PySide6"
export PYTEST_QT_API="pyside6"
export KRB_LD_LIBRARY_PATH="/opt/krb5/lib"
export PATH="${QT_PATH}:${PATH}"
export LD_LIBRARY_PATH="${KRB_LD_LIBRARY_PATH}:${QT_LD_LIBRARY_PATH}:${LD_LIBRARY_PATH}"
```

During compilation I see a lot of dependency problems because of cmake. Then I simply compiled it from source.
Latest version is better. My version is:
```bash
dylan@dylan: $ cmake --version
cmake version 3.23.20220428-g90d5d42

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```
Compilation of CMake is easy:
```bash
$ sudo apt install libssl-dev
$ git clone https://github.com/Kitware/CMake.git
$ cd CMake
$ ./bootstrap && make && sudo make install
$ cmake --version
```


## Install Qt 6.3+ on Host

Download and install Qt using online installer
    - https://www.qt.io/download-open-source
    >>> chmod +x ${HOME}/Downloads/qt-unified-linux-x64-*.run
    >>> sudo apt-get install libxcb-xinerama0
    >>> ${HOME}/Downloads/qt-unified-linux-x64-*.run

## Install Pyside6 on Host

```bash
git clone --recursive https://code.qt.io/pyside/pyside-setup
cd pyside-setup
python setup.py build \
       --qtpaths=/opt/Qt/6.3.0/gcc_64/bin/qtpaths \
       --build-tests \
       --ignore-git \
       --parallel=8
       
python setup.py install \
       --qtpaths=/opt/Qt/6.3.0/gcc_64/bin/qtpaths \
       --build-tests \
       --ignore-git \
       --parallel=8
       
python examples/widgets/tetrix/tetrix.py
```

## Copy Target sysroot

```bash
cd $HOME
mkdir rpi-sdk 
cd !$

mkdir sysroot sysroot/usr sysroot/opt
rsync -avz dylan@192.168.1.114:/usr/include sysroot/usr
rsync -avz dylan@192.168.1.114:/usr/bin sysroot/usr
rsync -avz dylan@192.168.1.114:/lib sysroot
rsync -avz dylan@192.168.1.114:/usr/lib sysroot/usr
rsync -avz dylan@192.168.1.114:/opt/vc sysroot/opt

wget https://raw.githubusercontent.com/riscv/riscv-poky/master/scripts/sysroot-relativelinks.py
chmod +x sysroot-relativelinks.py 
python3 sysroot-relativelinks.py sysroot
```

## Get the toolchain

```bash
VERSION="10.2-2020.11"
cd !$
wget "https://developer.arm.com/-/media/Files/downloads/gnu-a/${VERSION}/binrel/gcc-arm-${VERSION}-x86_64-aarch64-none-linux-gnu.tar.xz"
wget "https://developer.arm.com/-/media/Files/downloads/gnu-a/${VERSION}/binrel/gcc-arm-${VERSION}-x86_64-aarch64-none-linux-gnu.tar.xz.asc"
md5sum --check "gcc-arm-${VERSION}-x86_64-aarch64-none-linux-gnu.tar.xz.asc"
tar xf "gcc-arm-${VERSION}-x86_64-aarch64-none-linux-gnu.tar.xz" -C /usr/share/
ln -s "/usr/share/gcc-arm-${VERSION}-x86_64-aarch64-none-linux-gnu/bin/"* /usr/bin/
```

Save the following in /usr/share/toolchain-aarch64.cmake
```cmake
# toolchain-aarch64.cmake
cmake_minimum_required(VERSION 3.18)
include_guard(GLOBAL)

set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR aarch64)

set(TARGET_SYSROOT /home/dylan/rpi-sdk/sysroot)
set(CROSS_COMPILER /usr/share/gcc-arm-10.2-2020.11-x86_64-aarch64-none-linux-gnu/bin/aarch64-none-linux-gnu)

set(CMAKE_SYSROOT ${TARGET_SYSROOT})

set(ENV{PKG_CONFIG_PATH} "")
set(ENV{PKG_CONFIG_LIBDIR} ${CMAKE_SYSROOT}/usr/lib/pkgconfig:${CMAKE_SYSROOT}/usr/share/pkgconfig)
set(ENV{PKG_CONFIG_SYSROOT_DIR} ${CMAKE_SYSROOT})

set(CMAKE_C_COMPILER ${CROSS_COMPILER}/aarch64-none-linux-gnu-gcc)
set(CMAKE_CXX_COMPILER ${CROSS_COMPILER}/aarch64-none-linux-gnu-g++)

set(QT_COMPILER_FLAGS "-march=armv8-a")
set(QT_COMPILER_FLAGS_RELEASE "-O2 -pipe")
set(QT_LINKER_FLAGS "-Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed")

set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)

include(CMakeInitializeConfigs)

function(cmake_initialize_per_config_variable _PREFIX _DOCSTRING)
  if (_PREFIX MATCHES "CMAKE_(C|CXX|ASM)_FLAGS")
    set(CMAKE_${CMAKE_MATCH_1}_FLAGS_INIT "${QT_COMPILER_FLAGS}")

    foreach (config DEBUG RELEASE MINSIZEREL RELWITHDEBINFO)
      if (DEFINED QT_COMPILER_FLAGS_${config})
        set(CMAKE_${CMAKE_MATCH_1}_FLAGS_${config}_INIT "${QT_COMPILER_FLAGS_${config}}")
      endif()
    endforeach()
  endif()

  if (_PREFIX MATCHES "CMAKE_(SHARED|MODULE|EXE)_LINKER_FLAGS")
    foreach (config SHARED MODULE EXE)
      set(CMAKE_${config}_LINKER_FLAGS_INIT "${QT_LINKER_FLAGS}")
    endforeach()
  endif()

  _cmake_initialize_per_config_variable(${ARGV})
endfunction()
```


## Clone pyside source code and cross compile it

```bash
git clone --recursive https://code.qt.io/pyside/pyside-setup
cd pyside-setup
python setup.py bdist_wheel \
       --parallel=8 --ignore-git --reuse-build --standalone --limited-api=yes \
       --cmake-toolchain-file=/opt/toolchain-aarch64.cmake \
       --qt-host-path=/opt/Qt/6.3.0/gcc_64 \
       --plat-name=linux_aarch64
```

## Copy the binaries from Host to Target

```bash
scp dist/* dylan@192.168.1.114:/home/dylan/
scp examples/widgets/tetrix/tetrix.py dylan@192.168.1.114:/home/dylan/
```

# Install and Run on the Target

```bash
cd ${HOME}
pip install shiboken*
pip install PySide*
python tetrix
```






