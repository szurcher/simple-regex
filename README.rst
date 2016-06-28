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
