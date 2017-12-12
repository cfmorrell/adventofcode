#!/usr/bin/env python3

import sys

def part1(f):
	d = {}
	connected = []
	tobeadded = []
	for line in f:
		orig = int(line.split('<->')[0])
		destlst = [int(i) for i in line.split('<->')[1].split(',')]
		d[orig] = destlst
	tobeadded.extend(d[0])
	connected.append(0)
	while len(tobeadded) > 0:
		while len(tobeadded) > 0 and tobeadded[0] in connected:
			tobeadded.pop(0)
		else:
			if len(tobeadded) == 0:
				break
		tobeadded.extend(d[tobeadded[0]])
		connected.append(tobeadded.pop(0))	
		# print('C:',connected,'T:',tobeadded)
	return(len(connected))

def part2(f):
	d = {}
	connectedroot = []
	allconnected = []

	for line in f:
		orig = int(line.split('<->')[0])
		destlst = [int(i) for i in line.split('<->')[1].split(',')]
		d[orig] = destlst

	while len(allconnected) < len(d.keys()):
		for i in d.keys():
			if i not in allconnected:
				tobeadded = d[i]
				connected = [i]
				break
		while len(tobeadded) > 0:
			while len(tobeadded) > 0 and tobeadded[0] in connected:
				tobeadded.pop(0)
			else:
				if len(tobeadded) == 0:
					break
			# print('C:',connected,'T:',tobeadded)
			tobeadded.extend(d[tobeadded[0]])
			connected.append(tobeadded.pop(0))	
		allconnected.extend(connected)
		connectedroot.append(connected[0])
		# print(connectedroot)
	return len(connectedroot)

filename = str(sys.argv[1])
f = open(filename, 'r')

# print(part1(f))
print(part2(f))

