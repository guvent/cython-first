# from Cython.Distutils import build_ext
# from setuptools import setup
# from setuptools import Extension

# module = 'run'

# ext_modules = [Extension(module, sources=[module + ".pyx"],
#             #   include_dirs=['path1','path2'], # put include paths here
#               library_dirs=[], # usually need your Windows SDK stuff here 
#               language='c++')]

# setup(
#     name = module,
#     ext_modules = ext_modules,
#     cmdclass = {'build_ext': build_ext},
#     # include_dirs = ['path1', 'path2']
# )

# ^^^  python setup.py build_ext --compiler=msvc


from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('run.pyx'))


"""
python setup.py build_ext --inplace

python -a run.pyx

"""
