"""This is essentially a glorified "find . -name \*.pyc -exec rm -f {} \;"
except that since it's in python should work on any platform and I can just
add it to the list of default packages that get installed in my virtual
environments and know it will always be there whenever I'm using python.

"""

import logging
import argparse
import glob
import os

isdir = os.path.isdir


def safe_listdir(dir_):
    # To avoid permission denied, etc.
    try:
        return os.listdir(dir_)
    except:
        return []


def rmpyc_dir(options, dir_):
    fn_glob = os.path.join(dir_, options.glob)
    for pyc_file in glob.glob(fn_glob):
        os.remove(pyc_file)
    if options.recurse:
        paths = [os.path.join(dir_, fn) for fn in safe_listdir(dir_)]
        new_dirs = filter(isdir, paths)
        return new_dirs


def rmpyc(options):
    dir_lists = [options.dirs]
    while dir_lists:
        dirs = dir_lists.pop()
        for dir_ in dirs:
            new_dirs = rmpyc_dir(options, dir_)
            dir_lists.append(new_dirs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--glob",
                        help="",
                        default="*.pyc")
    parser.add_argument("-r", "--recurse",
                        action="store_true",
                        default=True)
    parser.add_argument("--no-recurse",
                        dest="recurse",
                        action="store_false",
                        default=False)
    parser.add_argument("dirs",
                        help="A list of directories to be cleansed.",
                        nargs="*",
                        default=[os.getcwd()])
    options = parser.parse_args()

    rmpyc(options)


if __name__ == "__main__":
    # This is so that this script can be invoked directly but if you
    # installed it via setuptools you should've gotten an "rmpyc"
    # executable in your path.
    main()
