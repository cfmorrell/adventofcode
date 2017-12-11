#!/usr/bin/env python3

#https://github.com/stephanh42/hexutil

import hexutil
import sys

def part1(line):
	loc = [0,0]
	mvdict = {'n':(1,1),'ne':(2,0),'se':(1,-1),'s':(-1,-1),'sw':(-2,0),'nw':(-1,1)}
	for mv in line.split(','):
		loc[0] += mvdict[mv][0]
		loc[1] += mvdict[mv][1]
	hexloc = hexutil.Hex(loc[0],loc[1])
	return hexloc.distance(hexutil.origin)


def part2(line):
	dist = 0
	loc = [0,0]
	mvdict = {'n':(1,1),'ne':(2,0),'se':(1,-1),'s':(-1,-1),'sw':(-2,0),'nw':(-1,1)}
	for mv in line.split(','):
		loc[0] += mvdict[mv][0]
		loc[1] += mvdict[mv][1]
		hexloc = hexutil.Hex(loc[0],loc[1])
		if hexloc.distance(hexutil.origin) > dist:
			dist = hexloc.distance(hexutil.origin)
	return dist


filename = str(sys.argv[1])
f = open(filename, 'r')

for line in f:
	print('Final Distance:',part1(line.strip()))
	print('Max Distance:',part2(line.strip()))

