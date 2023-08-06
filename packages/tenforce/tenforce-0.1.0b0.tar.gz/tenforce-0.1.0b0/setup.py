from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='Tenforce',
    version="0.1.0b",
    ext_modules=cythonize(["tenforce/enforcer.pyx"]),
    description="Type enforcement for Python",
    long_description="Enforces types on class variables through type hints"
)
