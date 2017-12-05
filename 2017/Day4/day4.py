#!/usr/bin/python

import sys
import itertools

filename = str(sys.argv[1])
f = open(filename, 'r')

count = 0
for line in f:
	words = line.strip().split()
	print words
	multiple = False
	for word in words:
		perms = set(itertools.permutations(word))
		totalCount = 0
		for perm in perms:
			testword = ''.join(perm)
			totalCount += words.count(testword)
			# print testword, totalCount
		if totalCount > 1:
			multiple = True
	if not multiple:
		print 'Valid'
		count += 1
	else:
		print 'Invalid'
print count