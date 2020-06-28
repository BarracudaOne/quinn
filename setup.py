# !/usr/bin/env python3
"""
quinn: A simple deep Q learning framework using torch

This package provides some simple classes that can be useful
for Q learning

"""

import os
import sys

from setuptools import setup, find_packages

here = os.path.dirname(__file__)
README = open(os.path.join(here, 'README.md')).read()


if sys.version_info.major < 3 or sys.version_info.minor < 5:
    print("Package is for python 3.5 or later, please upgrade")
    sys.exit(1)


setup(name='quinn',
      version='0.0.1',
      license='MIT',
      description="quinn: a simple deep Q learning framework",
      long_description=README,
      long_description_content_type="text/markdown",
      author='Q Learning Team',
      url='https://www.github.com/BarracudaOne/quinn',
      project_urls={"Bug Tracker": "https://github.com/BarracudaOne/quinn/issues",
                    "Source Code": "https://github.com/BarracudaOne/quinn"},
      keywords=["Reinforcement Learning", "Q learning", "Deep Q Learning"],
      platforms=["Linux"],
      python_requires=">=3.5",
      packages=find_packages(),
      tests_require=["pytest"],
      install_requires=['smbus'],
      classifiers=['Development Status :: 1 - Planning',
                   'Intended Audience :: Developers',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7']
      )
