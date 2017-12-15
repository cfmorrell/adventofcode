#!/usr/bin/env python3

import sys

def part1(start):
	a,b = start
	afactor = 16807
	bfactor = 48271
	divisor = 2147483647
	matches = 0
	for i in range(40000000):
		if i%100000 == 0:
			print(i)
		a = (a * afactor) % divisor
		b = (b * bfactor) % divisor
		if bin(a)[-16:] == bin(b)[-16:]:
			matches += 1
	return matches

def part2(start):
	a,b = start
	afactor = 16807
	bfactor = 48271
	divisor = 2147483647
	matches = 0
	for i in range(5000000):
		if i%10000 == 0:
			print(i)
		a = (a * afactor) % divisor
		while a % 4 != 0:
			a = (a * afactor) % divisor
		b = (b * bfactor) % divisor
		while b % 8 != 0:
			b = (b * bfactor) % divisor
		if bin(a)[-16:] == bin(b)[-16:]:
			matches += 1
	return matches

teststart = (65,8921)
realstart = (512,191)
print(part1(realstart))
#print(part2(realstart))
