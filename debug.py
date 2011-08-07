#!/usr/bin/env python
# encoding: utf-8
"""
import debug: https://github.com/narfdotpl/debug
"""

from sys import _getframe

from ipdb import set_trace


# get frame
frame = _getframe().f_back

# inject see (from see import see)
ns = frame.f_globals
if 'see' not in ns:
    ns['see'] = __import__('see', fromlist=['see']).see

# start ipdb
set_trace(frame)
