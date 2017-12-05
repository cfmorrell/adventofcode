#!/usr/bin/python

import sys

filename = str(sys.argv[1])
f = open(filename, 'r').read()

lst = [int(i) for i in f.strip().split()]
#print lst

loc = 0
jumps = 0
while loc < len(lst):
	old_loc = loc
	loc += lst[loc]
	if lst[old_loc] >= 3:
		lst[old_loc] -= 1
	else:
		lst[old_loc] += 1
	jumps += 1

print jumps
