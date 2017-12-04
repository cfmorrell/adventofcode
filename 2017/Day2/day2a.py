#!/usr/bin/python

import sys

filename = str(sys.argv[1])
f = open(filename, 'r')

checksum = 0
for line in f:
	intline = [int(i) for i in line.split()]
	checksum += max(intline) - min(intline)
	print(checksum)