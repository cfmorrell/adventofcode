#!/usr/bin/env python3

import sys

def part1(steps):
	index = 1
	buf = [0,1]
	for i in range(2,2018):
		if i%100000 == 0:
			print(i)
		index = ((index + steps) % len(buf))+1
		buf.insert(index,i)
	i2017 = buf.index(2017)
	return buf[i2017+1]

def part2(steps):
	answer = 1
	index = 1
	for i in range(2,50000000):
		index = ((index + steps) % i)+1
		if index-1 == 0:
			answer = i
	return answer


teststeps = 3
realsteps = 366
print(part1(realsteps))
print(part2(realsteps))
