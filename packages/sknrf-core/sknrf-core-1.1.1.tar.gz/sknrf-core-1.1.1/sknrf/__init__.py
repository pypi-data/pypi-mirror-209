import os
import sys
import site

__version__ = '1.1.1'

# Environment Variables
os.environ['SKNRF_DIR'] = os.getenv('SKNRF_DIR', site.getsitepackages()[0])
os.environ['CONDA_PREFIX'] = os.getenv('CONDA_PREFIX', '/usr/local')
os.environ['VISA_LIB'] = os.getenv('VISA_LIB', '@py')

# Import Shared Objects
lib_dir = os.sep.join((os.environ['CONDA_PREFIX'], 'lib'))
if lib_dir not in sys.path:
    sys.path.insert(0, lib_dir)
