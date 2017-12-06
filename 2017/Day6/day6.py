#!/usr/bin/python

import sys
import copy
filename = str(sys.argv[1])

mem = [int(i) for i in open(filename, 'r').read().strip().split()]

seen = [copy.deepcopy(mem)]
moves = 0
# print(mem)

while 1:
	mem_to_move = max(mem)
	loc = mem.index(mem_to_move)
	mem[loc] = 0
	for i in range(loc+1,loc+mem_to_move+1):
		mem[i%len(mem)] += 1
	# print(mem,seen)
	moves += 1
	if seen.count(mem) == 2:
		break
	else:
		seen.append(copy.deepcopy(mem))

print(moves)