#!/usr/bin/env python
"""Setup script for the librispeech-abx module """

import numpy
import setuptools
from Cython.Build import cythonize

extensions = [setuptools.Extension(
        'libri_light_dtw',
        sources=['libriabx/libri_light/ABX_src/dtw.pyx'],
        extra_compile_args=['-O3'],
        include_dirs=[numpy.get_include()])]

setuptools.setup(
    ext_modules=cythonize(extensions, force=True),
    # needed for cython/setuptools, see
    # http://docs.cython.org/en/latest/src/quickstart/build.html
    zip_safe=False
)

