#!/usr/bin/python

import sys

filename = str(sys.argv[1])
f = open(filename, 'r')

checksum = 0
for line in f:
	intline = sorted([int(i) for i in line.split()])
	for i in intline:
		for j in intline:
			if i < j and j % i == 0:
				checksum += j / i
				break
	print(checksum)