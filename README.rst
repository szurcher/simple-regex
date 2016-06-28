Simple-RegEx
------------

A simple command line tool to apply a regular expression search to an input file, and output the text with the matches replaced using a String.format()-style replacement string.

For example::

    simple-regex '[au](ll)' 'e{0}' infile.txt

If infile.txt contains::

    Hallo hullo

The program will output::

    Hello hello

Install
=======

Download and extract `dist/simple-regex-0.1.0.tar.gz`__, or clone this repo with::

  git clone https://github.com/szurcher/simple-regex.git

__ dist/simple-regex-0.1.0.tar.gz

From the simple-regex directory, run::

    python setup.py install

Built-in Help
=============

If you run ```simple-regex -h``` you will get the following help output::

    usage: simple-regex.py [-h] [-x [DEBUG]] find replace infile [outfile]

    Regular expression find and replace.

    positional arguments:
      find                  Pattern to use in searches.
      replace               Python format string to use for replacing matches.
      infile                File to be searched.
      outfile               File to output modified result.

    optional arguments:
      -h, --help            show this help message and exit
      -x [DEBUG], --debug [DEBUG]
                            Specify debug output level (results in regex.log)

Notes
=====

* Use single quotes (') around find and replace patterns to avoid shell expansion.

* ```outfile``` is there for convenience.  By default output is sent to STDOUT, but if you specify an outfile it will receive the text with replacements instead.  ```infile``` is required as the program does **not** read STDIN.

* By default DEBUG level is ERROR and regex.log will be empty.  If you set ```-x INFO``` you will get a lot of (probably useless) info about where the program found matches.
