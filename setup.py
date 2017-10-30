"""
setup.py

    Setup file for Sphecius package.

@author: Douglas Daly
@date: 4/6/2017
"""
#
#   Imports
#
import os
from distutils.core import setup


#
#   Functions
#

def read(filename):
    """Read the contents of a file"""
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


#
#   Setup Code
#
setup(
    name='sphecius',
    author='Doug Daly',
    author_email='douglas.daly89@gmail.com',
    description='A library for cryptanalysis and cryptography.',
    keywords='cryptanalysis cryptography cryptology',
    version='0.1dev',
    url="https://github.com/douglasdaly/sphecius",
    packages=['sphecius'],
    license='MIT',
    long_description=read('README.md')
)
