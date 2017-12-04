#!/usr/bin/python

import sys

filename = str(sys.argv[1])
f = open(filename, 'r')

for line in f:
	acc = 0
	jump = len(line.strip())/2
	for i,c in enumerate(line.strip()):
		# print(i,c)
		if c == line[(i+jump)%(len(line)-1)]:
			acc += int(c)
	print(line.strip(),acc)