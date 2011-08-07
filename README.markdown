import debug
============

Start fancy debugger in a single statement.

People debug with `print`.  It's great in simple cases.  Another
debugging tool, [pdb][], is less popular as it requires more effort: one
has to do a Google search, skim through documentation, type some long
"trace... sth", and all of this only to get some unfriendly two-color
shell that doesn't even seem to understand how tab key should work.

  [pdb]: http://docs.python.org/library/pdb.html

This project FTFY: you `import debug` and you find yourself in a
debugger with syntax highlighting, tab completion, and readable `dir()`
alternative.  From there you can pretend you're just using interactive
console -- you don't have to know any `pdb` commands, just remember that
"c" closes debugger and goes back to your program.

(What really happens is that we simply start [ipdb][] and import [see][]
for you.)

  [ipdb]: https://github.com/gotcha/ipdb
  [see]: http://inky.github.com/see/


Usage
-----

Put `import debug` right where you want to start debugging (it's like
[antigravity][]).

Thanks to some monkeys and some patches, it will work as many times as
you need it to.

  [antigravity]: http://xkcd.com/353/


Installation
------------

    pip install debug


Meta
----

This little piece of glue code is written by [Maciej Konieczny][].  It's
released into the [public domain][] and uses [semantic versioning][] for
release numbering.

  [Maciej Konieczny]: http://narf.pl/
  [public domain]: http://unlicense.org/
  [semantic versioning]: http://semver.org/
