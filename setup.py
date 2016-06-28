"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('simple_regex/regex.py').read(),
    re.M
    ).group(1)

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name = "simple-regex",
    packages = ["simple_regex"],
    entry_points = {
        "console_scripts": ['simple-regex = simple_regex.regex:main']
        },
    version = version,
    license = "BSD 2-Clause",
    description = "Regular expression search and replace on a file.",
    long_description = long_descr,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Environment :: Console',
        'Topic :: Text Processing :: Filters'
        ],
    keywords = 'regular expression find replace cli',
    include_package_data = True,
    author = "Stephen Zurcher",
    author_email = "stephen.zurcher@gmail.com",
    url = "http://szurcher.com",
    )
