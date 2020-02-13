from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('run.pyx'))

"""
python setup.py build_ext --inplace

python -a run.pyx

"""
