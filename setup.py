#!/usr/bin/env python

import setuptools  # for side-effects to make "python setup.py develop" work
from distutils.core import setup

if __name__ == "__main__":
    setup(name="rmpyc",
          version="0.0.1",
          description=("Automatically remove all .pyc files from a"
                       " directory tree."),
          author="John Evans",
          author_email="lgastako@gmail.com",
          provides="rmpyc",
          entry_points = dict(console_scripts=["rmpyc = rmpyc:main"]))
