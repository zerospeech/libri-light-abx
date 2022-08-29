#!/usr/bin/env python
"""Setup script for the librispeech-abx module """

import codecs

import numpy
import setuptools

setuptools.setup(
    name='libriabx',
    description='A wrapper installer around the librispeech implementation of abx',
    version='1.0.3',
    install_requires=['torch', 'progressbar2', 'torchaudio']
    # python package dependencies
    setup_requires=['cython', 'numpy'],
    # include Python code
    packages=setuptools.find_packages(),
    # build cython extension
    ext_modules=[setuptools.Extension(
        'libri_light_dtw',
        sources=['libriabx/libri_light/ABX_src/dtw.pyx'],
        extra_compile_args=['-O3'],
        include_dirs=[numpy.get_include()])],

    # needed for cython/setuptools, see
    # http://docs.cython.org/en/latest/src/quickstart/build.html
    zip_safe=False,

    # the command-line scripts to export
    entry_points={
        'console_scripts': [
            'libri-abx = libriabx.libri_light.eval_ABX:main',
        ]},

    # metadata
    author='CoML team',
    author_email='dev@zerospeech.com',
    license='GPL3',
    url='https://zerospeech.com/',
    long_description=codecs.open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.7',

)

