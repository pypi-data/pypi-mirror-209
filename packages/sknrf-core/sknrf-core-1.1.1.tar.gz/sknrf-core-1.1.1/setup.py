import os
import sys
import shutil
import pathlib
import yaml
import site
import warnings
from distutils.dir_util import copy_tree
from distutils.command.clean import clean as _clean
from distutils.command.config import config as _config
from distutils.command.build import build as _build
from distutils.command.build_clib import build_clib as _build_clib
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
from distutils.command.install import install as _install
from distutils.command.install_lib import install_lib as _install_lib
from distutils.command.install_data import install_data as _install_data
from distutils.command.upload import upload as _upload
from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from distutils.core import Command
from subprocess import Popen

LLVM_INSTALL_DIR = os.getenv('LLVM_INSTALL_DIR', '/usr/local/libclang')
os.environ['LLVM_INSTALL_DIR'] = LLVM_INSTALL_DIR
CONDA_PREFIX = os.getenv("CONDA_PREFIX", '/usr/local')
os.environ['CONDA_PREFIX'] = CONDA_PREFIX
SITE_PACKAGES = site.getsitepackages()[0]
SKNRF_DIR = os.getenv('SKNRF_DIR', SITE_PACKAGES)
os.environ['SKNRF_DIR'] = SKNRF_DIR
VISA_LIB = os.getenv('VISA_LIB', '@py')
os.environ['VISA_LIB'] = VISA_LIB
print('ENVIRONMENT VARIABLES:')
print('---------------------------------------------------------------------------------------------------------------')
print(f'LLVM_INSTALL_DIR: {LLVM_INSTALL_DIR:s}')
print(f'CONDA_PREFIX:     {CONDA_PREFIX:s}')
print(f'SITE_PACKAGES:    {SITE_PACKAGES:s}')
print(f'SKNRF_DIR:        {SKNRF_DIR:s}')
print('---------------------------------------------------------------------------------------------------------------')

root = pathlib.Path(__file__).parent
root_build = root / 'build'
root_build_doc = root_build / 'doc'
root_build_doc_html = root_build_doc / 'html'
root_build_doc_doctrees = root_build_doc / 'doctrees'
root_src = root / 'sknrf'
root_src_data = root_src / 'data'
root_src_data_datagroups = root_src_data / 'datagroups'
root_doc = root / 'doc'
root_doc_src = root_doc / 'source'
root_doc_src_api = root_doc_src / 'api'
root_dist = root / 'dist'
ins = pathlib.Path(CONDA_PREFIX)
ins_pkg = ins / 'sknrf'
www_public_html = pathlib.Path('scikitno@scikit-nonlinear.org:/home/scikitno/public_html')

print('DIRECTORY TREE')
print('---------------------------------------------------------------------------------------------------------------')
print(f'package_root         {str(root):s}')
print(f'|-build              {str(root_build):s}')
print(f'|   |-doc            {str(root_build_doc):s}')
print(f'|       |-html       {str(root_build_doc_html):s}')
print(f'|       |-doctrees   {str(root_build_doc_doctrees):s}')
print(f'|-sknrf              {str(root_src):s}')
print(f'    |-data           {str(root_src_data):s}')
print(f'    |   |-datagroups {str(root_src_data_datagroups):s}')
print(f'    |-doc            {str(root_doc):s}')
print(f'        |-source     {str(root_doc_src):s}')
print(f'            |-api    {str(root_doc_src_api):s}')
print(f'    |-dist           {str(root_dist):s}')
print(f'')
print(f'install_root         {str(ins):s}')
print(f'')
print(f'url_root             {str(www_public_html):s}')
print('---------------------------------------------------------------------------------------------------------------')

with open(str(root / "sknrf" / "sknrf.yml")) as f:
    cfg = yaml.safe_load(f)
    ins_data = pathlib.Path(os.path.expandvars(cfg["data_root"]))


# src
with open('sknrfconfig.h') as fid:
    for line in fid:
        if line.startswith('#define SKNRF_VERSION_MAJOR'):
            SKNRF_VERSION_MAJOR = int(line.strip().split(' ')[-1])
        elif line.startswith('#define SKNRF_VERSION_MINOR'):
            SKNRF_VERSION_MINOR = int(line.strip().split(' ')[-1])
        elif line.startswith('#define SKNRF_VERSION_PATCH'):
            SKNRF_VERSION_PATCH = int(line.strip().split(' ')[-1])
        else:
            pass
    VERSION = "%d.%d.%d" % (SKNRF_VERSION_MAJOR, SKNRF_VERSION_MINOR, SKNRF_VERSION_PATCH)



def system_cmd(command, wait=True, cwd=root):
    command = command if isinstance(command, str) else " ".join(command)
    print(command)
    my_env = os.environ.copy()
    process = Popen(command, shell=True, stdout=sys.stdout, cwd=str(cwd), env=my_env)
    if wait:
        process.wait()
    return process


class clean(_clean):

    def has_pure_modules(self):
        return True

    def has_c_libraries(self):
        return True

    def has_ext_modules(self):
        return False

    def has_scripts(self):
        return True

    sub_commands = [('clean_clib',    has_c_libraries),
                    ('clean_py',      has_pure_modules),
                    ('clean_doc',     has_scripts),
                    ]

    def run(self):
        # Run all relevant sub-commands.  This will be some subset of:
        #  - clean_clib     - standalone C libraries
        #  - clean_py       - pure Python modules
        #  - clean_doc      - documentation
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)


class clean_clib(_config):
    description = "Clean C/C++ build directory"
    user_options = []
    boolean_options = []
    help_options = []

    def initialize_options(self):
        super().initialize_options()

    def finalize_options(self):
        super().finalize_options()

    def run(self):
        if root_build.exists():
            system_cmd('xargs rm < install_manifest.txt', cwd=root_build)

        if root_build.exists():
            shutil.rmtree(str(root_build))


class clean_py(_config):
    description = "Clean Python dist directory"
    user_options = []
    boolean_options = []
    help_options = []

    def initialize_options(self):
        super().initialize_options()

    def finalize_options(self):
        super().finalize_options()

    def run(self):
        if root_dist.exists():
            shutil.rmtree(str(root_dist))


class clean_doc(_config):
    description = "Clean Python doc directory"
    user_options = []
    boolean_options = []
    help_options = []

    def initialize_options(self):
        super().initialize_options()

    def finalize_options(self):
        super().finalize_options()

    def run(self):
        if root_build_doc.exists():
            shutil.rmtree(str(root_build_doc))

        if root_doc_src_api.exists():
            shutil.rmtree(str(root_doc_src_api))
        shutil.copyfile(str(root_src / 'sknrf.yml'), str(root_doc / 'sknrf.yml'))


class config(_config):

    # -- Predicates for the sub-command list ---------------------------

    def has_pure_modules(self):
        return True

    def has_c_libraries(self):
        return True

    def has_ext_modules(self):
        return False

    def has_scripts(self):
        return False

    sub_commands = [('config_py',      has_pure_modules),
                    ('config_clib',    has_c_libraries),
                    ('config_ext',     has_ext_modules),
                    ('config_scripts', has_scripts),
                    ]

    def run(self):

        # Run all relevant sub-commands.  This will be some subset of:
        #  - config_py      - pure Python modules
        #  - config_clib    - standalone C libraries
        #  - config_ext     - Python extensions
        #  - config_scripts - (Python) scripts
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)


class config_clib(_config):
    description = "Configure C/C++ Libraries"
    user_options = [
        ('debug', 'g', "debug mode"),
        ('force', 'f', "forcibly configure everything (ignore file timestamps)"),
        ('cmake=', 'k', "cmake config options"),
    ]
    boolean_options = ["debug", "force"]
    help_options = []

    def initialize_options(self):
        super().initialize_options()
        self.debug = False
        self.force = False
        self.cmake = None

    def finalize_options(self):
        super().finalize_options()
        self.force = False if self.force is None else self.force
        config = 'Debug' if self.debug else 'Release'
        self.cmake = f'-DCMAKE_BUILD_TYPE={config:s} \
                       -DSKNRF_BUILD_DOC=ON \
                       -DSKNRF_BUILD_TEST=ON' if self.cmake is None else self.cmake

    def run(self):
        root_build.mkdir(parents=True, exist_ok=True)
        system_cmd(['cmake', str(root), self.cmake], cwd=root_build)  # configure: 'cmake ..'


class config_py(_config):
    description = "Configure Python Libraries"
    user_options = [
        ('debug', 'g', "debug mode"),
        ('force', 'f', "forcibly configure everything (ignore file timestamps)"),
        ('uic=', 'u', "pyside6-uic config options"),
        ('rcc=', 'u', "pyside6-rcc config options"),
    ]
    boolean_options = ["debug", "force"]
    help_options = []

    def initialize_options(self):
        super().initialize_options()
        self.debug = False
        self.force = False

    def finalize_options(self):
        super().finalize_options()
        self.force = False if self.force is None else self.force

    def run(self):
        for path in (root_src / "view").rglob('*.ui'):
            fr_path = f"{str(path.parent):s}/{str(path.stem):s}{str(path.suffix):s}"
            to_path = f"{str(path.parent):s}/../{str(path.stem):s}_ui.py"
            print(f'PYSIDE: {fr_path:s} \n-> {to_path:s}')
            system_cmd(f'pyside6-uic {fr_path:s} -o {to_path:s}', cwd=root)

class build(_build):

    # -- Predicates for the sub-command list ---------------------------

    def has_pure_modules(self):
        return self.distribution.has_pure_modules()

    def has_c_libraries(self):
        return True

    def has_ext_modules(self):
        return self.distribution.has_ext_modules()

    def has_scripts(self):
        return self.distribution.has_scripts()

    sub_commands = [('build_py',      has_pure_modules),
                    ('build_clib',    has_c_libraries),
                    ('build_ext',     has_ext_modules),
                    ('build_scripts', has_scripts), ]


class build_clib(_build_clib):
    description = "Build C/C++ Libraries"
    user_options = _build_clib.user_options + [
        ('cmake=', 'k', "cmake build options"),
    ]

    def initialize_options(self):
        super().initialize_options()
        self.cmake = None

    def finalize_options(self):
        super().finalize_options()
        config = 'Debug' if self.debug else 'Release'
        self.cmake = '--config {:s}'.format(config) if self.cmake is None else self.cmake

    def run(self):
        system_cmd(['cmake', '--build', str(root_build), self.cmake], cwd=root_build)  # make: 'make' to build the project


class install(_install):

    def has_clib(self):
        return True

    def has_py(self):
        return True

    def has_desktop(self):
        return True

    def has_data(self):
        return True

    def has_doc(self):
        return True

    sub_commands = [('install_clib',     has_clib),
                    ('install_py',       has_py),
                    ('install_data',     has_data),
                    ('install_doc',      has_doc), ] + _install.sub_commands

    def initialize_options(self):
        super().initialize_options()

    def finalize_options(self):
        super().finalize_options()

    def run(self):
        # super().run()  # Replaced by install_py
        # Run all sub-commands (at least those that need to be run)
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)


class install_clib(_install_lib):
    description = "Install C/C++ Libraries"
    user_options = _install_lib.user_options + [
        ('cmake=', 'k', "cmake install options"),
    ]

    def initialize_options(self):
        super().initialize_options()
        self.cmake = None

    def finalize_options(self):
        super().finalize_options()
        self.cmake = f'' if self.cmake is None else self.cmake

    def run(self):
        system_cmd(['cmake', '--install', str(root_build), '--prefix', str(ins), self.cmake], cwd=root_build)


class install_py(_install):

    def initialize_options(self):
        super().initialize_options()

    def finalize_options(self):
        super().finalize_options()

    def run(self):
        super().run()


class install_data(_install_data):
    description = "Install application config data from ./sknrf/data"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for filename in root_src_data_datagroups.iterdir():
            if filename.stem != ".gitignore":
                filename.unlink()
        if not os.path.exists(ins_data):
            shutil.copytree(root_src_data, ins_data)
            print(f'Installed application config data to {str(ins_data):s}')
        else:
            print(f'Directory application config data in {str(ins_data):s} already exists, did not overwrite')
        shutil.copyfile((root_src / 'sknrf.yml'), pathlib.Path(SKNRF_DIR) / 'sknrf' / 'sknrf.yml')


class install_doc(Command):
    description = "Build HTML Documentation and save in ./doc/build/html directory."
    user_options = [
        ('force', 'f', "clean the documentation folder."),
        ('api', 'a', "build programmable api."),
        ('html', 'w', "build html documentation."),
    ]
    boolean_options = ['clean', 'api', 'html']
    help_options = []

    def initialize_options(self):
        self.force = False

    def finalize_options(self):
        pass

    def run(self):
        self.force = False if self.force is None else self.force
        if self.force:
            system_cmd("make clean", cwd=root_doc)
        system_cmd("make api", cwd=root_doc)
        system_cmd("make html", cwd=root_doc)


class bdist_wheel(_bdist_wheel):
    def finalize_options(self):
        _bdist_wheel.finalize_options(self)
        self.root_is_pure = False
        self.py_limited_api = "cp310"


class upload(_upload):

    def has_pypi(self):
        return True

    def has_doc(self):
        return True

    sub_commands = [('upload_pypi',    has_pypi),
                    ('upload_doc',     has_doc)] + _install.sub_commands

    def run(self):
        # Run all sub-commands (at least those that need to be run)
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)


class upload_pypi(_upload):

    description = "Upload source code to pypi."
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class upload_doc(Command):

    description = "Upload latest doc from ./build/doc/ directory."
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        system_cmd(f'rsync -ac --delete {str(root_build_doc_html):s} {str(www_public_html):s}', cwd=root_doc)
        system_cmd(f'rsync -ac --delete {str(root_build_doc_doctrees):s} {str(www_public_html):s}', cwd=root_doc)


setup(
    version=VERSION,
    package_dir={'sknrf': 'sknrf'},
    include_package_data=True,
    packages=find_packages(exclude=['doc', 'tests*']),
    entry_points={
        'gui_scripts': ['main = sknrf.main:main'],
    },
    # Support functions
    cmdclass={
            # Clean
            'clean': clean,
            'clean_clib': clean_clib,
            'clean_py': clean_py,
            'clean_doc': clean_doc,
            # Configure
            'config': config,
            'config_clib': config_clib,
            'config_py': config_py,
            # Build
            'build': build,
            'build_clib': build_clib,
            #'build_py': (Included),
            # Install
            'install': install,
            'install_clib': install_clib,
            'install_data': install_data,
            'install_py': install_py,
            'install_doc': install_doc,
            # Distribute
            'bdist_wheel': bdist_wheel,
            # Upload
            'upload': upload,
            'upload_pypi': upload_pypi,
            'upload_doc': upload_doc}
)

