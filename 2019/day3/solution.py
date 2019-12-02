#!/usr/bin/python

import sys


def func(fn):
    """
    >>> func("test1.txt")
    >>> func("test2.txt")
    >>> func("test3.txt")
    >>> func("test4.txt")
    """
    f = open(fn, 'r')
    for line in f:
        print(line)

    f.close()


if __name__ == "__main__":
    filename = str(sys.argv[1])
    print(func(filename))
