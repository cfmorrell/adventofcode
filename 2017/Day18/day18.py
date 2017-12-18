#!/usr/bin/env python3

import sys

def is_digit(n):
	try:
		int(n)
		return True
	except:
		return False


def part1(i):
	registers = {}
	sound = 0
	ptr = 0
	while 1:
		if i[ptr][0] == 'set':
			if is_digit(i[ptr][2]):
				registers[i[ptr][1]] = int(i[ptr][2])
			else:
				registers[i[ptr][1]] = registers[i[ptr][2]]				
		elif i[ptr][0] == 'add' and i[ptr][1] in registers:
			if is_digit(i[ptr][2]):
				registers[i[ptr][1]] += int(i[ptr][2])
			else:
				registers[i[ptr][1]] += registers[i[ptr][2]]
		elif i[ptr][0] == 'mul' and i[ptr][1] in registers:
			if is_digit(i[ptr][2]):
				registers[i[ptr][1]] *= int(i[ptr][2])
			else:
				registers[i[ptr][1]] *= registers[i[ptr][2]]
		elif i[ptr][0] == 'mod' and i[ptr][1] in registers:
			if is_digit(i[ptr][2]):
				registers[i[ptr][1]] %= int(i[ptr][2])
			else:
				registers[i[ptr][1]] %= registers[i[ptr][2]]
		elif i[ptr][0] == 'rcv' and i[ptr][1] in registers:
			if registers[i[ptr][1]] != 0:
				return(sound)
		elif i[ptr][0] == 'jgz' and i[ptr][1] in registers:
			if registers[i[ptr][1]] > 0:
				ptr += int(i[ptr][2]) - 1
		elif i[ptr][0] == 'snd' and i[ptr][1] in registers:
			sound = registers[i[ptr][1]]
		else:
			print('Invalid instruction')
		# print(registers,sound,ptr)
		# input()
		ptr += 1

def part2():
	pass



testfile = 'sample.txt'
realfile = 'input.txt'

instructions = []
f = open(realfile,'r')
for line in f:
	instructions.append(tuple(line.split()))

print(part1(instructions))