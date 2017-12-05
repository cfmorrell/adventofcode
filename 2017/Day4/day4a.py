#!/usr/bin/python

import sys

filename = str(sys.argv[1])
f = open(filename, 'r')

for line in f:
  print line
