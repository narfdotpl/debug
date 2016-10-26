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
    # don't touch non-debug imports
    name = args[0]
    if name != 'debug':
        return old_import(*args, **kwargs)

    # Make sure that the name "debug" refers to *this* module,
    # i.e. that the import is `import debug` and not for example
    # `from .debug import foo`.
    #
    # To check this I have to look at the value of the `level`
    # argument.  It's the last argument and it has a default value.
    # I don't want to add it to the signature of `new_import` because
    # `__import__` is different in Python 2 and 3:
    #
    #     __import__(name, globals={}, locals={}, fromlist=[], level=-1)
    #     __import__(name, globals=None, locals=None, fromlist=(), level=0)
    #
    # I work around this by getting `level` from `kwargs` and `args`,
    # which works the same way in both Python versions.
    is_relative = False
    if 'level' in kwargs:
        is_relative = kwargs['level'] > 0
    elif len(args) == 5:
        is_relative = args[-1] > 0

    if is_relative:
        return old_import(*args, **kwargs)
    else:
        debug()

__builtin__.__import__ = new_import
