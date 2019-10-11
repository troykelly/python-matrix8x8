# -*- coding: utf-8 -*-

from hdmimatrix import __version__
from distutils.core import setup

setup(
    name = 'hdmimatrix',
    version = __version__,
    description = 'An interface to generic HDMI 8x8 Matrix devices',
    author = 'Troy Kelly',
    license='MIT',
    url = 'https://github.com/troykelly/python-matrix8x8',
    py_modules=['hdmimatrix'],
)
