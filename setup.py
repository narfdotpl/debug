#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup


setup(
    name='debug',
    version='0.2.0dev',
    description='Start fancy debugger in a single statement.',
    author='Maciej Konieczny',
    author_email='hello@narf.pl',
    url='https://github.com/narfdotpl/debug',
    py_modules=['debug'],
    install_requires=['ipython >= 0.10, < 0.11', 'see >= 1.0']
)
