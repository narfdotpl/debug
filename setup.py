#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup


setup(
    name='debug',
    version='0.2.1',
    description='Start fancy debugger in a single statement.',
    author='Maciej Konieczny',
    author_email='hello@narf.pl',
    url='https://github.com/narfdotpl/debug',
    py_modules=['debug'],
    install_requires=['ipdb >= 0.8.1', 'see >= 1.1']
)
