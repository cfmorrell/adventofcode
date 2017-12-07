#!/usr/bin/python

import sys

filename = str(sys.argv[1])
f = open(filename, 'r')

nodeweight = {}
for line in f:
	node = line.split()[0]
	weight = int(line.split()[1][1:-1])
	nodeweight[node] = weight

f.seek(0)
for line in f:
	if '->' in line:
		parent = line.split('->')[0].strip().split()[0]
		children = [i.strip() for i in line.strip().split('->')[1].strip().split(',')]
		firstweight = nodeweight[children[0]]
		for child in children:
			print nodeweight[child]
			if nodeweight[child] != firstweight:
				print parent,child,children


# for node in allnodes:
# 	if allnodes.count(node) == 1:
# 		print node