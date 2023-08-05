import os
import sys
import subprocess
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

# pybind11 import, if it's missing then try to install it
try:
    import pybind11
except ImportError:
    print("pybind11 not found, installing...")
    # Install pybind11 using pip
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pybind11'])
    import pybind11

# Get the numpy include directory
try:
    import numpy as np
except ImportError:
    print("numpy not found, installing...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
    

def get_numpy_include():
    """Return numpy include directory."""
    return np.get_include()

def get_pybind_include():
    """Return pybind11 include directory."""
    return pybind11.get_include()



# Define the extension module
ext_module = Extension(
    'Enumerator_linux',
    sources=['Enumerator_linux.cpp'],
    include_dirs=[pybind11.get_include()],
    language='c++'
)

# Custom build_ext command to enable passing extra compiler options
class BuildExt(build_ext):
    def build_extensions(self):
        # Add any extra compiler options here
        extra_compile_args = ['-std=c++11']
        for ext in self.extensions:
            ext.extra_compile_args = extra_compile_args
        build_ext.build_extensions(self)

# Setup configuration
setup(
    name='enumerator-linux',
    version='1.0',
    description='Enumerator Linux Extension Module',
    author='Your Name',
    author_email='your_email@example.com',
    ext_modules=[ext_module],
    cmdclass={'build_ext': BuildExt},
    zip_safe=False
)
