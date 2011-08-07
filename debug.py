#!/usr/bin/env python
# encoding: utf-8
"""
import debug: https://github.com/narfdotpl/debug
"""

from sys import _getframe

from IPython import ipapi
from IPython.Debugger import Pdb
from IPython.Shell import IPShell


# get frame
frame = _getframe().f_back

# inject see (from see import see)
ns = frame.f_globals
if 'see' not in ns:
    ns['see'] = __import__('see', fromlist=['see']).see

# start ipdb with colors
shell = IPShell(argv=[''])
ip = ipapi.get()
Pdb(ip.options.colors).set_trace(frame)
