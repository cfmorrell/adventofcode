#!/usr/bin/python

import sys

filename = str(sys.argv[1])
f = open(filename, 'r')

for line in f:
	acc = 0
	for i,c in enumerate(line.strip()):
		# print(i,c)
		if c == line[(i+1)%(len(line)-1)]:
			acc += int(c)
	print(line.strip(),acc)