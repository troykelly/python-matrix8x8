import codecs
import os
import re
import sys

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


long_description = read('README.md')

setup(
    name="matrix8x8",
    version=find_version("src", "pip", "__init__.py"),
    description="Control an 8x8 HDMI matrix switcher.",
    long_description=long_description,

    license='MIT',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    url='https://github.com/troykelly/python-matrix8x8',
    keywords='homeautomation hdmi matrix vision switching switcher',

    author='Troy Kelly',
    author_email='troy@troykelly.com',

    package_dir={"": "matrix8x8_lib"},
    packages=find_packages(
        where="matrix8x8_lib",
        exclude=["contrib", "docs", "tests*", "tasks"],
    ),
    zip_safe=False,
    python_requires='>=3.7',
)
