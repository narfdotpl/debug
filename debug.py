#!/usr/bin/env python
# encoding: utf-8
"""
import debug: https://github.com/narfdotpl/debug
"""

try:
    import __builtin__
except ImportError:
    # Python 3.x
    import builtins as __builtin__
from sys import _getframe

from ipdb import set_trace


# do not forget
old_import = __builtin__.__import__

def debug():
    # get frame
    frame = _getframe(2)

    # inject see (`from see import see`)
    ns = frame.f_globals
    if 'see' not in ns:
        ns['see'] = old_import('see', fromlist=['see']).see

    # start ipdb
    set_trace(frame)

# run on first import
debug()

# monkeypatch `import` so `import debug` will work every time
def new_import(*args, **kwargs):
    name = args[0]
    level = args[-1]
    is_absolute = level is None or level == 0

    if name == 'debug' and is_absolute:
        debug()
    else:
        return old_import(*args, **kwargs)

__builtin__.__import__ = new_import
