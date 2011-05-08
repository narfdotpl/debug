#!/usr/bin/env python
# encoding: utf-8

from sys import _getframe

from IPython import ipapi
from IPython.Debugger import Pdb
from IPython.Shell import IPShell


__author__ = 'Maciej Konieczny <hello@narf.pl>'
__version__ = '0.1.0dev'


# get frame
frame = _getframe().f_back

# inject see (from see import see)
frame.f_globals['see'] = __import__('see', fromlist=['see']).see

# start ipdb with colors
shell = IPShell(argv=[''])
ip = ipapi.get()
Pdb(ip.options.colors).set_trace(frame)
