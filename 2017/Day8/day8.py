#!/usr/bin/python

import sys

filename = str(sys.argv[1])
f = open(filename, 'r')

maxval = 0
registers = {}
for line in f:
	cmds = line.strip().split()
	if cmds[0] not in registers:
		registers[cmds[0]] = 0
	if cmds[4] not in registers:
		registers[cmds[4]] = 0
	if eval(str(registers[cmds[4]]) + cmds[5] + cmds[6]):
		if cmds[1] == 'inc':
			registers[cmds[0]] += int(cmds[2])
		else:
			registers[cmds[0]] -= int(cmds[2])
	if max(registers.values()) > maxval:
		maxval = max(registers.values())
	print maxval