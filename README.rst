RegEx
-----

A simple command line tool to apply a regular expression search to an input file, and output the text with the matches replaced using a String.format()-style replacement string.

For example::

    regex '[au](ll)' 'e{0}' infile.txt

If infile.txt contains::

    Hallo hullo

The program will output::

    Hello hello
