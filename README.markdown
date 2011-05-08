import debug
============

Start fancy debugger in a single statement.

People debug with `print`.  It's great in simple cases.  Another
debugging tool, [pdb][], is less popular as it requires more effort:
first, one has to spend a few minutes reading documentation and/or blag
posts, then type some long "trace" stuff instead of good old short
"print", and what one finally gets is an unfriendly two-color shell that
doesn't even seem to understand how tab key should work.

  [pdb]: http://docs.python.org/library/pdb.html

This project FTFY: you `import debug` and you immediately start
debugger with syntax highlighting, tab completion and readable `dir()`
alternative.  From there you can pretend you're just using interactive
console -- you don't have to know any `pdb` commands, just remember that
"c" closes debugger and goes back to your program.

(`import debug` simply starts [IPython][] debugger and imports [see][].)

  [IPython]: http://ipython.scipy.org/
  [see]: http://inky.github.com/see/


Usage
-----

Type `import debug` right where you want to start debugging (it's like
[antigravity][]).

  [antigravity]: http://xkcd.com/353/


Installation
------------

    pip install debug


Meta
----

This little glue code is written by [Maciej Konieczny][].  It's released
into the [public domain][] and uses [semantic versioning][] for release
numbering.

  [Maciej Konieczny]: http://narf.pl/
  [public domain]: http://unlicense.org/
  [semantic versioning]: http://semver.org/
